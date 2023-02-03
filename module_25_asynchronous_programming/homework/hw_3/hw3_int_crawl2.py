from loguru import logger
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import colorama
import aiohttp
import asyncio
import aiofiles
import requests
import time
import sys

HEADERS = ''
URL = 'https://www.geeksforgeeks.org/'
reqs = requests.get(URL)
soup = BeautifulSoup(reqs.text, 'html.parser')
INTERNAL_URLS = set()
EXTERNAL_URLS = set()
TOTAL_URL_CNT = 0
TEST_URL = 'http://localhost:63342/python_advanced/module_25_asynchronous_programming/homework/hw_3/html_test/' \
           'index.html?_ijt=gavpvjmv983e68o8mtio0os865&_ij_reload'
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW


def is_valid(url: str):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


async def get_links_on_page(session, url):
    ...


async def crawl():
    async with aiohttp.ClientSession() as session:
        tasks = []

        while True:
            task = asyncio.create_task(get_links_on_page(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)



def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # res = asyncio.run(get_links_on_page(URL))
    one_page_res = asyncio.run(get_all_links_on_page(URL))



if __name__ == "__main__":
    start_time = time.strftime('%X')
    logger.info(f"started crawler at {start_time}")
    main()
    logger.info(f"was started at {start_time}")
    logger.info(f"finished crawler at {time.strftime('%X')}")
    logger.debug(f'total urls - {TOTAL_URL_CNT}')