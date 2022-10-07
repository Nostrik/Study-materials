"""
Юный натуралист Петя решил посетить Юнтоловский заказник на рассвете и записать журнал всех птиц,
    которых он увидел в заказнике. Он написал программу, но, в процессе написания,
    так устал, что уснул на клавиатуре, отчего пол-программы стёрлось.

Наш юный натуралист точно помнит, что программа позволяла добавить в БД новую птицу и говорила ему,
    видел ли он такую птицу раньше.

Помогите восстановить исходный код программы ЮНат v0.1 ,
    реализовав функции log_bird (добавление новой птицы в БД) и check_if_such_bird_already_seen
    (проверка что мы уже видели такую птицу)

Пожалуйста помогите ему, реализовав функцию log_bird .
    При реализации не забудьте про параметризацию SQL запроса!
"""

import datetime
import sqlite3

sql_insert_request = """
INSERT INTO 'table_birds' (brd_name, date) VALUES 
    (?, ?)
"""
sql_select_request = """
SELECT count(*) FROM 'table_birds'
    WHERE brd_name = ?
"""


def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    c.execute(sql_insert_request, (bird_name, date_time))


def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    c.execute(sql_select_request, (bird_name, ))
    result = c.fetchone()
    if result != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        log_bird(cursor, name, right_now)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
