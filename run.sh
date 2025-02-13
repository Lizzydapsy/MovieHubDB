#!/bin/bash

# Stop script on error
set -e

echo "🚀 Setting up the project..."

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/Scripts/activate

# Install dependencies
#echo "📦 Installing dependencies..."
#pip install -r backend/requirements.txt

# Run database migration
#echo "🛠️ Creating PostgreSQL tables..."
#python backend/models.py

# Populate database and Redis cache
#echo "📥 Populating PostgreSQL and Redis..."
#python backend/populate_db.py

# Start Flask API
echo "🚀 Starting Flask application..."
python backend/app.py
