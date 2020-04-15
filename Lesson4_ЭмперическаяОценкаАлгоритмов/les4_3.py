# Поиск чисел Фибоначчи с помощью рекурсии
# мемоизация в словарь и в список
import  cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

# test_fib(fib_dict)

# fib_dict(10)
# 1000 loops, best of 3: 5.01 usec per loop

# cProfile.run('fib_dict(10)')
#  19/1    0.000    0.000    0.000    0.000 les4_3.py:14(_fib_dict)

cProfile.run('fib_dict(25)')
# 49/1    0.000    0.000    0.000    0.000 les4_3.py:14(_fib_dict)


# def fib_list(n):
#     fib_l = [None] * 1000
#     fib_l[:2] = [0, 1]
#
#     def _fib_list(n):
#         if fib_l[n] in None:
#             fib_l[n] = _fib_list(n -1) + _fib_list(n - 2)
#         return fib_l[n]
#
#     return _fib_list(n)

# test_fib(fib_list)

# cProfile.run('fib_list(10)')