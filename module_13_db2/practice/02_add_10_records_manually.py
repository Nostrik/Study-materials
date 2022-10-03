"""
Пожалуйста, запустите скрипт generate_practice_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы practise.db
Урок 1, задание 2

Давайте начнём практику с более простого задания.

Есть база данных "practise.db", в которой есть таблица table_warehouse,
    которую мы видели на занятии.
Напишите функцию, которая принимает на вход объект курсор
    и добавляет в таблицу table_warehouse 10 различных записей.

"""
import sqlite3


class AddingItem:
    def __init__(self, name: str, description: str, amount: int) -> None:
        self.name = name
        self.description = description
        self.amount = amount


def input_new_item() -> AddingItem:
    name = input("Введите имя продукта\n>")
    description = input("Введите описание продукта\n>")
    amount = input("Введите остаток на складе\n>")

    amount_val = int(amount)

    return AddingItem(name=name, description=description, amount=amount_val)


def add_10_records_to_table_warehouse(cursor: sqlite3.Cursor) -> None:
    for _ in range(10):
        new_item = input_new_item()
        cursor.execute(
            """
            INSERT INTO 'table_warehouse' (name, description, amount) VALUES
                (?, ?, ?); 
            """,
            (new_item.name, new_item.description, new_item.amount),
        )


if __name__ == "__main__":
    with sqlite3.connect('practise.db') as connect:
        add_10_records_to_table_warehouse(connect.cursor())

