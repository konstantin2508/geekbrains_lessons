# Рекурсия
# Даны 2 числа: необходимо вывести все числа от A до B,
# в порядке возрастания (A<B) или убывания (A>B)

def func(a, b):
    if a == b:
        return f'{a}'
    elif a > b:
        return f'{a}, {func(a - 1, b)}'
    elif a < b:
        return f'{a}, {func(a + 1, b)}'

print(func(3, 25))
print(func(20, 2))