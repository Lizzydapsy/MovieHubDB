import psycopg2      # PostgreSQL adapter for Python to connect and interact with PostgreSQL databases
import redis         # Redis client library to interact with Redis key-value store
import configparser  # Standard library module to read configuration files (INI format)

# =====================================================
# Load configuration
# =====================================================
config = configparser.ConfigParser()  # Create a ConfigParser object to read INI files
config.read('backend/config.ini')     # Read the configuration file located at 'backend/config.ini'

# =====================================================
# PostgreSQL configuration
# =====================================================
DB_CONFIG = {
    'user': config['postgresql']['user'],       # PostgreSQL username from config
    'password': config['postgresql']['password'], # PostgreSQL password from config
    'host': config['postgresql']['host'],       # Database host (e.g., localhost or remote server)
    'port': config['postgresql']['port']        # Port number PostgreSQL listens on (usually 5432)
}

# =====================================================
# Redis configuration
# =====================================================
REDIS_CONFIG = {
    'host': config['redis']['host'],  # Redis server host (e.g., localhost or remote)
    'port': config['redis']['port']   # Redis server port (usually 6379)
}

# =====================================================
# Function to connect to PostgreSQL
# =====================================================
def get_db_connection():
    """
    Connect to PostgreSQL database using DB_CONFIG and return a connection object.
    Returns None if the connection fails.
    """
    try:
        # Establish a connection using psycopg2 and the configuration parameters
        conn = psycopg2.connect(**DB_CONFIG)
        return conn  # Return the connection object to be used elsewhere
    except Exception as e:
        # Print the error for debugging and return None
        print("Database connection error:", e)
        return None

# =====================================================
# Create Redis client
# =====================================================
redis_client = redis.StrictRedis(
    **REDIS_CONFIG,        # Pass host and port from configuration
    decode_responses=True  # Ensures Redis returns strings instead of bytes
)
