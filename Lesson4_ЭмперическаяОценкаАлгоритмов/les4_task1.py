# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import timeit
import cProfile
import functools


# функция для проведения теста
def test_sum_elements(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i} OK')

# 1 - вариант кода с использованием цикла и его анализ
def sum_elements(n: int) -> float:
    """Выводит сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…"""
    item = 1
    summa = 0
    for i in range(n):
        summa += item
        item /= -2
    return summa


# test_sum_elements(sum_elements)

# тестирование с помощью timeit показывает что алгоритм имеет ЛИНЕЙНУЮ СЛОЖНОСТЬ!
# "les4_task1.sum_elements(10)" ---> 1000 loops, best of 3: 1.63 usec per loop
# "les4_task1.sum_elements(500)" ---> 1000 loops, best of 3: 53.2 usec per loop
# "les4_task1.sum_elements(1000)" ---> 1000 loops, best of 3: 110 usec per loop

# cProfile.run('sum_elements(1000000)')
# 4 function calls in 0.121 seconds
#  1    0.121    0.121    0.121    0.121 les4_task1.py:15(sum_elements)



#----------------------------------------------------------------
# 2 - вариант кода с использованием рекурсии и его анализ
def sum_elements(n: int) -> float:
    """Выводит сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…"""
    if n == 1:
        return n
    return 1 + sum_elements(n - 1)/-2

# test_sum_elements(sum_elements)

# тестирование с помощью timeit
# "les4_task1.sum_elements(10)" ---> 1000 loops, best of 3: 2.41 usec per loop
# "les4_task1.sum_elements(500)" ---> 1000 loops, best of 3: 157 usec per loop
# "les4_task1.sum_elements(1000)" --->  maximum recursion depth exceeded in comparison

#cProfile.run('sum_elements(500)')
# 503 function calls (4 primitive calls) in 0.000 seconds
# 500/1    0.000    0.000    0.000    0.000 les4_task1.py:38(sum_elements)



# -----------------------------------------------------------------
# 3 - вариант кода рекурсия с мемоизацией и его анализ
@functools.lru_cache()
def sum_elements(n: int) -> float:
    """Выводит сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…"""
    if n == 1:
        return n
    return 1 + sum_elements(n - 1)/-2

# test_sum_elements(sum_elements)

# тестирование с помощью timeit
# "les4_task1.sum_elements(10)" ---> 1000 loops, best of 3: 0.134 usec per loop
# "les4_task1.sum_elements(100)" ---> 1000 loops, best of 3: 0.136 usec per loop
# "les4_task1.sum_elements(300)" --->  1000 loops, best of 3: 0.136 usec per loop
# "les4_task1.sum_elements(500)" --->  maximum recursion depth exceeded

# cProfile.run('sum_elements(300)')
# 303 function calls (4 primitive calls) in 0.000 seconds
# 300/1    0.000    0.000    0.000    0.000 les4_task1.py:56(sum_elements)