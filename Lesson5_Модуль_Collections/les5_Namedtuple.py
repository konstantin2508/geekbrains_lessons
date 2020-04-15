from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])

class Person:

    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strenght')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'health', 'mana', 'strenght']
New_Person_1 = namedtuple('New_Person_1', prop, rename=True)
hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)


Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=3, y=4)
print(p1)

# Строим точку на основе списка
t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

# Метод преобразует Namedtuple в Orderdict
d2 = p2._asdict()
print(d2)
# OrderedDict([('x', 5), ('y', 10), ('z', 15)])

# Изменить именованый кортеж
p3 = p2._replace(x=6)
print(p3)
# Point(x=6, y=10, z=15)

# Просмотр всех полей
print(p3._fields)
# ('x', 'y', 'z')

# Добавление значения по умолчанию для Python 3.7
# New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
# p4 = New_Point(5)
# print(p4)
# print(p4._fields_defaults)

# Способ создания именованного кортежа из словаря
New_Point = namedtuple('New_Point', 'x, y, z')
dct = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Point(**dct)
print(p5)
# New_Point(x=10, y=20, z=30)
