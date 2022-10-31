import json
import logging
from flask import Flask, request, make_response
from typing import Optional
from hw_models import init_db, DATA, Room, get_rooms, RoomEncoder, add_room, book_room

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[hw_API]')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/room')
def get_room():
    guest_num: Optional[str] = request.args.get('guestsNum')
    if guest_num:
        logger.debug(f'/room where guest_num == {guest_num}')
        guest_num: int = int(guest_num)
        rooms = get_rooms(guest_num)
        data: dict = {
            "properties": {
                "rooms": rooms
            }
        }
    else:
        logger.debug('guest_num is None')
        rooms: list[Room] = get_rooms()

        data: dict = {
            "rooms": rooms
        }
    return json.dumps(data, cls=RoomEncoder), 200


@app.route("/add-room", methods=["GET", "POST"])
def add_room_p():
    if request.method == "POST":
        add_room(DATA[1])
        return "<p>add-room POST</p>", 200
    return "<p>add-room GET</p>", 200


@app.route("/booking", methods=["POST"])
def booking():
    # logger.debug(type(c))
    # if request.method == 'POST':
    #     # logger.debug(f'booking -> {c["roomId"]}')
    #     return f"<p>booking POST {a, b}</p>", 200
    # if book_room(request.json):
    #     return make_response('Booking successful', 200)
    # return make_response('Room is already booked', 409)
    data: dict = {
        "rooms": book_room(request.json)
    }
    result = json.dumps(data, cls=RoomEncoder)
    return result


if __name__ == "__main__":
    init_db(DATA)
    app.run(debug=True)
