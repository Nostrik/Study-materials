"""
Пожалуйста, запустите скрипт generate_practice_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы practise.db
Параметризация запросов это очень важно (я не устану это повторять).
Давайте в качестве разминки напишем функцию,
    которая считывает список книг из файла построчно
    и добавляет их в БД practise.db в талицу table_books

При написании insert запроса, пожалуйста, используйте параметризованные SQL запросы.
"""
import sqlite3
import csv


class AddingBook:
    def __init__(self, book_name: str, author: str, publish_year: str, isbn: str) -> None:
        self.book_name = book_name
        self.author = author
        self.publish_year = publish_year
        self.isbn = isbn


def add_books_from_file(c: sqlite3.Cursor, file_name: str) -> None:
    with open(file_name) as csvfile:
        csv_obj = csv.reader(csvfile, delimiter=',')
        for row in csv_obj:
            print(row)
            book = AddingBook(row[1], row[2], row[3], row[0])
            c.execute(
                """
                INSERT INTO 'table_books' (book_name, author, publish_year, isbn) VALUES
                    (?, ?, ?, ?)
                """,
                (book.book_name, book.author, book.publish_year, book.isbn)
            )


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()

        add_books_from_file(cursor, "books_list.csv")
