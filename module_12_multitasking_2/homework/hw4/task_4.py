import logging
import multiprocessing
import threading
import requests
import time
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool


logging.basicConfig(
    filename="task_4.log",
    level=logging.INFO,
    format="<%(threadName)s> - <%(message)s>"
)
logger = logging.getLogger(__name__)
date_url = "https://showcase.api.linx.twenty57.net/UnixTime/fromunix"
list_urls = [date_url] * 10


def work_func():
    """
    The function returns the current time using unix time stamp, converting it to human readable format.
    Writes a message log within 20 seconds.
    """
    url = date_url
    from_time = str(time.time())[:10]
    request = requests.get(url, params={'timestamp': from_time})
    time_start = time.time()
    current_time = 0
    log_data_list = []
    while current_time - time_start < 5:
        # logger.info(request.text)
        log_data_list.append(request.text)
        current_time = time.time()
    for i_log in log_data_list:
        logger.info(i_log)


if __name__ == "__main__":
    # pool = ThreadPool(processes=10)
    # result = pool.map(work_func, list_urls)
    # pool.close()
    # pool.join()
    for i_thread in range(10):
        thread = threading.Thread(target=work_func)
        thread.start()
        thread.join()
        print(f"Thread number {i_thread} started")
        time.sleep(0.5)
    exit(0)
