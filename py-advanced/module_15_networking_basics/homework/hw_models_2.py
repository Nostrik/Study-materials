import sqlite3
import logging
import json
from typing import Any, Optional


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[hw_models]')


class Room:
    def __init__(self, room_id: int, floor: int, guestnum: int, beds: int, price: int, date_in: int,
                 date_out: int, vacant: str) -> None:
        self.roomId: int = room_id
        self.floor: int = floor
        self.guestsNum: int = guestnum
        self.beds: int = beds
        self.price: int = price
        self.date_in: int = date_in
        self.date_out: int = date_out
        self.vacant: str = vacant

    def __getitem__(self, item) -> Any:
        return getattr(self, item)


class RoomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Room):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def init_db() -> None:
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
                    date_out,
                    vacant
                )
                """
            )


def get_rooms(guest_num: int = 0):
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        if guest_num == 0:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                """
            )
        else:
            cursor.execute(
                """
                SELECT * FROM `table_rooms`
                WHERE guestNum = ?
                """, (guest_num,)
            )
        return [Room(*row) for row in cursor.fetchall()]


def add_room(new_room: dict):
    floor: Optional[str] = new_room['floor']
    beds: Optional[str] = new_room['beds']
    guest_num: Optional[str] = new_room['guestNum']
    price: Optional[str] = new_room['price']
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO `table_rooms`
            (floor, guestNum, beds, price) VALUES (?, ?, ?, ?)
            """, (floor, guest_num, beds, price)
        )


def booking_room(booking_info):
    date_in = booking_info['bookingDates']['checkIn']
    date_out = booking_info['bookingDates']['checkOut']
    name = booking_info['firstName']
    surname = booking_info['lastName']
    room = booking_info['roomId']
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT vacant FROM `table_rooms`
            WHERE roomId = ?
            """, (room, )
        )
        check = cursor.fetchone()
        logger.debug(f'check vacant -> {check}')
        if check[0] == 'false':
            logger.debug(f'check vacant -> {check, type(check)}')
            return False
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE `table_rooms`
                SET date_in = ?, date_out = ?, vacant = ?
                WHERE roomId = ?
            """, (date_in, date_out, 'false', room)
        )
    with sqlite3.connect('table_rooms.bd') as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM `table_rooms`
            WHERE roomId = ?
            """, (room,)
        )
        result = cursor.fetchall()
    return [Room(*row) for row in result]
