import logging
import random
import threading
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

COUNTER = 1
sem = threading.BoundedSemaphore(1)


def worker_one():
    global COUNTER
    sem.acquire()
    while COUNTER < 1000:
        COUNTER += 1

        logger.info(f'Worker one incremented counter to  {COUNTER}')
    sem.release()


def worker_two():
    global COUNTER
    sem.acquire()
    while COUNTER > -1000:
        COUNTER -= 1

        logger.info(f'Worker two decremented counter to  {COUNTER}')
    sem.release()


def main():
    start = time.time()
    thread_1 = threading.Thread(target=worker_one)
    thread_2 = threading.Thread(target=worker_two)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    logger.info(f'Execition time {time.time() - start}')


if __name__ == '__main__':
    main()
