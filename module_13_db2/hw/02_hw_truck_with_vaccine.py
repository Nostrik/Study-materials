"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3
from itertools import groupby


sql_request = """
SELECT 
  count(*) 
FROM 
  (
    SELECT 
      * 
    FROM 
      table_truck_with_vaccine 
    WHERE 
      truck_number = ?
  ) 
WHERE 
  temperature_in_celsius BETWEEN 17.8 
  AND 18.2
"""
sample_truck_numbers = []


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    c.execute(sql_request, (truck_number, ))
    result = c.fetchone()
    if int(result[0]) != 0:
        return False
    else:
        return True


def get_truck_number(c: sqlite3.Cursor) -> list:
    c.execute("""SELECT truck_number FROM table_truck_with_vaccine""")
    result = c.fetchall()
    list_numbers = [res[0] for res in result]
    return [el for el, _ in groupby(list_numbers)]


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connect:
        cursor = connect.cursor()

    sample_truck_numbers = get_truck_number(cursor)
    for tr_number in sample_truck_numbers:
        print(f'Truck number {tr_number} vaccine good - ', check_if_vaccine_has_spoiled(cursor, tr_number))
