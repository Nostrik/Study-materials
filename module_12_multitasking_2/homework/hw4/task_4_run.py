import subprocess
from pprint import pprint
from task_4 import stamp_to_human


def sort_temp_file():
    """
    Buffer file sort function
    """
    file = open("temp_log.txt", 'r')
    for line in file:
        tmp_list.append(line.rstrip())
    # sorted(tmp_list, key=lambda d: d[14:33])


def final(material: list) -> list:
    """
    Creating a sorted list with a human readable date and time
    """
    result_list = []
    try:
        for element in material:
            human_date_time = stamp_to_human(element[14:24])
            result_list.append(element[:25] + human_date_time)
    except Exception as er:
        print('Some problem with request;', er)
    return result_list


if __name__ == "__main__":
    tmp_list = []
    print('task_4 start..')
    proc = subprocess.Popen(['python', 'task_4.py'])
    proc.wait()
    print("You can start sort temp file")
    sort_temp_file()
    pprint(tmp_list)
    sort_temp_list = sorted(tmp_list, key=lambda d: d[14:24])
    pprint(sort_temp_list)
    print("Start date/time conversion...")
    print(final(sort_temp_list))
