from database_creator import data_base_setup, insert_info, see_all
import json
import sqlite3

def get_json():
    """Purpose: To load data from output of scrappy web crawler
       Paramaters: N/a
       Return Value: data = All data obtained by web crawler
    """
    file = open('A.json',)
    data = json.load(file)
    file.close()
    return data

def fill_movies(movie_json):
    """Purpose: Fills SQL database with info on movies
       Paramaters: movie_json = Information of all movies obtained from web crawler
       Return Value: N/a
    """
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
    """Purpose: Reorganize data to fit JSON format
       Paramaters: data = Information about movies
       Return Value: movie_dict = A dictionary of reorganized data
    """
    movie_info = 0
    movie_dict = {}
    for movie in range(len(data)):
        print(movie)
        movie_dict[movie_info] = {
                             'stars': data[movie][6],
                             'personal_rating': data[movie][7],
                             'name': data[movie][1],
                             'genre': data[movie][5],
                             'viewer_rating': data[movie][3],
                             'runtime': data[movie][4],
                             'release_date': data[movie][2],
                             }
        movie_info +=1
    return movie_dict

def select_genre(genre):
    """Purpose: To select all movies of X genre
       Paramaters: genre = Genre of movie
       Return Value: movies_of_genre = All movies of X genre
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT name, viewer_rating, runtime, genre, stars, personal_rating FROM movie_info WHERE Genre LIKE '%{}%'""".format(genre))
    movies_of_genre = c.fetchall()

    conn.commit()
    conn.close()

    return movies_of_genre

def find_avg_stars(genre):  #ISSUE WITH DUPLICATES
    """Purpose: To find average amount of stars for X genre
       Paramaters: genre = Genre of movie
       Return Value: stars_of_genre = Integer of stars
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT AVG(stars) FROM movie_info WHERE genre like '%{}%'""".format(genre))
    stars_of_genre = c.fetchall()

    conn.commit()
    conn.close()
    return float(str(stars_of_genre[0][0])[:5])

def avg_runtime_genre(genre):
    """Purpose: To find average runtime for X genre
       Paramaters: genre = Genre of movie
       Return Value: str_final = Formatted average duration for X genre
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT AVG(runtime) FROM movie_info WHERE genre like '%{}%'""".format(genre))
    runtime_of_movie = c.fetchall()

    conn.commit()
    conn.close()
    str_final = ''
    str_final += str(float(str(runtime_of_movie[0][0])[:5]))
    str_final += ' min'
    return str_final

def update_personal_rating(my_rating, movie):
    """Purpose: To update personal rating for a given movie
       Paramaters: my_rating = Rating that will be given to movie, movie = Movie that will take personal rating
       Return Value: N/a
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""UPDATE movie_info SET personal_rating = '{}' WHERE name like '%{}%'""".format(my_rating, movie))
    genre_of_movie = c.fetchall()

    conn.commit()
    conn.close()

def random_movie_picker(genre, personal_rating):
    """Purpose: To pick random movie given X specifications
       Paramaters: genre = Genre of movies being considered, personal_rating = personal rating being considered
       Return Value: random information of a single movie in json format
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT * FROM movie_info WHERE genre like '%{}%' AND personal_rating > '{}' ORDER BY RANDOM() LIMIT 1""".format(genre, personal_rating))
    genre_of_movie = c.fetchall()

    conn.commit()
    conn.close()
    return genre_of_movie

def see_all():
    """Purpose: To see all data in database
       Paramaters: N/a
       Return Value: movies = all info in database
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT * FROM movie_info""")
    movies = c.fetchall()

    conn.commit()
    conn.close()
    return movies

def insert_new_movie(name, release_date, viewer_rating, runtime, genre, stars):
    """Purpose: To insert data on a new movie provided by user
       Paramaters: name = Name of movie, release_date = Date of move release, viewer_rating = The
                    rating given to the movie for age viewing, runtime = The duration of movie,
                    genre = Genre of movie, stars = The star rating of movie
       Return Value: N/a
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""INSERT INTO movie_info (name, release_date, viewer_rating, runtime, genre, stars)
                VALUES (:name, :release_date, :viewer_rating, :runtime, :genre, :stars)""",
                {'name': name, 'release_date': release_date, 'viewer_rating': viewer_rating,
                'runtime': runtime, 'genre': genre, 'stars': stars})

    conn.commit()
    conn.close()

def select_a_movie(name):
    """Purpose: To select of of X name
       Paramaters: name = name of a movie
       Return Value:
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""SELECT id, name, viewer_rating, runtime, genre, stars, personal_rating, release_date FROM movie_info WHERE name LIKE '%{}%'""".format(name))
    movie_name = c.fetchall()

    conn.commit()
    conn.close()
    return movie_name

def main():
    # data_base_setup()
    information = get_json()
    fill_movies(information)
    # remove_duplicates()
main()
    # movies_of_genre = select_genre("Short")
    # update_personal_rating(10, "The Snowtown Crimes")
    # movies_of_genre = select_genre("Short")
    # avg_of_movies = find_avg_stars("Crime")
    # avg_runtime_genreX = avg_runtime_genre("Short")
    # print(avg_runtime_genreX)
    # x = (["The Snowtown Crimes", 5, "5 min", "Documentary, Short, Biography", 7.2, 5],["Sex, Fame and Murder: The Luka Magnotta Story","Not Rated","43 min","Documentary, Short, Crime",10.2,5])
    # fix_data(x)
    # x = random_movie_picker("Short", 5)
    # print(x)

# main()

#idea of personal rating for every movie
    #can search for movies of X personal rating
#idea of avg run time for each movie
