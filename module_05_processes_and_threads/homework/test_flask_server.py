import flask


app = flask.Flask(__name__)


@app.route("/start", methods=["GET"])
def run_server():
    return "Good, server is running"


if __name__ == '__main__':
    app.run(debug=True)
