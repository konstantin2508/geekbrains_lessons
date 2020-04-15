# Определить, какое число в массиве встречается чаще всего

import random


def mostCommonValue(array: list) -> int:
    """Выводит какое число в массиве встречается чаще всего"""

    d = dict.fromkeys(array, 0)
    for item in array:
        d[item] += 1

    duplicate_key = None
    duplicate_value = 0
    for key, value in d.items():
        if value > duplicate_value:
            duplicate_value = value
            duplicate_key = key

    return duplicate_key


a = [random.randint(0, 10) for _ in range(20)]
print(f'Входной массив: {a}')
print(f'Чаще всего в массиве встречается число: {mostCommonValue(a)}')
