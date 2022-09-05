import functools
from typing import Union

Number = Union[int, float, complex]


def find_insert_position(array: list[Number], number: Number) -> int:
    position = 0
    if len(array) < 1:
        raise ValueError
    while True:
        array.insert(position, number)
        sort_list = array.copy()
        sort_list.sort()
        if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, array, sort_list)):
            break
        array.pop(position)
        position += 1
    return position


if __name__ == '__main__':
    A: list[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    insert_position: int = find_insert_position(A, x)
    assert insert_position == 5

    A: list[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    A.insert(insert_position, x)
    assert A == sorted(A)
