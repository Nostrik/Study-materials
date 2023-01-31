from loguru import logger
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import requests
import time

HEADERS = ''
URL = 'https://www.geeksforgeeks.org/'
reqs = requests.get(URL)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []


async def get_html(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            return await response.text()


def main():
    for link in soup.find_all('a'):
        logger.debug(link.get('href'))


if __name__ == "__main__":
    logger.info(f"started crawler at {time.strftime('%X')}")
    main()
    logger.info(f"finished crawler at {time.strftime('%X')}")
