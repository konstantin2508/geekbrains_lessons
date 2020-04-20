# Написать программу сложения и умножения двух 16-ных чесел
# При этом каждое число представляется как массив

num_1 = ['A', '2']
num_2 = ['C', '4', 'F']

# сумма из примера ['C','F','1'}
# произведение ['7', 'C', '9', 'F', 'E']

dic_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

num_1_upd = [dic_hex[i] for i in num_1]
num_2_upd = [dic_hex[i] for i in num_2]
# print(num_1_upd, num_2_upd)
# создаем словарь из списка
dic_1 = dict(zip(range(len(num_1_upd)), reversed(num_1_upd)))
dic_2 = dict(zip(range(len(num_2_upd)), reversed(num_2_upd)))
print(dic_1, dic_2)