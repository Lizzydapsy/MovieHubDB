import psycopg2
from config import DB_CONFIG

def get_db_connection():
    """Connect to PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
