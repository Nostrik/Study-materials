import subprocess
import time


def run_flask_server():
    proc = subprocess.Popen(['python', '../materials/prev_hw_review/hw_3_1.py'])
    print(proc.pid)
    time.sleep(5)
    proc_2 = subprocess.run(['kill ', f'%{proc.pid}'], shell=True)


if __name__ == '__main__':
    run_flask_server()
