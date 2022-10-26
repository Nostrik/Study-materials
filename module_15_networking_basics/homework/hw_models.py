import sqlite3
import logging
import random
import json
from typing import Any, Optional, List


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from hw_models]')

DATA: list[dict] = [
    {'room_id': 0, 'floor': random.randint(1, 5), 'guest_num': random.randint(1, 40), 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000)},
    {'room_id': 1, 'floor': random.randint(1, 5), 'guest_num': random.randint(1, 40), 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000)},
    {'room_id': 2, 'floor': random.randint(1, 5), 'guest_num': random.randint(1, 40), 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000)},
]


class Room:
    # room_id: int = 0
    # floor: int = 0
    # guests_num: int = 0
    # beds: int = 0
    # price: int = 0
    def __init__(self, roomid: int, floor: int, guestnum: int, beds: int, price: int) -> None:
        self.room_id: int = roomid
        self.floor: int = floor
        self.guests_num: int = guestnum
        self.beds: int = beds
        self.price: int = price

    def __getitem__(self, item) -> Any:
        return getattr(self, item)


class RoomEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.room_id, obj.floor, obj.guests_num, obj.beds, obj.price]


def init_db(initial_records: List[dict]) -> None:
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_rooms'; 
            """
        )
        exists: Optional[tuple[str, ]] = cursor.fetchone()
        if not exists:
            cursor.executescript(
                """
                CREATE TABLE `table_rooms` (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_id,
                    floor,
                    guest_num,
                    beds,
                    price
                )
                """
            )
            cursor.executemany(
                """
                INSERT INTO `table_rooms`
                (room_id, floor, guest_num, beds, price) VALUES (?, ?, ?, ?, ?)
                """, [
                    (item['room_id'], item['floor'], item['guest_num'], item['beds'], item['price'])
                    for item in initial_records
                ]
            )
            logger.debug('table_rooms has been created..')


# def get_rooms(guest_num: int = 0):
#     if guest_num == 0:
#         with sqlite3.connect('table_rooms.bd') as conn:
#             cursor: sqlite3.Cursor = conn.cursor()
#             cursor.execute(
#                 """
#                 SELECT * FROM `table_rooms`
#                 """
#             )
#             result = cursor.fetchall()
#     else:
#         with sqlite3.connect('table_rooms.bd') as conn:
#             cursor: sqlite3.Cursor = conn.cursor()
#             cursor.execute(
#                 """
#                 SELECT * FROM `table_rooms`
#                 WHERE guest_num = ?
#                 """, (str(guest_num), )
#             )
#             result = cursor.fetchall()
#
#     return [Room(*row) for row in result]


def get_rooms(guest_num: int = 0):
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        if guest_num == 0:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                """
            )
            result = cursor.fetchall()
        else:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                WHERE guest_num = ?
                """, (str(guest_num),)
            )
            result = cursor.fetchall()
    return [Room(*row) for row in result]