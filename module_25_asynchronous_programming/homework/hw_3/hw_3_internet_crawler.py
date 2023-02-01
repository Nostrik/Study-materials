from loguru import logger
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import aiofiles
import requests
import time

HEADERS = ''
URL = 'https://www.geeksforgeeks.org/'
reqs = requests.get(URL)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
TOTAL_URL_CNT = 0
TEST_URL = 'http://localhost:63342/python_advanced/module_25_asynchronous_programming/homework/hw_3/html_test/' \
           'index.html?_ijt=gavpvjmv983e68o8mtio0os865&_ij_reload'

# https://waksoft.susu.ru/2021/04/14/kak-s-pomoshhyu-v-python-izvlech-vse-ssylki-na-veb-sajty/

# async def get_html(url: str):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=HEADERS) as response:
#             return await response.text()


# import aiohttp
# import lxml.html
#
# async def fetch_and_parse_links():
#     async with aiohttp.ClientSession() as session:
#         response = await session.get('https://www.example.com')
#         html = await response.text()
#         root = lxml.html.fromstring(html)
#         links = root.xpath('//a/@href')
#         return links


@logger.catch
async def get_links_on_page(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    for link in soup.find_all('a'):
        current_url = link.get('href')
        logger.debug(current_url)
        global TOTAL_URL_CNT
        TOTAL_URL_CNT += 1
        # await write_to_file(link.get('href'))
    if "https://" in current_url:
        await get_links_on_page(current_url)


@logger.catch
async def fetch_and_parse_links(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            logger.debug(link.get('href'))
            global TOTAL_URL_CNT
            TOTAL_URL_CNT += 1


async def write_to_file(link: str):
    async with aiofiles.open('result.txt', mode='a') as file:
        global TOTAL_URL_CNT
        TOTAL_URL_CNT += 1
        await file.write(link + '\n')


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    res = asyncio.run(get_links_on_page(URL))
    # res2 = asyncio.run(fetch_and_parse_links(URL))


if __name__ == "__main__":
    start_time = time.strftime('%X')
    logger.info(f"started crawler at {start_time}")
    main()
    logger.info(f"was started at {start_time}")
    logger.info(f"finished crawler at {time.strftime('%X')}")
    logger.debug(f'total urls - {TOTAL_URL_CNT}')
