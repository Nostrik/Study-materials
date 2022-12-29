import time
import random
import threading

import requests

endpoints = ('test_one', 'test_two')


def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get("http://app:5000/%s" % target, timeout=3)

        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)
