from flask import Flask, jsonify, request, Response, render_template
from loguru import logger

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_handler():
    logger.debug(request.headers)
    return jsonify({"Hello": "User"})


@app.route('/', methods=['POST'])
def post_handler():
    logger.debug(request.form.get('value'))
    logger.debug(request.headers)
    return render_template('request successful')


@app.after_request
def add_cors(response: Response):
    response.headers.add('Access-Control-Allow-Origin', 'https://www.google.com')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    response.headers.add('Access-Control-Allow-Headers', 'X-My-Fancy-Header')
    return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)

# fetch('http://127.0.0.1:8080', {method: 'GET'}).then(resp => resp.text()).then(console.log())
