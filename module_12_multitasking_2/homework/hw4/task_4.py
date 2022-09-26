import logging
import threading
import requests
import time


temp_log_file = "temp_log.txt"
logging.basicConfig(
    filename=temp_log_file,
    level=logging.INFO,
    format="<%(threadName)s> - <%(message)s>"
)
logger = logging.getLogger(__name__)
date_url = "https://showcase.api.linx.twenty57.net/UnixTime/fromunix"
list_urls = [date_url] * 10
buffer_list = []
sem = threading.BoundedSemaphore()
threading_list = []


def clean_temp_file():
    """
    Clearing the log buffer file
    """
    file = open(temp_log_file, 'w')
    file.close()


def work_func():
    """
    The function returns the current time using unix time stamp, converting it to human readable format.
    Writes a message log within 20 seconds.
    """
    url = date_url
    log_data_list = []
    cnt_requests = 0
    while cnt_requests != 5:
        from_time = str(time.time())[:10]
        request = requests.get(url, params={'timestamp': from_time})
        log_data_list.append(request.text[1:20])
        time.sleep(1)
        cnt_requests += 1
    for i_log in log_data_list:
        logger.info(i_log)


clean_temp_file()
for i_thread in range(2):
    thread = threading.Thread(target=work_func)
    thread.start()
    print(f"Thread number {i_thread} started")
    time.sleep(0.5)
