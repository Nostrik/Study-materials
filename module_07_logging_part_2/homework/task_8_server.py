from flask import Flask, request


app = Flask(__name__)


@app.route("/log-entry", methods=["POST"])
def accept_log_entry():
    msg = request.form.get('msg')
    return f'{msg}'


@app.route("/query-example")
def query_example():
    return "Query example"


if __name__ == '__main__':
    app.run(debug=True)
#  https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-ru
