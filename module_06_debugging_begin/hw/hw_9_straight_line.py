"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""
from typing import List, Tuple


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    x_1 = coordinates[0][0]
    y_1 = coordinates[0][1]
    x_2 = coordinates[1][0]
    y_2 = coordinates[1][1]
    x_3 = coordinates[2][0]
    y_3 = coordinates[2][1]
    if (y_3 - y_1) / (y_2 - y_1) == (x_3 - x_1) / (x_2 - x_1):
        return True
    else:
        return False


if __name__ == '__main__':
    assert check_is_straight_line([(1, 1), (2, 2), (3, 3)]) is True
    assert check_is_straight_line([(1, 3), (3, 2), (1, 2)]) is False
