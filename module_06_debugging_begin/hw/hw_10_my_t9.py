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
from typing import List
import re
from pprint import pprint

# btn_2 = ['a', 'b', 'c']
# btn_3 = ['d', 'e', 'f']
# btn_4 = ['g', 'h', 'i']
# btn_5 = ['j', 'k', 'l']
# btn_6 = ['m', 'n', 'o']
# btn_7 = ['p', 'q', 'r', 's']
# btn_8 = ['t', 'u', 'v']
# btn_9 = ['w', 'x', 'y', 'z']
# dictionary = {
#     '2': ('a', 'b', 'c'),
#     '3': ('d', 'e', 'f'),
#     '4': ('g', 'h', 'i'),
#     '5': ('j', 'k', 'l'),
#     '6': ('m', 'n', 'o'),
#     '7': ('p', 'q', 'r', 's'),
#     '8': ('t', 'u', 'v'),
#     '9': ('w', 'x', 'y', 'z')
# }


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
    res = ''
    temp_list = []
    temp_list_2 = []
    for sym_line in input_numbers:
        for s in dictionary[sym_line]:
            result += s
    print(result)
    print(len(input_numbers))
    try:
        with open('../../words', 'r') as words_file:
            for line in words_file:
                if len(line) == len(input_numbers) + 1 and line.startswith(dictionary[input_numbers[0]]):
                    temp_list.append(line.rstrip())
    except Exception as er:
        pass
    cnt_let = len(input_numbers) + 1
    while cnt_let != 0:
        pass
        cnt_let -= 1
    print('res is ', res)
    pprint(temp_list)


if __name__ == '__main__':
    my_t9('43556')
