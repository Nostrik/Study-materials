import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/one')
@metrics.counter('counter', 'this code response 200 counter')
def one_route():
    time.sleep(random.random() * 0.2)
    return 'ok', 200


@app.route('/two')
@metrics.counter('counter', 'this code response 200 counter')
def two_route():
    time.sleep(random.random() * 0.4)
    return 'ok', 200


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
