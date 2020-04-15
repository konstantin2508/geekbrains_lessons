# 1. Разложить положительные и отрицательные числа
#  по разным массивам

import random

# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
#
# arr_below = []
# arr_lager = []
#
# for item in array:
#
#     if item > 0:
#         arr_lager.append(item)
#     elif item < 0:
#         arr_below.append(item)
#
# print(arr_below)
# print(arr_lager)
#
# # Этот способ хуже, т.к. осуществляется за 2 прохода
# arr_below1 = [item for item in array if item < 0]
# arr_lager1 = [item for item in array if item > 0]
# print(arr_below1)
# print(arr_lager1)

# 2. Вставка элемента в произвольное место массива

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки:'))
pos = int(input('На какую позицию вставить число:'))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1

# array.insert(pos, num)  # этот метод реализован по алгоритму выше

# array_new = array[:pos] + [num] + array[pos:]   # этот способ хуже тратиться в 2 раза больше памяти

array[pos] = num
print(array)
