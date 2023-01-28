import asyncio
from pathlib import Path

import aiohttp
import aiofiles
import time

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = Path(__file__).parent / 'cats'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


async def get_cat(client: aiohttp.ClientSession, idx: int) -> bytes:
    async with client.get(URL) as response:
        print(response.status)
        result = await response.read()
        await write_to_disk(result, idx)


async def write_to_disk(content: bytes, id: int):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    async with aiofiles.open(file_path, mode='wb') as f:
        await f.write(content)


def blocking_io(conent: bytes, id_c):
    print(f"start blocking_io at {time.strftime('%X')}")
    file_path = "{}/{}.png".format(OUT_PATH, id_c)
    with open(file_path, mode='wb') as file:
        file.write(conent)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def get_all_cats():

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_cat(client, i) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)


def main():
    res = asyncio.run(get_all_cats())
    print(len(res))


if __name__ == '__main__':
    main()
