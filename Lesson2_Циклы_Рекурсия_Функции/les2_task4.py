# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите кол-во элементов:'))
k = 1
s = 0

if n > 0:
    for i in range(n):
        s += k
        k = -(1 / 2) * k
    print(f'Сумма элементов ряда: {s}')
else:
    print('Неправильный ввод')
