import logging
import time
import sqlite3
import requests
import random
from pprint import pprint
from threading import Lock
from multiprocessing import Pool, cpu_count


logging.basicConfig(level=logging.INFO, format="[thread/num -%(threadName)s / %(thread)d ] [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)
characters = []
lock_db = Lock()


def get_character(number: int):
    response = requests.get(f'https://swapi.dev/api/people/{number}/')
    logger.info(f'Request number {number} to swapi..')
    if response.status_code != 200:
        logger.error('SWAPI is not available!')
    else:
        character = response.json()
        characters.append({
            'name': character['name'],
            'birth_year': character['birth_year'],
            'gender': character['gender']
        })
        lock_db.acquire()
        try:
            with sqlite3.connect("task_1_swapi.db") as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO characters (name, birth_year, gender) VALUES ("{}", "{}", "{}")'.format(
                    character["name"], character["birth_year"], character["gender"]
                ))
            logger.info(f'Characters name {character["name"]} is added')
        except Exception as er:
            logger.exception(er)
        lock_db.release()


def main():
    start_time = time.time()
    values = list(range(random.randint(1, 50)))

    with Pool(processes=cpu_count()) as pool:
        result = pool.map(get_character, values)

    time.sleep(3)
    logger.info(f'Time spent: {time.time() - start_time} - 3s')
    pprint(characters)


if __name__ == '__main__':
    main()
