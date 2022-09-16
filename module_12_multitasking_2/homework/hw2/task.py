import threading
import subprocess
from pprint import pprint


def process_count(username: str) -> int:
    # к-во процессов, запущенных из-под текущего пользователя
    proc = subprocess.Popen(
        ["ps", "U", "maksim"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    res = proc.communicate()
    for line in res:
        print(line.decode("utf-8"))
    pass


def total_memory_usage(root_pid: int) -> int:
    # суммарное потребление памяти древа процессов
    pass


if __name__ == "__main__":
    process_count("test_name")
    # print("I'm here")
