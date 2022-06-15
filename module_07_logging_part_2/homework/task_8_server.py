import logging
from flask import Flask, request


app = Flask(__name__)
logger = logging.getLogger('server_logger')
logging.basicConfig()
logger.setLevel('DEBUG')
handler = logging.FileHandler('task_8_log_ser.log', mode='w')
formatter = logging.Formatter(fmt="(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s |")
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route("/log-entry", methods=["POST"])
def accept_log_entry():
    msg = request.form.get('msg')
    logger.debug(msg)
    return f'{msg}'


@app.route("/query-example")
def query_example():
    return "Query example"


if __name__ == '__main__':
    app.run(debug=True)
    # logging.basicConfig(level=logging.debug(), filename='task_8_log_ser.log')
    #  curl -X POST http://localhost:5000/log-entry --data "msg=test"
