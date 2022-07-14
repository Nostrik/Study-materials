"""
В своей работе программист должен часто уметь решать рутинные задачи.

Хорошим примером такой задачи является вычисление суммарного размера директории.

Пожалуйста реализуйте функцию, которая на вход принимает путь до папки
    в виде стрки или объекта Path
и возвращает суммарный объём директории в байтах.

В случае, если на вход функции передаётся несуществующий путь или НЕ директория,
    функция должна выкинуть исключение ValueError с красивым описание ошибки
"""

import os
from pathlib import Path
from typing import Union


def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
    size_cnt = 0
    path_items = os.listdir(directory_path)
    for item in path_items:
        print(os.path.isfile(os.path.join(directory_path, item)))
        new_path_temp = os.path.join(directory_path, item)
        if os.path.isfile(new_path_temp):
            size_cnt += os.path.getsize(new_path_temp)
    return size_cnt


if __name__ == "__main__":
    test_path = '/home/nostrik/Documents'
    print(calculate_directory_size(test_path))
