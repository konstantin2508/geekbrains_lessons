# Пользователь вводит данные о кол-ве предприятий, их названия и прибыль за 4 квартала
# Надо определить среднюю прибыль за год и вывести наименования у кого выше и ниже среднего

from collections import defaultdict


n = int(input('Введите кол-во предприятий:'))
firm_lst = []
profit_year = 0

for i in range(n):
    name_firm = str(input(f'Введите название предприятия №{i + 1}:'))
    for k in range(4):
        profit = float(input(f'Введите прибыль по предприятию "{name_firm}" за квартал {k + 1}:'))
        firm_lst.append([name_firm, profit])
        profit_year += profit

profit_average = profit_year / n

firm_dict = defaultdict(list)
for k, v in firm_lst:
    firm_dict[k].append(v)

firm_good = []
firm_bad = []

for key, value in firm_dict.items():
    if sum(value) >= profit_average:
        firm_good.append(key)
    else:
        firm_bad.append(key)
print('-------------------------\n')
print(f'Среднегодовая прибыль состовляет: {profit_average}')
print(f'Фирмы, чья среднегодовая прибыль выше среднего: {firm_good}')
print(f'Фирмы, чья среднегодовая прибыль ниже среднего: {firm_bad}')
