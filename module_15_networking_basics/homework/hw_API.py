import json
from flask import Flask, request
from typing import Optional

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/room')
def get_room() -> tuple[str, int]:
    guest_num: Optional[str] = request.args.get('guestsNum')
    if guest_num:
        guest_num: int = int(guest_num)
        rooms: list[Room] = get_rooms(guest_num)
        data: dict = {
            "properties": {
                "rooms": rooms
            }
        }
    else:
        rooms: list[Room] = get_rooms()
        data: dict = {
            "rooms": rooms
        }
    return json.dumps(data, cls=RoomEncoder), 200


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
