from collections import deque

a = deque()
b = deque('abcdef')
c =deque([1, 2, 3, 4, 5 ])
print(a, b, c, sep='\n')
# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])

a = deque()
b = deque('abcdef', maxlen=3)
c =deque([1, 2, 3, 4, 5 ], maxlen=4)
print(a, b, c, sep='\n')
# deque([])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([2, 3, 4, 5], maxlen=4)

c.clear()
# deque([], maxlen=4)

# Добавление элементов в очередь
d = deque([i for i in range(5)])
d.append(5)
d.appendleft(6)
print(d)
# deque([6, 0, 1, 2, 3, 4, 5])

d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)
# deque([12, 11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9])

d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
# deque([6, 0, 1, 2, 3, 4, 5], maxlen=7)
d.extend([7, 8, 9])
print(d)
#deque([2, 3, 4, 5, 7, 8, 9], maxlen=7)
d.extendleft([10, 11, 12])
print(d)
# deque([12, 11, 10, 2, 3, 4, 5], maxlen=7)

# Забирание элементов из очереди
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')
# deque([1, 2, 3], maxlen=7)
# 4
# 0

g = deque([i for i in range(5)], maxlen=7)
print(g)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)
# deque([0, 1, 2, 3, 4], maxlen=7)
# 1
# 3
# deque([0, 1, 6, 2, 3, 4], maxlen=7)

g.reverse()
print(g)
# deque([4, 3, 2, 6, 1, 0], maxlen=7)
g.rotate(3)
print(g)
# deque([6, 1, 0, 4, 3, 2], maxlen=7)


# Пример разделения массива на положительные и отрицательные элементы
import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:
    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)

print(deq)
# [-26, 75, -89, 53, 94, -84, -4, 91, 28, 93]
# deque([-4, -84, -89, -26, 75, 53, 94, 91, 28, 93])
