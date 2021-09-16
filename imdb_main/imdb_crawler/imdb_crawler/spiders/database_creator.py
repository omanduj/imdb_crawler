import sqlite3

def data_base_setup():
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
                stars text
            ) """)

    conn.commit()
    conn.close()

def insert_info(name, release_date, viewer_rating, runtime, genre, stars):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("""INSERT INTO movie_info (name, release_date, viewer_rating, runtime, genre, stars)
                VALUES (:name, :release_date, :viewer_rating, :runtime, :genre, :stars)""",
                {'name': name, 'release_date': release_date, 'viewer_rating': viewer_rating,
                'runtime': runtime, 'genre': genre, 'stars': stars})

    conn.commit()
    conn.close()

def see_all():
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    c.execute("SELECT * FROM movie_info")

    info = c.fetchall()
    return info

def main():
    data_base_setup()
    see_all()
main()
