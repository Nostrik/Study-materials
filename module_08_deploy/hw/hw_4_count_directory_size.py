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
size_cnt = 0


def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
    global size_cnt
    for i_elem in os.listdir(directory_path):
        path = os.path.join(directory_path, i_elem)
        if os.path.isdir(path):
            calculate_directory_size(path)
        else:
            size_cnt += os.path.getsize(path)
    return f'directory_size is {size_cnt}'


if __name__ == "__main__":
    test_path = '/home/nostrik/Downloads'
    pathlib_obj = Path('home', 'nostrik', 'Downloads')
    print(calculate_directory_size(test_path))
    print(calculate_directory_size(pathlib_obj))
