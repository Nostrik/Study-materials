"""
Пожалуйста, запустите скрипт generate_practice_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы practise.db
Юные школьники Иван, Даня и Игнат решили бороться за чистоту окружающего мира и собирать мусор в парках и лесах.

Удачным для себя они считают день, когда они собирают минимум 2 мешка пластиковых отходов и 1 мешок алюминия.
Крайне удачный день - когда в день сбора мусора они успевают так же отнести мешки на перерабатывающий завод.

Пожалуйста, напишите функцию, которая по номеру месяца возвращает процент крайней удачных дней у ребят в этом месяце по
отношению к общему числу дней в месяце

"""
import sqlite3

sql_request = """
SELECT COUNT(*)
    FROM 'table_green_future'
    WHERE action = 'отнесли мешки на завод'
"""
full_sql_request = """
SELECT 
  count(*) 
FROM 
  (
    SELECT 
      action 
    FROM 
      table_green_future 
    WHERE 
      date = '2021-?-01'
  ) 
WHERE 
  action = 'отнесли мешки на завод'
"""


def get_number_of_lucky_days(c: sqlite3.Cursor, month_number: int) -> float:
    c.execute(sql_request, (month_number,))
    request_result, *_ = c.fetchone()
    return request_result


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()

        percent_of_lucky_days = get_number_of_lucky_days(cursor, 12)

        print(f"В декабре у ребят было {percent_of_lucky_days:.02f}% удачных дня!")
