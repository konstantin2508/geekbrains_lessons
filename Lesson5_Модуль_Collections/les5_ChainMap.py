from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c':6}
d_2 = {'a': 10, 'b': 20, 'd':40}

d_map = ChainMap(d_1, d_2)
print(d_map)
# ChainMap({'a': 2, 'b': 4, 'c': 6}, {'a': 10, 'b': 20, 'd': 40})

d_2['a'] = 100
print(d_map)
# ChainMap({'a': 2, 'b': 4, 'c': 6}, {'a': 100, 'b': 20, 'd': 40})

print(d_map['a'])
print(d_map['d'])
# 2
# 40

# метод добавляет словарь
x = d_map.new_child()
print(x)
# ChainMap({}, {'a': 2, 'b': 4, 'c': 6}, {'a': 100, 'b': 20, 'd': 40})

# Обращение к конкретному словарю по индексу
print(x.maps[0])
print(x.maps[-1])

print(x.parents)


y = d_map.new_child()
print(y)
print(y['a'])
# ChainMap({}, {'a': 2, 'b': 4, 'c': 6}, {'a': 100, 'b': 20, 'd': 40})
# 2
y['a'] = 1
print(y)
# ChainMap({'a': 1}, {'a': 2, 'b': 4, 'c': 6}, {'a': 100, 'b': 20, 'd': 40})

print(list(y))
print(list(y.values()))
# ['a', 'd', 'c', 'b']
# [1, 40, 6, 4]
