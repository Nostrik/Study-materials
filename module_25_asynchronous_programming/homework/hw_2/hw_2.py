import shutil
from pathlib import Path
from loguru import logger
import time
import requests

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = Path(__file__).parent / 'cats3'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


@logger.catch
def get_cat():
    response = requests.get(URL, stream=True)
    file_path = "{}/{}.png".format(OUT_PATH, 2)
    if response.status_code == 200:
        return response
    else:
        logger.error('Something was wrong')


@logger.catch
def write_to_disk():
    file_name = 'image.jpg'
    file_path = "{}/{}.png".format(OUT_PATH, 2)
    response = requests.get(URL, stream=True)
    with open(file_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


@logger.catch
def main():
    res = get_cat()
    logger.debug(res)


if __name__ == '__main__':
    logger.info(f"started main at {time.strftime('%X')}")
    # main()
    logger.info(f"finished main at {time.strftime('%X')}")
