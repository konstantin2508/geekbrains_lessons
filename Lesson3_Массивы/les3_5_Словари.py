# Задача с ассоциативным массивом

k = int(input('Введите количеств предприятий'))
enterprise = {}

for i in range(1, k + 1):
    name = input('Введите название предприятия: ')
    enterprise[name] = [float(input('План :')), float(input('Факт: '))]

    enterprise[name].append(enterprise[name][1] / enterprise[name][0])

print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%)')
for key, value in enterprise.items():
    if value[1] > 10 and value[2] < 1:
        print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')
