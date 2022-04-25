"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers: str):
    """Put your code here"""
    numbers_as_num = (int(it) for it in numbers.split("/"))
    return f'Максимальное переданное число <b>{max(numbers_as_num)}</b>'


if __name__ == "__main__":
    app.run(debug=True)
