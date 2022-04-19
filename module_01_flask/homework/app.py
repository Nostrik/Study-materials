import datetime
import random
from flask import Flask

app = Flask(__name__)
global vist_counter
vist_counter = 0


@app.route('/hello_world')
def hello_world():
   return 'Hello, world!'


@app.route('/cars')
def cars():
   return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def any_cat():
   cats = ['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']
   return random.choice(cats)


@app.route('/get_time/now')
def get_time_now():
   current_time = datetime.datetime.now()
   return f'Точное время {current_time}'


@app.route('/get_time/future')
def get_time_future():
   current_time = datetime.datetime.now()
   future_time = datetime.timedelta(hours=1)
   return f'Точное время через час будет {current_time + future_time}'


@app.route('/get_random_word')
def random_word():
   try:
      any_word = random.choice(random.choice(list(open('war_and_peace.txt', encoding='utf-8'))).split())
   except IndexError:
      any_word = 'any_word'
   return f'{any_word}'


@app.route('/visit')
def visit_func():
   global vist_counter
   vist_counter += 1
   return f'Page visit {vist_counter}'
