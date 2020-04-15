from collections import defaultdict

a = defaultdict()
print(a)
# defaultdict(None, {})

s = 'sdjfjnvbsdznbginedgfbrnsa'
b = defaultdict(int)
for i in s:
    b[i] += 1

print(b)
# defaultdict(<class 'int'>, {'s': 3, 'd': 3, 'j': 2, 'f': 2, 'n': 4, 'v': 1,
# 'b': 3, 'z': 1, 'g': 2, 'i': 1, 'e': 1, 'r': 1, 'a': 1})

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)

print(c)
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})

# можно сделать чтобы остались только уникальные значения
list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)

print(d)
# defaultdict(<class 'set'>, {'cat': {1, 2}, 'dog': {1, 5}, 'mouse': {1}})

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
# defaultdict(<function <lambda> at 0x00000000028B3400>, {'rex': 'dog', 'tomas': 'cat'})
# dog
# unknown
