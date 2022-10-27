import sqlite3
import logging
import random
import json
from typing import Any, Optional, List


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from hw_models]')

DATA: list[dict] = [
    {'floor': random.randint(1, 5), 'guestNum': 2, 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000), 'date_in': 0, 'date_out': 0},
    {'floor': random.randint(1, 5), 'guestNum': random.randint(1, 40), 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000), 'date_in': 0, 'date_out': 0},
    {'floor': random.randint(1, 5), 'guestNum': random.randint(1, 40), 'beds': random.randint(1, 3),
     'price': random.randint(1500, 4000), 'date_in': 0, 'date_out': 0},
]


class Room:
    def __init__(self, room_id: int, floor: int, guestnum: int, beds: int, price: int, date_in: int,
                 date_out: int) -> None:
        self.roomId: int = room_id
        self.floor: int = floor
        self.guestsNum: int = guestnum
        self.beds: int = beds
        self.price: int = price
        self.date_in: int = date_in
        self.date_out: int = date_out

    def __getitem__(self, item) -> Any:
        return getattr(self, item)


class RoomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Room):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


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
                    roomId INTEGER PRIMARY KEY AUTOINCREMENT,
                    floor,
                    guestNum,
                    beds,
                    price,
                    date_in,
                    date_out
                )
                """
            )
            cursor.executemany(
                """
                INSERT INTO `table_rooms`
                (floor, guestNum, beds, price, date_in, date_out) VALUES (?, ?, ?, ?, ?, ?)
                """, [
                    (item['floor'], item['guestNum'], item['beds'], item['price'], item['date_in'],
                     item['date_out'])
                    for item in initial_records
                ]
            )
            logger.debug('table_rooms has been created..')


def get_rooms(guest_num: int = 0):
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        if guest_num == 0:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                """
            )
            tmp_result = cursor.fetchall()
        else:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                WHERE guestNum = ?
                """, (guest_num,)
            )
            tmp_result = cursor.fetchall()
    logger.debug(f'[get_rooms] -> {tmp_result}')
    result = [Room(*row) for row in tmp_result]
    return result


def add_room(new_room: dict):
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO `table_rooms`
            (floor, guestNum, beds, price, date_in, date_out) VALUES (?, ?, ?, ?, ?, ?)
            """, (new_room['floor'], new_room['guestNum'], new_room['beds'], new_room['price'], new_room['date_in'],
                  new_room['date_out'])
        )