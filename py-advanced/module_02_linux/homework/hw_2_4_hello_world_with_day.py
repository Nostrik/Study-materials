"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
>>> import datetime
>>> print(datetime.datetime.today().weekday())
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<string:name>")
def hello_world(name) -> str:
    """Put your code here"""
    weekdays = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
                'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')
    day = datetime.datetime.today().weekday()
    return f'Привет, {name}. {weekdays[day]}!'


if __name__ == "__main__":
    app.run(debug=True)
