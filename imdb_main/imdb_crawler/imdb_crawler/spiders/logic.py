from database_creator import data_base_setup, insert_info, see_all
import json
import sqlite3

def get_json():
    file = open('A.json',)
    data = json.load(file)
    file.close()
    return data

def fill_movies(movie_json):
    count = 0
    for line in range(len(movie_json)):
        if movie_json[count]['stars'] == None:
            movie_json[count]['stars'] = 0
        insert_info(movie_json[count]['name'], movie_json[count]['release_year'], movie_json[count]['viewer_rating'],
                        movie_json[count]['runtime'], movie_json[count]['genre'], movie_json[count]['stars'])
        count += 1

def select_genre(genre):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT name, viewer_rating, runtime, genre, stars FROM movie_info WHERE Genre LIKE '%{}%'""".format(genre))
    movies_of_genre = c.fetchall()

    conn.commit()
    conn.close()

    return movies_of_genre

def find_avg_stars(genre):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT name FROM movie_info""")
    movies_of_genre = c.fetchall()

    conn.commit()
    conn.close()
    return movies_of_genre


def main():
    data_base_setup()
    information = get_json()
    fill_movies(information)
    movies_of_genre = select_genre("Crime")
    avg_of_movies = find_avg_stars("Crime")
    print(movies_of_genre)
main()
