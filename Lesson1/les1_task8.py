# Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого)

a = int(input('Введите целое число a:'))
b = int(input('Введите целое число b:'))
c = int(input('Введите целое число c:'))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее: {b}')
else:
    print(f'Среднее: {c}')