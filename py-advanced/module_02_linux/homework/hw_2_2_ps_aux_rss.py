"""
С помощью команды ps можно посмотреть список процессов, запущенных текущим пользователем.
Особенно эта команда выразительна с флагами
    $ ps aux
Запустите эту команду, output сохраните в файл, например вот так
$ ps aux > output_file.txt
В этом файле вы найдёте информацию обо всех процессах, запущенных в системе.
В частности там есть информация о потребляемой процессами памяти - это столбец RSS .
Напишите в функцию python, которая будет на вход принимать путь до файла с output
и на выход возвращать суммарный объём потребляемой памяти в человеко-читаемом формате.
Это означает, что ответ надо будет перевести в байты, килобайты, мегабайты и тд.

Для перевода можете воспользоваться функцией _sizeof_fmt
"""
import os


def _sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def get_summary_rss(ps_output_file_path: str) -> str:
    """put your code here"""
    used_memory = 0
    with open(ps_output_file_path, 'r') as system_file:
        for _ in system_file:
            temp_line = system_file.readline().split()
            used_memory += int(temp_line[5])
        return f'All used memory {_sizeof_fmt(used_memory)}'


if __name__ == "__main__":
    print(get_summary_rss("/home/nostrik/PycharmProjects/python_advanced/output_file.txt"))
