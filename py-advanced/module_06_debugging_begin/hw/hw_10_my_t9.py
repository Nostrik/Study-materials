"""
Представьте что мы решаем задачу следующего вида.
У нас есть кнопочный телефон (например, знаменитая Нокиа 3310) и мы хотим,
чтобы пользователь мог проще отправлять SMS.

Мы реализуем свой собственный клавиатурный помощник.
Каждой цифре телефона соответствует набор букв:
2 - a ,b, c
3 - d, e, f
4 - g, h, i
5 - j, k, l
6 - m, n, o
7 - p, q, r, s
8 - t, u, v
9 - w, x, y, z

Пользователь нажимает на клавиши, например,  22736368
    после чего на экране печатается basement

Напишите функцию-помощник my_t9, которая на вход принимает цифровую
строку и возвращает list из слов английского языка,
которые можно получить из этой цифровой строки.

В качестве словаря английского языка можете использовать
содержимое файла /usr/share/dict/words

Ваше решение должно работать с алгоритмической сложностью O(N),
где N -- длина цифровой строки.
"""
import copy
from typing import List


def my_t9(input_numbers: str) -> List[str]:
    dictionary = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
    }
    result = ''
    result_list = []
    temp_list = []
    for sym_line in input_numbers:
        for s in dictionary[sym_line]:
            result += s
    try:
        with open('../../words', 'r') as words_file:
            for line in words_file:
                if len(line) == len(input_numbers) + 1 and line.startswith(dictionary[input_numbers[0]]):
                    result_list.append(line.rstrip())
    except Exception as er:
        pass

    cnt = 1
    while cnt != len(input_numbers):
        for elem in result_list:
            if elem[cnt] in dictionary[input_numbers[cnt]]:
                temp_list.append(elem)
        result_list.clear()
        result_list = copy.deepcopy(temp_list)
        temp_list.clear()
        cnt += 1

    return result_list


if __name__ == '__main__':
    print(my_t9('43556'))  # hello
    print(my_t9('3428466279'))  # dictionary
    assert my_t9('43556') == ['hello']
    assert my_t9('3428466279') == ['dictionary']
