import csv
import random
from connect_database import get_db_connection, redis_client
from decimal import Decimal

# =====================================================
# Populate PostgreSQL (Full Dataset)
# =====================================================
def populate_postgres():
    """Create the movies table and populate PostgreSQL from CSV."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to PostgreSQL.")
        return

    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS movies;
        CREATE TABLE movies (
            movie_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            release_year INT,
            rating FLOAT,
            box_office_million_USD FLOAT
        );
    """)

    with open('data/movies.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            cur.execute("""
                INSERT INTO movies (movie_id, title, genre, release_year, rating, box_office_million_USD)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (movie_id) DO NOTHING;
            """, row)

    conn.commit()
    cur.close()
    conn.close()
    print("PostgreSQL database populated successfully.")

# =====================================================
# Flush Redis hot movies
# =====================================================
def clear_redis_hot_movies():
    keys = redis_client.keys("movie:*")
    if keys:
        redis_client.delete(*keys)
        print(f"Cleared {len(keys)} old Redis entries.")
    else:
        print("Redis was already empty.")

# =====================================================
# Populate Redis with SUBSET (Hot Data)
# =====================================================
def populate_redis_subset(strategy="top_box_office", limit=10):
    """
    Populate Redis with a subset of PostgreSQL data.
    strategy options:
    - "top_box_office"
    - "random"
    """
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to PostgreSQL.")
        return

    cur = conn.cursor()

    if strategy == "top_box_office":
        cur.execute("""
            SELECT * FROM movies
            ORDER BY box_office_million_USD DESC
            LIMIT %s;
        """, (limit,))
        movies = cur.fetchall()

    elif strategy == "random":
        cur.execute("SELECT * FROM movies;")
        all_movies = cur.fetchall()
        movies = random.sample(all_movies, min(limit, len(all_movies)))

    cur.close()
    conn.close()

    store_movies_in_redis(movies)
    print(f"Redis populated with {len(movies)} hot movies.")

    # Debug: print total Redis entries after population
    total_keys = redis_client.keys("movie:*")
    print(f"Total Redis entries now: {len(total_keys)}")

# =====================================================
# Helper: Store Movies in Redis
# =====================================================
def store_movies_in_redis(movies):
    for movie in movies:
        redis_client.hset(f"movie:{movie[0]}", mapping={
            "title": movie[1],
            "genre": movie[2],
            "release_year": movie[3],
            "rating": float(movie[4]) if isinstance(movie[4], Decimal) else movie[4],
            "box_office_million_USD": float(movie[5]) if isinstance(movie[5], Decimal) else movie[5]
        })

# =====================================================
# Main Execution
# =====================================================
if __name__ == "__main__":
    # Populate PostgreSQL
    populate_postgres()

    # Clear old Redis entries
    clear_redis_hot_movies()

    # Populate Redis with top 10 movies
    populate_redis_subset(strategy="top_box_office", limit=10)