#!/bin/bash

# Stop script immediately if any command fails
set -e

echo "=== Setting up the project ==="

# ------------------------------
# Virtual Environment Setup
# ------------------------------
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv  # Create virtual environment in 'venv'
fi

# Activate virtual environment (Linux/macOS or Windows)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "ERROR: Virtual environment not found. Exiting."
    exit 1
fi

# ------------------------------
# Install Dependencies
# ------------------------------
echo "Installing Python dependencies..."
#pip install --upgrade pip 
#C:/Anaconda3/python.exe -m pip install --upgrade pip  # Upgrade pip first

python -m pip install -r backend/requirements.txt || { echo "Failed to install dependencies."; exit 1; }

# ------------------------------
# SSH Tunnel Setup
# ------------------------------
REMOTE_USER="dsdauser"
REMOTE_HOST="ml-lab-a1661695-3f22-4db4-89d6-01d3f0940288.westeurope.cloudapp.azure.com"
SSH_PORT=50798

echo "Checking SSH connectivity to $REMOTE_HOST..."
if ! ssh -p $SSH_PORT -q $REMOTE_USER@$REMOTE_HOST exit; then
    echo "ERROR: Cannot connect to remote server. Check SSH credentials or network."
    exit 1
fi

echo "Starting SSH tunnels in the background..."

# PostgreSQL tunnel
ssh -f -N -L 5432:localhost:5432 -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST || { echo "Failed to start PostgreSQL tunnel."; exit 1; }

# Redis tunnel
ssh -f -N -L 6379:localhost:6379 -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST || { echo "Failed to start Redis tunnel."; exit 1; }

# ------------------------------
# Populate Databases
# ------------------------------
echo "Populating PostgreSQL and Redis..."
if ! python backend/populate_db.py; then
    echo "ERROR: Failed to populate databases. Check populate_db.py."
    exit 1
fi

# ------------------------------
# Start Flask API
# ------------------------------
echo "Starting Flask application..."
if ! python backend/app.py; then
    echo "ERROR: Flask application failed to start."
    exit 1
fi
