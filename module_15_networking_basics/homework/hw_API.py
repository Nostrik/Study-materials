from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/add-room", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        return "<p>add-room POST</p>"
    return "<p>add-room GET</p>", 200


@app.route("/GetRoom", methods=["GET"])
def get_room():
    return "GetRoom worked", 200


@app.route("/booking", methods=["GET", "POST"])
def booking():
    return "<p>booking endpoint</p>", 200


if __name__ == "__main__":
    app.run(debug=True)
