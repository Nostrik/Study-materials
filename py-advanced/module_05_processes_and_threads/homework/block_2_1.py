import signal
import subprocess
import time
import os


def use_lsof_and_kill_proc():
    proc = subprocess.Popen([f'lsof -i :5000'], shell=True, stdout=subprocess.PIPE)
    data_temp = proc.communicate()
    if data_temp != (b'', None):
        print('* Port is busy, cleaning..')
        data = data_temp[0].decode('utf-8')
        pid_temp = data.split('\n')[1]
        pid = pid_temp.split(' ')[1]
        os.kill(int(pid), signal.SIGTERM)
        time.sleep(1)
        print('* Port is free..')
        return True
    return None


def run_flask_server(port_number: str):
    print('* Checking port')
    result_check = use_lsof_and_kill_proc()
    if result_check is True:
        print('* Running flask server')
        process = subprocess.run(['python3', '../materials/prev_hw_review/hw_3_1.py', port_number])


if __name__ == '__main__':
    port = 5000
    run_flask_server(str(port))
