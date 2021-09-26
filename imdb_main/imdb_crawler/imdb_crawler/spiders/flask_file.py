from flask import Flask, request, jsonify
from logic import select_genre, find_avg_stars, avg_runtime_genre, update_personal_rating, random_movie_picker, fix_data, see_all, insert_new_movie


app = Flask(__name__)

@app.route("/movies", methods = ["GET"])
def see_all_info():
    movies_info = see_all()
    data = fix_data(movies_info)
    return(jsonify({'movies': data}))

@app.route("/movies/genre", methods = ["POST"])
def search_movies_of_genre():
    some_json = request.get_json()
    movies_info = select_genre(some_json['genre'])
    data = fix_data(movies_info)
    return(
        jsonify({
                'movie_info': data
            }))

@app.route("/movies/genre", methods = ["GET"]) #FIX
def get_movies_of_genre():
    data = fix_data(movies_info)
    return(jsonify({'movies': data}))

@app.route("/movies/genre/average", methods = ["POST"])
def find_avg_stars_per_genre():
    some_json = request.get_json()
    movies_info = find_avg_stars(some_json['genre'])
    return(
        jsonify({
                'Avarage for stars for genre': movies_info
            }))

@app.route("/movies/genre/runtime/average", methods = ["POST"])
def find_avg_runtime_per_genre():
    some_json = request.get_json()
    movies_info = avg_runtime_genre(some_json['genre'])
    return(
        jsonify({
                'Avarage runtime for genre': movies_info #fix the over case -> 17:66
            }))

@app.route("/movies/update/personal_rating", methods = ["POST"])
def update_personal_rating_db():
    some_json = request.get_json()
    movies_info = update_personal_rating(some_json['my_rating'], some_json['movie'])
    return(
        jsonify({
                'message': 'Person rating for the movie has been updated!'
            }))

@app.route("/movies/random/movie", methods = ["POST"])
def get_random_movie():
    some_json = request.get_json()
    movies_info = random_movie_picker(some_json['genre'], some_json['personal'])
    info = fix_data(movies_info)
    return(
        jsonify({
                'message': info
            }))

@app.route("/new_movies", methods = ["POST"])
def insert_movie():
    some_json = request.get_json()
    insert_new_movie(some_json['name'],some_json['release_date'], some_json['viewer_rating'], some_json['runtime'], some_json['genre'], some_json['stars'])
    return(
        jsonify({
                'message': 'Movie Inserted!'
            }))


app.run(debug=True)
