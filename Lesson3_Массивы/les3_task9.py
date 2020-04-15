# Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random

# Задаем размер матрицы и строим матрицу
size_matrix = [6, 5]
matrix = [[random.randint(1, 10) for _ in range(size_matrix[0])] for _ in range(size_matrix[1])]
print('Входная матрица:')

# Создадим массив для минимальных элементов столбцов матрицы
min_column = matrix[0]

for line in matrix:
    for i, item in enumerate(line):
        if item < min_column[i]:
            min_column[i] = item
        print(f'{item:>5}', end='')
    print()
print('-' * (len(matrix) * 7))

# Вычислим максимальный элемент в массиве и красиво отобразим
print('Минимальные элементы столбцов:')
max_min_column = min_column[0]
for i in min_column:
    print(f'{i:>5}', end='')
    if i > max_min_column:
        max_min_column = i

print()
print('-' * (len(matrix) * 7))
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min_column}')
