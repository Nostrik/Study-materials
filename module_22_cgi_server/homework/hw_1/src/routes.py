from flask import jsonify, Flask

application = Flask(__name__)


@application.route('/hello')
@application.route('/hello/<username>')
def hello_world(username='username'):
    return jsonify(message='hello', name=username)

# def application(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!\n'
#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
#     if environ['url'] == '/hello':
#         return jsonify(output)
#     else:
#         get_username = environ['url'].split('/')
#         return jsonify(message='hello', username=get_username[1])
