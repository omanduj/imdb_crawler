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
                        movie_json[count]['runtime'], movie_json[count]['genre'], float(movie_json[count]['stars']))
        count += 1

def remove_duplicates():
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""WITH CTE AS '(SELECT *, RN = ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) FROM movie_info)'""")
    c.execute("""DELETE FROM CTE WHERE RN > 1""")
    conn.commit()
    conn.close()

    print(x)
    return duplicates

def fix_data(data):
    movie_info = 0
    dict1 = {}
    for movie in range(len(data)):
        print(movie)
        dict1[movie_info] = {
                             'stars': data[movie][6],
                             'personal_rating': data[movie][7],
                             'name': data[movie][1],
                             'genre': data[movie][5],
                             'viewer_rating': data[movie][3],
                             'runtime': data[movie][4],
                             'release_date': data[movie][2],
                             }
        movie_info +=1
    return dict1

def select_genre(genre):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT name, viewer_rating, runtime, genre, stars, personal_rating FROM movie_info WHERE Genre LIKE '%{}%'""".format(genre))
    movies_of_genre = c.fetchall()

    conn.commit()
    conn.close()

    return movies_of_genre

def find_avg_stars(genre):  #ISSUE WITH DUPLICATES
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT AVG(stars) FROM movie_info WHERE genre like '%{}%'""".format(genre))
    stars_of_genre = c.fetchall()

    conn.commit()
    conn.close()
    return float(str(stars_of_genre[0][0])[:5])

def avg_runtime_genre(genre):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT AVG(runtime) FROM movie_info WHERE genre like '%{}%'""".format(genre))
    runtime_of_movie = c.fetchall()

    conn.commit()
    conn.close()
    x = ''
    x += str(float(str(runtime_of_movie[0][0])[:5]))
    x += ' min'
    return x

def update_personal_rating(my_rating, movie):
    # genre_of_movie = select_genre(genre)
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""UPDATE movie_info SET personal_rating = '{}' WHERE name like '%{}%'""".format(my_rating, movie))
    genre_of_movie = c.fetchall()

    conn.commit()
    conn.close()

def random_movie_picker(genre, personal_rating):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT * FROM movie_info WHERE genre like '%{}%' AND personal_rating > '{}' ORDER BY RANDOM() LIMIT 1""".format(genre, personal_rating))
    genre_of_movie = c.fetchall()

    conn.commit()
    conn.close()
    return genre_of_movie

def see_all():
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT * FROM movie_info""")
    movies = c.fetchall()

    conn.commit()
    conn.close()
    return movies

def main():
    # data_base_setup()
    information = get_json()
    fill_movies(information)
    # remove_duplicates()

    # movies_of_genre = select_genre("Short")
    update_personal_rating(10, "The Snowtown Crimes")
    movies_of_genre = select_genre("Short")
    # avg_of_movies = find_avg_stars("Crime")
    avg_runtime_genreX = avg_runtime_genre("Short")
    # print(avg_runtime_genreX)
    # x = (["The Snowtown Crimes", 5, "5 min", "Documentary, Short, Biography", 7.2, 5],["Sex, Fame and Murder: The Luka Magnotta Story","Not Rated","43 min","Documentary, Short, Crime",10.2,5])
    # fix_data(x)
    x = random_movie_picker("Short", 5)
    print(x)

main()

#idea of personal rating for every movie
    #can search for movies of X personal rating
#idea of avg run time for each movie
