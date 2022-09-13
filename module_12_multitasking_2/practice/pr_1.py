import math
import time
import logging
import multiprocessing
from multiprocessing.pool import ThreadPool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
list_numbers = list(range(1, 10000))


def sum_fact(numbers: list):
    return sum(map(lambda x: math.factorial(x), numbers))


def run_sequential_approach():
    start = time.time()
    res = sum_fact(list_numbers)
    end = time.time()
    logger.info(f'Time taken in seconds for sequential - {end - start}')


def run_with_threadpool():
    pool = ThreadPool(processes=multiprocessing.cpu_count())
    start = time.time()
    res = pool.map(sum_fact, list_numbers)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Time taken in seconds with threadpool - {end - start}')


def run_with_processpool():
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    start = time.time()
    res = pool.map(sum_fact, list_numbers)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Time taken in seconds with processes pool - {end - start}')


if __name__ == "__main__":
    # run_sequential_approach()
    run_with_threadpool()
    # run_with_processpool()
