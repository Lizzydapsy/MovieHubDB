from flask import Flask, request, jsonify
from connect_database import get_db_connection, redis_client
import time

app = Flask(__name__)

# =====================================================
# Helper: Convert PostgreSQL row to dictionary
# =====================================================
def row_to_dict(row):
    return {
        "movie_id": row[0],
        "title": row[1],
        "genre": row[2],
        "release_year": row[3],
        "rating": float(row[4]),
        "box_office_million_USD": float(row[5])
    }

# =====================================================
# Retrieve movies based on selected database
# =====================================================
def get_all_movies(db_choice):
    if db_choice not in ["redis", "postgres"]:
        return {"error": "Invalid database selection. Choose 'redis' or 'postgres'."}

    start_time = time.time()

    try:
        # -------------------------------
        # Redis (Hot Subset / Cache Layer)
        # -------------------------------
        if db_choice == "redis":
            movie_keys = redis_client.keys("movie:*")
            movies = []

            for key in movie_keys:
                movie_data = redis_client.hgetall(key)
                if movie_data:
                    movies.append({
                        "movie_id": int(key.split(":")[1]),
                        "title": movie_data["title"],
                        "genre": movie_data["genre"],
                        "release_year": int(movie_data["release_year"]),
                        "rating": float(movie_data["rating"]),
                        "box_office_million_USD": float(movie_data["box_office_million_USD"])
                    })

            execution_time = round((time.time() - start_time) * 1000, 2)
            return {
                "source": "Redis (Cache Layer - Hot Data Subset)",
                "execution_time_ms": execution_time,
                "count": len(movies),
                "data": movies
            }

        # -------------------------------
        # PostgreSQL (Full Dataset)
        # -------------------------------
        if db_choice == "postgres":
            conn = get_db_connection()
            if not conn:
                return {"error": "Could not connect to PostgreSQL."}

            cur = conn.cursor()
            cur.execute("SELECT * FROM movies;")
            rows = cur.fetchall()
            cur.close()
            conn.close()

            movies = [row_to_dict(row) for row in rows]
            execution_time = round((time.time() - start_time) * 1000, 2)

            return {
                "source": "PostgreSQL (Primary Database - Full Dataset)",
                "execution_time_ms": execution_time,
                "count": len(movies),
                "data": movies
            }

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# =====================================================
# API endpoint
# =====================================================
@app.route("/movies", methods=["GET"])
def get_all_movies_endpoint():
    db_choice = request.args.get("db", "postgres")
    result = get_all_movies(db_choice)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)

# =====================================================
# Run Flask
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)
