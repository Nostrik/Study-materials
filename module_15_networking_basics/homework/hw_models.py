import sqlite3
import logging
import random
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
    def __init__(self, roomid: int, floor: int, guestnum: int, beds: int, price: int) -> None:
        self.room_id: int = roomid
        self.floor: int = floor
        self.guests_num: int = guestnum
        self.beds: int = beds
        self.price: int = price

    def __getitem__(self, item) -> Any:
        return getattr(self, item)


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
