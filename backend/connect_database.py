import psycopg2
import redis
import configparser

config = configparser.ConfigParser()
config.read('backend/config.ini')

# PostgreSQL configuration
DB_CONFIG = {
    'user': config["postgresql"]["user"],
    'password': config['postgresql']['password'],
    'host': config['postgresql']['host'],
    'port': config['postgresql']['port']
}

# Redis configuration
REDIS_CONFIG = {
    'host': config['redis']['host'],
    'port': config['redis']['port']
}

# Connecting to PostgreSQL

def get_db_connection():
    """Connect to PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
    

# Connecting to redis

redis_client = redis.StrictRedis(**REDIS_CONFIG, decode_responses=True)

