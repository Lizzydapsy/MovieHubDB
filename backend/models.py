from database import get_db_connection

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        DROP TABLE IF EXISTS movies;  -- Drops the table if it exists
        CREATE TABLE IF NOT EXISTS movies (
            movie_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            release_year INT,
            rating FLOAT,
            box_office_million_USD FLOAT
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
