# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
import random


def evenArrayElements(array: list) -> list:
    """Выводит массив с индексами четных элементов входного массива"""
    lst_even_ind = []
    for i, item in enumerate(array):
        if item % 2 == 0:
            lst_even_ind.append(i)
    return lst_even_ind


a = [random.randint(0, 100) for _ in range(10)]
print(f'Входной массив: {a}')
print(f'Выходной массив: {evenArrayElements(a)}')
