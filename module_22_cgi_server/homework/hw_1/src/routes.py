from flask import jsonify, Flask
import logging
import json

# application = Flask(__name__)
#
#
# @application.route('/hello')
# @application.route('/hello/<username>')
# def hello_world(username='username'):
#     return jsonify(message='hello', name=username)

logging.basicConfig(level=logging.INFO)
r_logger = logging.getLogger("[r_logger]")


def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    # for k in environ:
    #     r_logger.info('-' * 50)
    #     r_logger.info(k)
    #     r_logger.info(environ[k])
    #     r_logger.info('-' * 50)
    data = {'message': 'hello', 'name': 'username'}
    if environ['REQUEST_URI'] == '/hello':
        return jsonify(message='hello', name='username')
        # return json.dumps(message='hello', name='username')
        # return json.dump(data)
    else:
        get_username = environ['REQUEST_URI'].split('/')
        r_logger.info(get_username)
        return jsonify(message='hello', name=get_username[2])
