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

# https://medium.com/python-pandemonium/asyncio-coroutine-patterns-beyond-await-a6121486656f


def is_valid(url: str):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


@logger.catch
async def get_all_links_on_page(url):
    async with aiohttp.ClientSession() as session:
        urls = set()
        domain_name = urlparse(url).netloc
        response = await session.get(url)
        # html = response.content
        html = await response.text()
        # a = response.content
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.findAll('a'):
            href = link.attrs.get('href')
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                continue
            if href in INTERNAL_URLS:
                continue
            if domain_name not in href:
                if href not in EXTERNAL_URLS:
                    # print(f"{GRAY}[!] Внешняя ссылка: {href}{RESET}")
                    logger.debug(f"{GRAY}[!] Внешняя ссылка: {href}{RESET}")
                    EXTERNAL_URLS.add(href)
            # print(f"{GREEN}[*] Внутреннея ссылка: {href}{RESET}")
            logger.debug(f"{GREEN}[*] Внутреннея ссылка: {href}{RESET}")
            urls.add(href)
            global TOTAL_URL_CNT
            TOTAL_URL_CNT += 1
            INTERNAL_URLS.add(href)
            # time.sleep(0.2)
        return urls


async def write_to_file():
    async with aiofiles.open('result.txt', mode='a') as file:
        for i_link in INTERNAL_URLS:
            await file.write(i_link + '\n')
        for i_link in EXTERNAL_URLS:
            await file.write(i_link + '\n')


@logger.catch
def crawl(url, max_urls=5000):
    logger.info(f"{YELLOW}[*] Проверено: {url}{RESET}")
    links = asyncio.run(get_all_links_on_page(url))
    if links is not None:
        for link in links:
            if TOTAL_URL_CNT > max_urls:
                break
            asyncio.create_task(crawl(link, max_urls=max_urls))


@logger.catch
def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(crawl(URL))
    asyncio.run(write_to_file())


if __name__ == "__main__":
    start_time = time.strftime('%X')
    logger.info(f"started crawler at {start_time}")
    main()
    logger.info(f"was started at {start_time}")
    logger.info(f"finished crawler at {time.strftime('%X')}")
    logger.debug(f'total urls - {TOTAL_URL_CNT}')
