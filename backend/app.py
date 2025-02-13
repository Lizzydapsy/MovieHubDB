from flask import Flask, request, jsonify
from database import get_db_connection  # Assuming the connection function for PostgreSQL
from redis_cache import redis_client  # Assuming the Redis client is configured here

app = Flask(__name__)

def get_all_movies(db_choice):
    """Try Redis first, then PostgreSQL based on db_choice to fetch all movies"""
    movies = None

    # Validate db_choice
    if db_choice not in ['redis', 'postgres']:
        return {"error": "Invalid database choice. Please choose 'redis' or 'postgres'."}
    
    try:
        if db_choice == "redis":
            # Fetch all movies from Redis (cache layer)
            # Assuming all movie entries are stored as a hash with keys "movie:{id}" in Redis
            movie_keys = redis_client.keys("movie:*")  # Get all keys starting with 'movie:'
            movies = []
            for key in movie_keys:
                movie_data = redis_client.hgetall(key)
                if movie_data:
                    movies.append(movie_data)
            
            # If no movies found in Redis, fetch from PostgreSQL
            if not movies:
                print("Movies not found in Redis, querying PostgreSQL...")
        
        if not movies and db_choice == "postgres":
            # Fetch all movies from PostgreSQL
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM movies")
            rows = cur.fetchall()
            
            movies = []
            for row in rows:
                movie = {
                    "movie_id": row[0],
                    "title": row[1],
                    "genre": row[2],
                    "release_year": row[3],
                    "rating": row[4],
                    "box_office_million_USD": row[5]
                }
                # Optionally store the fetched data in Redis for future use
                redis_client.hset(f"movie:{row[0]}", mapping=movie)
                movies.append(movie)

            cur.close()
            conn.close()
    
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

    return movies

@app.route("/movies", methods=["GET"])
def get_all_movies_endpoint():
    # Get the database choice from the query parameter (default to 'redis' if not provided)
    db_choice = request.args.get('db', 'redis')  # Default to 'redis' if no db is specified
    
    movies = get_all_movies(db_choice)
    
    if isinstance(movies, dict) and "error" in movies:
        # If there's an error message in the movie data (invalid db or exception occurred)
        return jsonify(movies), 400
    
    if movies:
        return jsonify(movies)
    else:
        return jsonify({"error": "No movies found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
