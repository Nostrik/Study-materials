import threading
import psutil
import subprocess
from pprint import pprint


def process_count(username: str) -> int:
    proc_dict = {proc.pid: proc.name() for proc in psutil.process_iter() if proc.username() == username}
    return int(len(proc_dict))


def total_memory_usage(root_pid: int) -> int:
    # суммарное потребление памяти древа процессов
    process = psutil.Process(root_pid)
    return int(process.memory_info().vms)


if __name__ == "__main__":
    # print(process_count("maksim"))
    # print("I'm here")
    # total_memory_usage(1555)
    pass
