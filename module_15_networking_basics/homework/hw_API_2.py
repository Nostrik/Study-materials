import json
import logging
from flask import Flask, request
from typing import Optional
from hw_models_2 import Room, RoomEncoder, get_rooms, init_db, add_room, booking_room

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


@app.route("/add-room", methods=["POST"])
def add_room_p():
    add_room(request.json)
    floor: Optional[str] = request.json['floor']
    beds: Optional[str] = request.json['beds']
    guest_num: Optional[str] = request.json['guestNum']
    price: Optional[str] = request.json['price']
    data: dict = {
        "method": "POST",
        "body": {
            "msg": 'Room added successful'
        },
        "url": "{{url}}/room?floor={{checkInDate}}&beds={{checkOutDate}}&guestsNum=2",
        "language": "json"
    }
    # return f'<h3>Room added successful</h3>', 200
    return


@app.route("/booking", methods=["POST"])
def book_room():
    answer = booking_room(request.json)
    logger.debug(f'booking answer is -> {answer}')
    if not answer:
        return "Can't book same room twice", 409
    return json.dumps(answer, cls=RoomEncoder), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
