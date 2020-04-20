# Написать программу сложения двух 16-ных чесел
# При этом каждое число представляется как массив

from collections import Counter
from collections import deque

num_1 = list(input('Введите первое 16-ное число:').upper())
num_2 = list(input('Введите второе 16-ное число:').upper())


dic_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert_dec(value):
    """Преобразует список в Counter {разряд: 10-ное значение}"""
    num_upd = [dic_hex[i] for i in value]
    dic = dict(zip(range(len(num_upd)), reversed(num_upd)))
    count_num = Counter(dic)
    return count_num


def convert_hex(value):
    """Преобразует в массив из 16-ных значений"""
    inv_dic_hex = {value: key for key, value in dic_hex.items()}
    result = deque()
    surplus = 0
    for i in value:
        if (value[i] + surplus) in inv_dic_hex:
            result.appendleft(inv_dic_hex[value[i] + surplus])
            surplus = 0
        else:
            result.appendleft(inv_dic_hex[(value[i] + surplus) % 16])
            surplus = (value[i] + surplus) // 16
    if surplus:
        result.appendleft(surplus)
    return result


result_sum = convert_dec(num_1) + convert_dec(num_2)
print(f'Сумма этих чисел: {list(convert_hex(result_sum))}')
