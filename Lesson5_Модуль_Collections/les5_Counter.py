from collections import Counter

a = Counter()
b = Counter('abrakadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')
# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})

print(b['z'])
# 0

b['z'] = 0
print(b)
# Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1, 'z': 0})

print(list(b.elements()))
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'k', 'd']

print(b.most_common(2))
# [('a', 5), ('b', 2)]

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=2)
g.subtract(f)
print(g)
# Counter({'b': 4, 'a': 3, 'd': -2, 'c': -5})

print(set(g))
print(dict(g))
g.clear()
print(g)
# {'b', 'd', 'a', 'c'}
# {'a': 3, 'b': 4, 'c': -5, 'd': -2}
# Counter()

x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)
# Counter({'a': 4, 'b': 3})
# Counter({'a': 2})
# Counter({'a': 1, 'b': 1})
# Counter({'a': 3, 'b': 2})

z = Counter(a=2, b=-4)
print(+z)
print(-z)
# Counter({'a': 2})
# Counter({'b': 4})
