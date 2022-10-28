import json
import logging
from flask import Flask, request, jsonify
from typing import Optional
from hw_models import init_db, DATA, Room, get_rooms, RoomEncoder, add_room

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from hw_API]')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/room', methods=["GET", "POST"])
def get_room():
    guest_num: Optional[str] = request.args.get('guestsNum')
    if guest_num:
        logger.debug(f'/room where guest_num == {guest_num}')
        guest_num: int = int(guest_num)
        rooms: list[Room] = get_rooms(guest_num)
        data: dict = {
            "properties": {
                "rooms": rooms
            }
        }
        # return jsonify(data)
    else:
        logger.debug('guest_num is None')
        rooms: list[Room] = get_rooms()

        data: dict = {
            "rooms": rooms
        }
    return json.dumps(data, cls=RoomEncoder), 200
# https://isotropic.co/how-to-fix-cannot-read-property-0-of-undefined-in-js/


@app.route("/add-room", methods=["GET", "POST"])
def add_room_p():
    if request.method == "POST":
        add_room(DATA[1])
        return "<p>add-room POST</p>"
    return "<p>add-room GET</p>", 200


@app.route("/booking", methods=["GET", "POST"])
def booking():
    return "<p>booking endpoint</p>", 200


if __name__ == "__main__":
    init_db(DATA)
    app.run(debug=True)
