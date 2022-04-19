import datetime
from flask import Flask

app = Flask(__name__)
global vist_counter
vist_counter = 0


@app.route('/test')
def test_function():
   return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                     datetime.datetime.now().utcnow()


@app.route('/hello_world')
def hello_world():
   return 'Hello, world!'


@app.route('/visit')
def visit_func():
   global vist_counter
   vist_counter += 1
   return f'Page visit {vist_counter}'
