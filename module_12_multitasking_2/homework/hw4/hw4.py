import time
import threading
import queue
import logging


logging.basicConfig(
    filename="log4.log",
    level=logging.INFO,
    format="<%(threadName)s> - <%(message)s>"
)
logger = logging.getLogger(__name__)


def worker(q: queue.Queue, lc: threading.Lock):
    # тут данные кладем в очередь


def writer(q: queue.Queue, lc: threading.Lock, ev: threading.Event):
    # тут данные сортирвем и достаем из очереди и записываем в файл


if __name__ == '__main__':
    start = time.time()
    lock = threading.Lock()
    event = threading.Event()
    buffer = queue.Queue()
    writer_thread = threading.Thread(target=writer, args=(buffer, lock, event,))
    writer_thread.start()
    threads = []

    for i in range(1, 11):
        thread = threading.Timer(i, function=worker, args=(buffer, lock,))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()
    event.set()

    end = time.time()
    logger.info(f'Finished in {end - start}')