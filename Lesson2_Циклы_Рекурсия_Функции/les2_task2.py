# Посчитать четные и нечетные цифры введенного натурального числа

num = int(input('Введите натуральное число:'))

even_num = 0
odd_num = 0

while num > 0:
    if (num % 10) % 2 == 0:
        even_num += 1
        num //= 10
    else:
        odd_num += 1
        num //= 10

print(f'В введенном Вами числе: четных цифр - {even_num}, нечетных цифр - {odd_num}')

