# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for _ in range(30)]
print(f'Входной массив: {a}')

pos_max_negative = -1
for i, item in enumerate(a):
    if item < 0 and pos_max_negative == -1:
        pos_max_negative = i
    elif item < 0 and item > a[pos_max_negative]:
        pos_max_negative = i
    i += 1

print(f'Максимально отрицательный элемент в массиве: {a[pos_max_negative]}, его позиция: {pos_max_negative + 1}')
