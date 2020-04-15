# Цикл с предусловием
# Вывод числа в обратном порядке
num = int(input("Введите число:"))
while num > 0:
    print(num % 10)
    num //= 10


# Цикл с постусловием
while True:
    num = int(input("Введите любое число от 0 до 100:"))
    if 0 <= num <= 100:
        break
print("Вывод вне тела цикла")

# Цикл с параметром
i = 0
while i <= 10:
    print(i)
    i += 1

for i in range(11):
    print(i)
