# import threading
from queue import Queue
import time
import ntplib
import datetime as dt
import threading
import multiprocessing

# def thread_time_decorator(thread):
#     @wraps(thread)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         thread(*args, **kwargs)
#         end = time.perf_counter()
#         threading.current_thread().thread_duration = end - start
#     return wrapper

THREADS_AMOUNT = 3
THREADS_WORK_TIME = 5


def worker2(queue):
    ev = threading.Event()
    thr = threading.Thread(target=worker, args=(ev, queue))
    thr.start()
    thr.join(THREADS_WORK_TIME)
    ev.set()


def worker(e, queue):
    while True:
        # беру дату с ntp сервера, но они блочат запросы если брать слишком много/сликом часто.
        c = ntplib.NTPClient()
        response = c.request('pool.ntp.org')

        # print(f"finished {multiprocessing.current_process().name}/{threading.current_thread().name}-{dt.datetime.fromtimestamp(response.tx_time)} ")
        queue.put(f"finished {multiprocessing.current_process().name}/{threading.current_thread().name}-{dt.datetime.fromtimestamp(response.tx_time)} ")
        time.sleep(2)
        if e.is_set():
            break


def main():

    q = Queue()

    threads = [threading.Timer(1, function=worker2, args=(q,)) for _ in range(THREADS_AMOUNT)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    li = list(q.queue)
    # это впихнуть в файл:
    print(sorted(li, key=lambda d: d[-26]))

    # while not q.empty():
    #     print(q.get())

    # q.join()


if __name__ == '__main__':
    main()
