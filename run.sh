#!/bin/bash

# This script will start the necessary services and run the Flask application

# Define the PostgreSQL and Redis service names (you can adjust these based on your system or Docker setup)
PG_SERVICE_NAME="postgresql"
REDIS_SERVICE_NAME="redis-server"

# Start PostgreSQL service (this assumes the service name is 'postgresql')
echo "Starting PostgreSQL service..."
sudo systemctl start $PG_SERVICE_NAME

# Start Redis service (this assumes the service name is 'redis-server')
echo "Starting Redis service..."
sudo systemctl start $REDIS_SERVICE_NAME

# Set environment variables if necessary (you can also use a .env file for better security)
export PG_DB_URL="postgres://username:password@localhost:5432/movie_db"
export REDIS_HOST="localhost"
export REDIS_PORT="6379"

# Run the Flask app (make sure you're in the correct directory)
echo "Starting Flask application..."
cd backend
python app.py  # You can replace this with `flask run` if you have Flask CLI set up
