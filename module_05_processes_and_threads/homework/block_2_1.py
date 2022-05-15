import signal
import subprocess
import time
import os
import re
from pprint import pprint


def get_pid_from_lsof():
    proc = subprocess.Popen([f'lsof -i :5000'], shell=True, stdout=subprocess.PIPE)
    data = (proc.communicate())[0].decode('utf-8')
    # print(data)
    pid_temp = data.split('\n')[1]
    # print(pid_temp)
    pid = pid_temp.split(' ')[1]
    # print(pid)
    pass
    return pid


def run_flask_server():
    print('* Running flask server')
    time.sleep(1)
    process = subprocess.run(['python3', '../materials/prev_hw_review/hw_3_1.py'],

                             )
    print(process.stdout)
    if process.returncode == 0:
        return True
    else:
        return False


def check_running_process_on_port():
    proc = run_flask_server()
    print(proc)
    # if proc.returncode is None:
    #     print('* Running port is busy')
    #     time.sleep(2)
    #     pid_lsof = get_pid_from_lsof()
    #     print('* Cleaning port')
    #     os.kill(int(pid_lsof), signal.SIGTERM)
    #     time.sleep(1)
    #     check_running_process_on_port()
    # else:
    #     print(proc.stdout)


if __name__ == '__main__':
    run_flask_server()
