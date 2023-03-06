import asyncio
import sys
from typing import Any
from loguru import logger
import aiohttp
from pprint import pprint


URL_USER = 'https://random-data-api.com/api/v2/users'
URL_COFFEE = 'https://random-data-api.com/api/coffee/random_coffee'
WANT_QUANTITY = 10
# logger.add(sys.stderr, format="{time} | {level} | {message}", level="INFO")


async def get_fake_user_data(client: aiohttp.ClientSession, idx: int) -> Any:
    async with client.get(URL_USER) as user:
        result = await user.json()
        # logger.debug(result)
        return result


async def get_fake_coffee_data(client: aiohttp.ClientSession, idx: int) -> Any:
    async with client.get(URL_COFFEE) as user:
        result = await user.json()
        # logger.debug(result)
        return result


async def get_all_fake_users():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as client:
        tasks = [get_fake_user_data(client, i) for i in range(WANT_QUANTITY)]
        return await asyncio.gather(*tasks)


async def get_all_fake_coffee():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as client:
        tasks = [get_fake_coffee_data(client, i) for i in range(WANT_QUANTITY)]
        return await asyncio.gather(*tasks)


def start_download():
    FAKE_USERS = asyncio.run(get_all_fake_users())
    logger.info('getting user data has finish')
    FAKE_COFFEES = asyncio.run(get_all_fake_coffee())
    logger.info('getting coffee data has finish')
    return FAKE_USERS, FAKE_COFFEES


# if __name__ == '__main__':
#     logger.info('Start getting users data')
#     start_download()
#     logger.info('Getting ALL data successful')
