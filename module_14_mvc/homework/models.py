import sqlite3
import logging
from typing import Any, Optional, List


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from models]')

DATA: list[dict] = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.', 'views_cnt': 0},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville', 'views_cnt': 0},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy', 'views_cnt': 0},
]


class Book:

    def __init__(self, id: int, title: str, author: str, views_cnt: int) -> None:
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.views_cnt: int = views_cnt

    def __getitem__(self, item) -> Any:
        return getattr(self, item)


def init_db(initial_records: list[dict]) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_books'; 
            """
        )
        exists: Optional[tuple[str, ]] = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                """
                CREATE TABLE `table_books` (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title, 
                    author,
                    views_cnt
                )
                """
            )
            cursor.executemany(
                """
                INSERT INTO `table_books`
                (title, author, views_cnt) VALUES (?, ?, ?)
                """,
                [
                    (item['title'], item['author'], item['views_cnt'])
                    for item in initial_records
                ]
            )


def get_all_books() -> list[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * from `table_books`
            """
        )
        # result = [Book(*row) for row in cursor.fetchall()]
        result = [increment_views_count(Book(*row)) for row in cursor.fetchall()]
        return result


def add_new_book(book_title, author_name):
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO `table_books`
            (title, author) VALUES (?, ?);
            """, (book_title, author_name)
        )


def get_book_by_author(name) -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * from `table_books`
            WHERE author = ?
            """, (name, )
        )
        res = [Book(*row) for row in cursor.fetchall()]
        return res


def get_book_by_id(book_id):
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        logger.debug(f'book id is - {book_id}')
        cursor.execute(
            """
            SELECT * FROM `table_books`
            WHERE id = ?
            """, (book_id, )
        )
        return [increment_views_count(Book(*row)) for row in cursor.fetchall()]


def increment_views_count(book_obj):
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT views_cnt FROM `table_books`
            WHERE id = ?
            """, (book_obj.id, )
        )
        value = cursor.fetchone()
        logger.debug(f'value is - {value[0]}')
        int_value = int(value[0])
        int_value += 1
        cursor.execute(
            """
            UPDATE `table_books`
            SET views_cnt = ?
            WHERE id = ?
            """, (book_obj.id, str(int_value))
        )
    return book_obj

