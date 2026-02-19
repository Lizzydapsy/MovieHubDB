#!/bin/bash

# Stop script on error
set -e

echo "Setting up the project..."

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment (Linux/macOS)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
# Activate virtual environment (Windows)
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Virtual environment not found. Exiting."
    exit 1
fi

# Install required dependencies
echo "Installing dependencies..."
pip install -r backend/requirements.txt

# ------------------------------
# SSH Tunnels
# ------------------------------
echo "Starting SSH tunnels for PostgreSQL and Redis..."

# PostgreSQL tunnel (background)
ssh -f -N -L 5432:localhost:5432 -p 52817 dsdauser@ml-lab-7bebf525-b3be-4a32-98d5-e22665cb2333.westeurope.cloudapp.azure.com
# Redis tunnel (background)
ssh -f -N -L 6379:localhost:6379 -p 52817 dsdauser@ml-lab-7bebf525-b3be-4a32-98d5-e22665cb2333.westeurope.cloudapp.azure.com
# ------------------------------
# Populate PostgreSQL and Redis
# ------------------------------
echo "Populating PostgreSQL and Redis..."
python backend/populate_db.py

# Start Flask API
echo "Starting Flask application..."
python backend/app.py