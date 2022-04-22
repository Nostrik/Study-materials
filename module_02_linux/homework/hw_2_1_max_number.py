"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<float:number1>/<float:number2>/<float:number3>")
def max_number(number1, number2, number3):
    """Put your code here"""
    if number1 > number2 and number1 > number3:
        number = number1
    elif number2 > number3:
        number = number2
    else:
        number = number3
    return f'Максимальное переданное число <b>{number}</b>'


if __name__ == "__main__":
    app.run(debug=True)
