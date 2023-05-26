"""
В 20NN году оккультному автосалону "Чёртово колесо" исполняется ровно 13 лет.
    В честь этого они предлагает своим клиентам уникальную акцию:
    если вы обращаетесь в автосалон в пятницу тринадцатое и ваш автомобиль
    чёрного цвета и марки "Лада" или "BMW", то вы можете поменять колёса со скидкой 13%.
Младший менеджер "Чёртова колеса" слил данные клиентов в интернет,
    поэтому мы можем посчитать, как много клиентов автосалона могли воспользоваться
    скидкой (если бы они об этом знали). Давайте сделаем это!

Реализуйте функцию, c именем get_number_of_luckers которая принимает на вход курсор и номер месяца,
    и в ответ возвращает число клиентов, которые могли бы воспользоваться скидкой автосалона.
    Таблица с данными называется `table_occult_car_repair`
"""

import sqlite3

sql_request = """
SELECT count(*) FROM table_occult_car_repair
WHERE strftime("%m", timestamp) = ?
"""


def get_number_of_luckers(c: sqlite3.Cursor, m: str) -> str:
    c.execute(sql_request, (m,))
    result = c.fetchone()
    return result


if __name__ == "__main__":
    month = input('Введите номер месяца: ')
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        get_number_of_luckers(cursor, month)
        print(get_number_of_luckers(cursor, month))
