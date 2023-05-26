import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

CREATE_DIRECTOR_TABLE = """
DROP TABLE IF EXISTS 'director';
CREATE TABLE 'director' (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_last_name VARCHAR(50) NOT NULL
)
"""

CREATE_MOVIE_TABLE = """
DROP TABLE IF EXISTS 'movie';
CREATE TABLE 'movie' (
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50) NOT NULL
)
"""

CREATE_ACTORS_TABLE = """
DROP TABLE IF EXISTS 'actors';
CREATE TABLE 'actors' (
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50),
    act_last_name VARCHAR(50),
    act_gender VARCHAR(1)
)
"""

CREATE_MOVIE_DIRECTION_TABLE = """
DROP TABLE IF EXISTS 'movie_direction';
CREATE TABLE 'movie_direction' (
    dir_id INTEGER NOT NULL REFERENCES director (dir_id) ON DELETE CASCADE,
    mov_id INTEGER NOT NULL REFERENCES movie (mov_id) ON DELETE CASCADE
)
"""

CREATE_OSCAR_AWARDED_TABLE = """
DROP TABLE IF EXISTS 'oscar_awarded';
CREATE TABLE 'oscar_awarded' (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id INTEGER NOT NULL REFERENCES movie (mov_id) ON DELETE CASCADE
)
"""

CREATE_MOVIE_CAST_TABLE = """
DROP TABLE IF EXISTS 'movie_cast';
CREATE TABLE 'movie_cast' (
    act_id INTEGER NOT NULL REFERENCES actors(act_id) ON DELETE CASCADE,
    mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE CASCADE,
    role VARCHAR(50)
)
"""


def create_table():
    with sqlite3.connect("cinema_table.db") as connect:
        cursor = connect.cursor()

        cursor.executescript(ENABLE_FOREIGN_KEY)
        cursor.executescript(CREATE_DIRECTOR_TABLE)
        cursor.executescript(CREATE_MOVIE_TABLE)
        cursor.executescript(CREATE_ACTORS_TABLE)
        cursor.executescript(CREATE_MOVIE_DIRECTION_TABLE)
        cursor.executescript(CREATE_OSCAR_AWARDED_TABLE)
        cursor.executescript(CREATE_MOVIE_CAST_TABLE)


if __name__ == '__main__':
    create_table()
