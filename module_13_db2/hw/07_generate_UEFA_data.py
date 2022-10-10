"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3
import random

commands_power = ["strong", "medium", "weak"]


def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    with open("countries.txt", "r") as countries:
        countries_file = countries.readlines()
    with open("commands.txt", "r") as commands:
        commands_file = commands.readlines()
    group = 1
    n = 1
    for i in range(number_of_groups):
        rows = [
            (n, random.choice(commands_file), random.choice(countries_file), commands_power[0]),
            (n+1, random.choice(commands_file), random.choice(countries_file), commands_power[1]),
            (n+2, random.choice(commands_file), random.choice(countries_file), commands_power[1]),
            (n+3, random.choice(commands_file), random.choice(countries_file), commands_power[2]),
        ]
        rows2 = [
            (n, n, group),
            (n+1, n+1, group),
            (n+2, n+2, group),
            (n+3, n+3, group)
        ]
        c.executemany("INSERT INTO 'uefa_commands' VALUES (?, ?, ?, ?)", rows)
        n += 4
        c.executemany("INSERT INTO 'uefa_draw' VALUES (? ,?, ?)", rows2)
        group += 1


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        generate_test_data(cursor, 4)
