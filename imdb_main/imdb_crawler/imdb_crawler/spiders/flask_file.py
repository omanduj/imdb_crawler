from flask import Flask, request, jsonify
from logic import select_genre, find_avg_stars, avg_runtime_genre, update_personal_rating, random_movie_picker, fix_data, see_all


app = Flask(__name__)

@app.route("/movies", methods = ["GET"])
def main0():
    movies_info = see_all()
    data = fix_data(movies_info)
    return(jsonify({'movies': data}))

@app.route("/movies/genre", methods = ["POST"])
def main():
    some_json = request.get_json()
    movies_info = select_genre(some_json['genre'])
    data = fix_data(movies_info)
    return(
        jsonify({
                'movie_info': data
            }))

@app.route("/movies/genre", methods = ["GET"])
def main2():
    data = fix_data(movies_info)
    return(jsonify({'movies': data}))

@app.route("/movies/genre/average", methods = ["POST"])
def main3():
    some_json = request.get_json()
    movies_info = find_avg_stars(some_json['genre'])
    # data = fix_data(movies_info)
    return(
        jsonify({
                'Avarage for stars for genre': movies_info
            }))

@app.route("/movies/genre/runtime/average", methods = ["POST"])
def main4():
    some_json = request.get_json()
    movies_info = avg_runtime_genre(some_json['genre'])
    # data = fix_data(movies_info)
    return(
        jsonify({
                'Avarage runtime for genre': movies_info #fix the over case -> 17:66
            }))

@app.route("/movies/update/personal_rating", methods = ["POST"])
def main5():
    some_json = request.get_json()
    movies_info = update_personal_rating(some_json['my_rating'], some_json['movie'])
    return(
        jsonify({
                'message': 'Person rating for the movie has been updated!'
            }))

@app.route("/movies/random/movie", methods = ["POST"])
def main6():
    some_json = request.get_json()
    movies_info = random_movie_picker(some_json['genre'], some_json['personal'])
    info = fix_data(movies_info)
    return(
        jsonify({
                'message': info
            }))


app.run(debug=True)
