from flask import Flask, jsonify, request
from database import get_movie_by_id, cache_movie
import redis
import psycopg2
import os

# Initialize Flask app
app = Flask(__name__)

# Database configurations
PG_DB_URL = os.getenv("PG_DB_URL", "your-postgresql-database-url")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

# PostgreSQL and Redis connections
pg_conn = psycopg2.connect(PG_DB_URL)
redis_conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

@app.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    # Check if movie data is in Redis cache
    movie = redis_conn.get(f"movie:{movie_id}")
    if movie:
        return jsonify({"source": "cache", "movie": movie.decode('utf-8')})

    # If not in cache, fetch from PostgreSQL
    movie = get_movie_by_id(pg_conn, movie_id)
    if movie:
        cache_movie(redis_conn, movie)
        return jsonify({"source": "database", "movie": movie})
    return jsonify({"message": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
