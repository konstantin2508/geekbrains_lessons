# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random


def replacementArrayElements(array: list) -> list:
    """Выводит массив с поменяными местами мин. и макс. элементами входного массива"""
    num_max = array[0]
    pos_max = 0
    num_min = array[0]
    pos_min = 0

    for i, item in enumerate(array):
        if num_max < item:
            num_max = item
            pos_max = i
        elif num_min > item:
            num_min = item
            pos_min = i

    array[pos_min], array[pos_max] = array[pos_max], array[pos_min]

    return array


a = [random.randint(0, 100) for _ in range(10)]
print(f'Входной массив: {a}')
print(f'Выходной массив: {replacementArrayElements(a)}')
