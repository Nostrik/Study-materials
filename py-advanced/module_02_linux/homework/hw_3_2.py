"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask
import time

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    try:
        valid_date = time.strptime(date, '%Y%m%d')
        if date in storage:
            storage[date] += number
        else:
            storage[date] = number
        return 'Данные сохранены'
    except ValueError:
        return 'Неверный формат даты!'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    sum_of_year = 0
    for date in storage:
        if date[:4] == str(year):
            sum_of_year += storage[date]
    return f'Суммарные траты за указанный год - {sum_of_year}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    sum_of_month = 0
    for date in storage:
        if date[:4] == str(year) and int(date[4:6]) == month:
            sum_of_month += storage[date]
    return f'Суммарные траты за указанный месяц{sum_of_month}'


if __name__ == "__main__":
    app.run(debug=True)
