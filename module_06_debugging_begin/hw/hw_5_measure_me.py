"""
Обычно мы пишем логи с какой-то целью.
Иногда для дебага, иногда для своевременного реагирования на ошибки.
Однако с логами можно делать очень-очень много чего.

Например, ведь верно, что каждая строка лога содержит в себе метку времени.
Таким образом, правильно организовав логирование,
    мы можем вести статистику -- какая функция сколько времени выполняется.
Программа, которую вы видите в файле hw_5_measure_me.py пишет логи в stdout.
Внутри неё есть функция measure_me,
в начале и конце которой пишется "Enter measure_me" и "Leave measure_me".
Из-за конфигурации - в начале каждой строки с логами указано текущее время.
Запустите эту программу, соберите логи и посчитайте
среднее время выполнения функции measure_me.
"""
import logging
import random
import pprint
from typing import List

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                            f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


if __name__ == "__main__":
    logging.basicConfig(
        level="DEBUG",
        filename='hw_5_measure_me.log',
        format="%(asctime)s - %(funcName)s - %(message)s"
    )
    for it in range(15):
        data_line = get_data_line(10 ** 2)
        measure_me(data_line)

    print('Анализ логов...')
    average_list = []
    start_val = ''
    stop_val = ''
    summ = 0
    with open('hw_5_measure_me.log', 'r') as log_file:
        for line in log_file:
            list_line = line.split('-')
            if list_line[4] == ' Enter measure_me\n':
                start_val = list_line[2]
            elif list_line[4] == ' Leave measure_me\n':
                stop_val = list_line[2]
            float_stop_val = stop_val[9:15].replace(',', '.')
            float_start_val = start_val[9:15].replace(',', '.')
            if float_stop_val != float_start_val and float_start_val != '' \
                    and float_stop_val != '' and float_stop_val > float_start_val:
                average_list.append(round(float(float_stop_val) - float(float_start_val), 3))
    for i in average_list:
        summ += i
    result = summ / len(average_list)
    print('Среднее время выполнения функции measure_me', round(result, 3), 'msec')
