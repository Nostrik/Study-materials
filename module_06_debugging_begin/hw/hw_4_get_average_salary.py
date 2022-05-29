"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
from typing import List
import random


def get_average_salary_corrected(salaries: List[int]) -> float:
    min_val = min(salaries)
    max_val = max(salaries)
    truncated_list = [i for i in salaries if min_val < i < max_val]
    return sum(truncated_list) / len(truncated_list)


if __name__ == '__main__':
    list_salary = [random.randint(100, 1000) for i in range(30)]
    print(get_average_salary_corrected(list_salary))
