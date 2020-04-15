# Измерение времени работы программы с помощью timeit

# import timeit
#
# x = 2 + 2
# print(timeit.timeit('x = 2 + 2'))
# print(timeit.timeit('x = sum(range(10))'))

# Измерение времени работы программы с помощью cProfile

import cProfile


def get_len(array):
    return len(array)

def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s

def main():
    lst = [i for i in range(1000000)]
    a = get_len(lst)
    b = get_sum(lst)

cProfile.run('main()')
