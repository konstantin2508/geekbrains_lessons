from _collections import OrderedDict

# сортировка по ключу
a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda  x: x[0]))
print(new_a)
# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])

# сортировка по значению
b = {'cat': 5, 'dog': 2, 'mouse': 4}
new_b = OrderedDict(sorted(b.items(), key=lambda  x: x[1]))
print(new_b)
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])

# изменение порядка в отсортированном словаре
new_b.move_to_end('mouse')
print(new_b)
# OrderedDict([('dog', 2), ('cat', 5), ('mouse', 4)])

new_b.move_to_end('mouse', last=False)
print(new_b)
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])

new_b.popitem()
print(new_b)
# OrderedDict([('mouse', 4), ('dog', 2)])

new_b.popitem(last=False)
print(new_b)
# OrderedDict([('dog', 2)])

new_b['cow'] = 1
print(new_b)
# OrderedDict([('dog', 2), ('cow', 1)])     добавляется всегда в конец

new_b['dog'] = 8
print(new_b)
# OrderedDict([('dog', 8), ('cow', 1)])     значение поменялось, а сортировка нет

# Сортировка по длине ключа
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)
# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])

# Вывод в обратном порядке
for key in reversed(new_c):
    print(key, new_c[key])
# mouse 4
# dog 2
# cat 5
