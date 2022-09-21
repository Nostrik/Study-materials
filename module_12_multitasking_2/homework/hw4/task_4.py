import logging
import requests
import time


logging.basicConfig(

    level=logging.INFO,
    format="<%(threadName)s> - <%(message)s>"
)
logger = logging.getLogger(__name__)
date_url = "https://showcase.api.linx.twenty57.net/UnixTime/fromunix"


def get_time_from_api_linux() -> str:
    """
    The function returns the current time using unix time stamp, converting it to human readable format.
    """
    from_time = str(time.time())[:10]
    request = requests.get(date_url, params={'timestamp': from_time})
    return request.text


if __name__ == "__main__":
    print(get_time_from_api_linux())
    logger.info(get_time_from_api_linux())
