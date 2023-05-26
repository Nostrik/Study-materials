"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3


sql_request_select = """
SELECT salary FROM 'table_effective_manager'
    WHERE name = ?;
"""
sql_request_update = """
UPDATE 'table_effective_manager'
    SET salary = ?
    WHERE name = ?;
"""
sql_request_delete = """
DELETE FROM 'table_effective_manager'
    WHERE name = ?;
"""


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    c.execute(sql_request_select, (name, ))
    current_salary = c.fetchone()
    new_salary = (int(current_salary) * 0.1) + current_salary
    if new_salary < 100000:
        c.execute(sql_request_update, (str(new_salary), name))
    else:
        c.execute(sql_request_delete, (name, ))


if __name__ == "__main__":
    name_emp = input("Введите имя сотрудника:")
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        ivan_sovin_the_most_effective(cursor, name_emp)
