import sqlite3

def data_base_setup():
    """Purpose: To set up database that will be used
       Paramaters: N/a
       Return Value: N/a
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""DROP TABLE IF EXISTS movie_info""")

    c.execute("""CREATE TABLE movie_info (
                id integer primary key autoincrement,
                name text,
                release_date text,
                viewer_rating text,
                runtime text,
                genre text,
                stars integer,
                personal_rating integer
            ) """)

    conn.commit()
    conn.close()

def insert_info(name, release_date, viewer_rating, runtime, genre, stars):
    """Purpose: To fill data columns in movie_info database
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

def see_all():
    """Purpose: To view all info in the data base
       Paramaters: N/a
       Return Value: N/a
    """
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("SELECT * FROM movie_info")

    info = c.fetchall()
    return info

def main():
    data_base_setup()
    see_all()
main()
