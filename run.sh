#!/bin/bash

# Stop script on error
set -e

echo "Setting up the project..."

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/Scripts/activate

# Check if required dependencies are installed
if ! pip freeze | grep -q -F -f backend/requirements.txt; then
    echo "Installing dependencies..."
    pip install -r backend/requirements.txt
else
    echo "All dependencies are already installed."
fi

# Populate database and Redis cache
echo "Creating PostgreSQL tables..., Populating PostgreSQL and Redis..."
python backend/populate_db.py

# Start Flask API
echo "Starting Flask application..."
python backend/app.py
