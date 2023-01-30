import shutil
from pathlib import Path
from loguru import logger
import time
import requests
from multiprocessing import Process

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = Path(__file__).parent / 'cats4'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


@logger.catch
def download_and_save_img(num):
    response = requests.get(URL, stream=True)
    if response.status_code == 200:
        logger.debug(response.status_code)
        file_path = "{}/{}.png".format(OUT_PATH, num)
        logger.debug(file_path)
        with open(file_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    else:
        logger.error('Something was happening')


@logger.catch
def main():
    processes = []
    for i in range(CATS_WE_WANT):
        t = Process(target=download_and_save_img, args=(i, ))
        processes.append(t)
        t.start()
    for t in processes:
        t.join()


if __name__ == '__main__':
    logger.info(f"started main at {time.strftime('%X')}")
    main()
    logger.info(f"finished main at {time.strftime('%X')}")
