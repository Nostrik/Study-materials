"""
На заводе "Дружба" работает очень дружный коллектив.
Рабочие работают посменно, в смене -- 10 человек.
На смену заходит 366 .

Бухгалтер завода составила расписание смен и занесла его в базу данных
    в таблицу `table_work_schedule`, но совершенно не учла тот факт,
    что все сотрудники люди спортивные и ходят на различные спортивные кружки:
        1. футбол (проходит по понедельникам)
        2. хоккей (по вторникам
        3. шахматы (среды)
        4. SUP сёрфинг (четверг)
        5. бокс (пятница)
        6. Dota2 (суббота)
        7. шах-бокс (воскресенье)

Как вы видите, тренировки по этим видам спорта проходят в определённый день недели.

Пожалуйста помогите изменить расписание смен с учётом личных предпочтений коллектива
    (или докажите, что то, чего они хотят - не возможно).
"""
import sqlite3
from pprint import pprint

sports_clubs = {
    'monday': 'football',
    'tuesday': 'hockey',
    'wednesday': 'chess',
    'thursday': 'sup',
    'friday': 'boxing',
    'saturday': 'dota2',
    'sunday': 'checkbox'
}


def update_work_schedule(c: sqlite3.Cursor) -> None:
    c.execute(
        "SELECT S.employee_id, date, name, preferable_sport, strftime('%w',date) as dow  FROM table_friendship_schedule S INNER JOIN table_friendship_employees E on E.id = S.employee_id " +
        " WHERE   (dow='0' and preferable_sport='шахбокс') or " +
        " (dow='1' and preferable_sport='футбол') or " +
        " (dow='2' and preferable_sport='хоккей') or " +
        " (dow='3' and preferable_sport='шахматы') or " +
        " (dow='4' and preferable_sport='SUP-сёрфинг') or " +
        " (dow='5' and preferable_sport='бокс') or " +
        " (dow='6' and preferable_sport='Dota2');"
        )
    result = c.fetchall()
    pprint(result)
    print(len(result))


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        update_work_schedule(cursor)
