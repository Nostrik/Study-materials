import json
import logging
from flask import Flask, request
from typing import Optional
from hw_models import init_db, DATA, Room, get_rooms, RoomEncoder, add_room

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from hw_API]')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/room')
def get_room() -> tuple[str, int]:
    guest_num: Optional[str] = request.args.get('guestNum')
    if guest_num:
        logger.debug(f'/room where guest_num == {guest_num}')
        guest_num: int = int(guest_num)
        rooms: list[Room] = get_rooms(guest_num)
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
        return "<p>add-room POST</p>"
    return "<p>add-room GET</p>", 200


# @app.route("/GetRoom", methods=["GET"])
# def g_room():
#     data: dict = {
#         "properties": {
#             "rooms": {
#                 "items": {
#                     "$id": "#/properties/rooms/items",
#                     "anyOf": [
#                         {
#                             "type": "object",
#                             "required": [
#                                 "roomId",
#                                 "floor",
#                                 "guestNum",
#                                 "beds",
#                                 "price"
#                             ],
#                             "properties": {
#                                 "roomId": {
#                                     "type": "integer"
#                                 },
#                                 "floor": {
#                                     "type": "integer"
#                                 },
#                                 "guestNum": {
#                                     "type": "integer"
#                                 },
#                                 "beds": {
#                                     "type": "integer"
#                                 },
#                                 "price": {
#                                     "type": "integer"
#                                 }
#                             }
#                         }
#                     ]
#                 }
#             }
#         }
#     }
#     response = json.dumps(data)
#     logger.debug(f'[g_room] -> {response}')
#     return data


@app.route("/booking", methods=["GET", "POST"])
def booking():
    return "<p>booking endpoint</p>", 200


if __name__ == "__main__":
    init_db(DATA)
    app.run(debug=True)
