# Матрица

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print(matrix)   # Не красиво выводит))

# Так красиво
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

#Посчитать сумму строк и столбцов матрицы

# 1. Создадим массив для подсчета суммы по столбцам
sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item

        print(f'{item:>5}', end='')

    print(f'   | {sum_line}')

print('-' * (len(matrix) * 5))

for s in sum_column:
    print(f'{s:>5}', end='')

# 2. Обмен значений главной и побочной диаганоли
# квадратной матрицы

size = 5

matrix2 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

for line in matrix2:
    for item in line:
        print(f'{item:>4}', end='')
    print()

for i in range(size):
    for j in range(size):
        if i == j:

            spam = matrix2[i][j]
            matrix2[i][j] = matrix2[i][size - 1 - j]
            matrix2[i][size - 1 - j] = spam

print('*' * 30)

for line in matrix2:
    for item in line:
        print(f'{item:>4}', end='')
    print()
