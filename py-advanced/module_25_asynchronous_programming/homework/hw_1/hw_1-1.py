import asyncio
from pathlib import Path
from loguru import logger
import aiohttp
import aiofiles
import time

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 100
OUT_PATH = Path(__file__).parent / 'cats2'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


async def get_cat(client: aiohttp.ClientSession, idx: int) -> bytes:
    async with client.get(URL) as response:
        logger.debug(f'status {response.status} for {idx}')
        result = await response.read()
        await write_to_disk(result, idx)


@logger.catch
def blocking_io(content: bytes, id_b):
    file_path = "{}/{}.png".format(OUT_PATH, id_b)
    with open(file_path, mode='wb') as file:
        file.write(content)


@logger.catch
async def write_to_disk(content: bytes, id_w: int):
    await asyncio.gather(
        asyncio.to_thread(blocking_io, content, id_w)
    )


@logger.catch
async def get_all_cats():

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_cat(client, i) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)


@logger.catch
def main():
    res = asyncio.run(get_all_cats())
    logger.info(len(res))


if __name__ == '__main__':
    logger.info(f"started main at {time.strftime('%X')}")
    main()
    logger.info(f"finished main at {time.strftime('%X')}")
