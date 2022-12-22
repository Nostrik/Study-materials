from flask import Flask, jsonify
import time

application = Flask(__name__)


@application.route('/hello')
@application.route('/hello/<username>')
def hello_world(username='username'):
    return jsonify(message='hello', name=username)


@application.route('/long_task')
def long_task():
    time.sleep(30)
    return jsonify(message='we did it')
