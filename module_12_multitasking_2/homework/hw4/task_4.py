import logging
import multiprocessing

import requests
import time
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool


logging.basicConfig(

    level=logging.INFO,
    format="<%(threadName)s> - <%(message)s>"
)
logger = logging.getLogger(__name__)
date_url = "https://showcase.api.linx.twenty57.net/UnixTime/fromunix"
list_urls = [date_url] * 10


def work_func(url):
    """
    The function returns the current time using unix time stamp, converting it to human readable format.
    Writes a message log within 20 seconds.
    """
    from_time = str(time.time())[:10]
    request = requests.get(url, params={'timestamp': from_time})
    time_start = time.time()
    current_time = 0
    while current_time - time_start < 10:
        logger.info(request.text)
        current_time = time.time()


if __name__ == "__main__":
    pool = ThreadPool(processes=10)
    result = pool.map(work_func, list_urls)
    pool.close()
    pool.join()
