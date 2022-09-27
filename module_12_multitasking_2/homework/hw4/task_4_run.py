import subprocess
from pprint import pprint


def sort_temp_file():
    file = open("temp_log.txt", 'r')
    for line in file:
        tmp_list.append(line.rstrip())
    # sorted(tmp_list, key=lambda d: d[14:33])


if __name__ == "__main__":
    tmp_list = []
    print('task_4 start..')
    proc = subprocess.Popen(['python', 'task_4.py'])
    proc.wait()
    print("You can start sort temp file")
    sort_temp_file()
    pprint(tmp_list)
    # pprint(sorted(tmp_list, key=lambda d: d[14:33]))
