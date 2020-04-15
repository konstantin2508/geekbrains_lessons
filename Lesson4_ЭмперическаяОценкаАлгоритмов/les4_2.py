# Поиск чисел Фибоначчи с помощью рекурсии
import  cProfile
import  functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# test_fib(fib)
# python -m timeit -n 1000 -s "import les4_2" "les4_2.fib(10)"
#"les4_2.fib(10)"
# 1000 loops, best of 3: 29.3 usec per loop

#"les4_2.fib(15)"
# 1000 loops, best of 3: 350 usec per loop

#"les4_2.fib(20)"
# 1000 loops, best of 3: 3.74 msec per loop

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
# 177/1    0.000    0.000    0.000    0.000 les4_2.py:12(fib)

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 les4_2.py:12(fib)

cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.006 seconds
# 21891/1    0.006    0.000    0.006    0.006 les4_2.py:12(fib)
