import csv
from connect_database import get_db_connection
from connect_database import redis_client
from decimal import Decimal


def populate_postgres():
    conn = get_db_connection()
    cur = conn.cursor()

    # Create table

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

    # Populate the table

    with open('data/movies.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            cur.execute("""
                INSERT INTO movies (movie_id, title, genre, release_year, rating, box_office_million_USD)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (movie_id) DO NOTHING;
            """, row)

    conn.commit()
    cur.close()
    conn.close()

def populate_redis():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()

    for movie in movies:
        # Convert Decimal values to float before inserting into Redis
        redis_client.hset(f"movie:{movie[0]}", mapping={
            "title": movie[1],
            "genre": movie[2],
            "release_year": movie[3],
            "rating": float(movie[4]) if isinstance(movie[4], Decimal) else movie[4],  # Convert Decimal to float
            "box_office_million_USD": float(movie[5]) if isinstance(movie[5], Decimal) else movie[5]  # Convert Decimal to float
        })

    cur.close()
    conn.close()

    cur.close()
    conn.close()

if __name__ == "__main__":
    
    populate_postgres()
    populate_redis()
