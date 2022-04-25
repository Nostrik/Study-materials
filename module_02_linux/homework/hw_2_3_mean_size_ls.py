"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    """Put your code here"""
    result = 0
    file_count = 0
    try:
        with open(ls_output_path, 'r') as out_file:
            for _ in out_file:
                temp_line = out_file.readline().split()
                result += int(temp_line[4])
                file_count += 1
            return round(result / file_count, 2)
    except FileNotFoundError as ex:
        return ex


if __name__ == "__main__":
    print(get_mean_size("/home/nostrik/PycharmProjects/python_advanced/module_02_linux/homework/output_ls.txt"))
