import psycopg2
import redis

# Function to fetch a movie from PostgreSQL by ID
def get_movie_by_id(pg_conn, movie_id):
    cursor = pg_conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE movie_id = %s", (movie_id,))
    movie = cursor.fetchone()
    if movie:
        return {"movie_id": movie[0], "title": movie[1], "genre": movie[2], "release_year": movie[3], "rating": movie[4], "box_office": movie[5]}
    return None

# Function to cache movie data in Redis
def cache_movie(redis_conn, movie):
    redis_conn.set(f"movie:{movie['movie_id']}", str(movie))
