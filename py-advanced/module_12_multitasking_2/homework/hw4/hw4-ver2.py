from queue import Queue
from pprint import pprint
import time
import ntplib
import datetime as dt
import threading
import multiprocessing
import logging

THREADS_AMOUNT = 10
THREADS_WORK_TIME = 20

logging.basicConfig(
    filename="log4.log",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def worker2(queue):
    event = threading.Event()
    thr = threading.Thread(target=worker, args=(event, queue))
    thr.start()
    thr.join(THREADS_WORK_TIME)
    event.set()


def worker(event, queue):
    while True:
        # беру дату с ntp сервера, но они блочат запросы если брать слишком много/сликом часто.
        current_time = ntplib.NTPClient()
        response = current_time.request('pool.ntp.org')

        queue.put(f"finished {multiprocessing.current_process().name}/{threading.current_thread().name}-"
                  f"{dt.datetime.fromtimestamp(response.tx_time)} ")
        time.sleep(2)
        if event.is_set():
            break


def main():
    print('Main thread start..')
    start = time.time()
    q = Queue()
    threads = [threading.Timer(1, function=worker2, args=(q,)) for _ in range(THREADS_AMOUNT)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    li = list(q.queue)
    sorted_treads = sorted(li, key=lambda d: d[-26])
    pprint(sorted_treads)
    for sor_tread in sorted_treads:
        logger.info(sor_tread)
    end = time.time()
    print(f'Finished in {end - start}')


if __name__ == '__main__':
    main()
