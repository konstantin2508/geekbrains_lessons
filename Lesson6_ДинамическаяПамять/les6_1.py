import sys

a = 42
print(bin(a))
print(oct(a))
print(hex(a))
# 0b101010
# 0o52
# 0x2a

b = 0b100110
print(b)
# 38

c = int('2cd50', base=24)
print(c)
# 837048

z = int('z', base=36)
print(z)
# 35

print(ord('d'))     # кодировка ASCII до 255 бит
# 100

print(ord('л'))     # utf-8
# 1083

# Размеры занимаемые в памяти объектами
a = 5
b = 125.54
c = 'Hello'

print(sys.getsizeof(a))     # 14 байт
print(sys.getsizeof(b))     # 16
print(sys.getsizeof(c))     # 30

lst = [i for i in range(10)]
print(sys.getsizeof(lst))       # 100 байт

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

show_size(a)
show_size(b)
show_size(c)
# type = < class 'int'>, size= 14, object= 5
# type = < class 'float'>, size= 16, object= 125.54
# type = < class 'str'>, size= 30, object= Hello

show_size(lst)
 # type= <class 'list'>, size= 100, object= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	#  type= <class 'int'>, size= 12, object= 0
	#  type= <class 'int'>, size= 14, object= 1
	#  type= <class 'int'>, size= 14, object= 2
	#  type= <class 'int'>, size= 14, object= 3
	#  type= <class 'int'>, size= 14, object= 4
	#  type= <class 'int'>, size= 14, object= 5
	#  type= <class 'int'>, size= 14, object= 6
	#  type= <class 'int'>, size= 14, object= 7
	#  type= <class 'int'>, size= 14, object= 8
	#  type= <class 'int'>, size= 14, object= 9

show_size(tuple(lst))
 # type= <class 'tuple'>, size= 68, object= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	#  type= <class 'int'>, size= 12, object= 0
	#  type= <class 'int'>, size= 14, object= 1
	#  type= <class 'int'>, size= 14, object= 2
	#  type= <class 'int'>, size= 14, object= 3
	#  type= <class 'int'>, size= 14, object= 4
	#  type= <class 'int'>, size= 14, object= 5
	#  type= <class 'int'>, size= 14, object= 6
	#  type= <class 'int'>, size= 14, object= 7
	#  type= <class 'int'>, size= 14, object= 8
	#  type= <class 'int'>, size= 14, object= 9

show_size(set(lst))
 # type= <class 'set'>, size= 372, object= {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	#  type= <class 'int'>, size= 12, object= 0
	#  type= <class 'int'>, size= 14, object= 1
	#  type= <class 'int'>, size= 14, object= 2
	#  type= <class 'int'>, size= 14, object= 3
	#  type= <class 'int'>, size= 14, object= 4
	#  type= <class 'int'>, size= 14, object= 5
	#  type= <class 'int'>, size= 14, object= 6
	#  type= <class 'int'>, size= 14, object= 7
	#  type= <class 'int'>, size= 14, object= 8
	#  type= <class 'int'>, size= 14, object= 9

d = {str(i): i for i in range(10)}
show_size(d)
 # type= <class 'dict'>, size= 204, object= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	#  type= <class 'tuple'>, size= 36, object= ('0', 0)
	# 	 type= <class 'str'>, size= 26, object= 0
	# 	 type= <class 'int'>, size= 12, object= 0
	#  type= <class 'tuple'>, size= 36, object= ('1', 1)
	# 	 type= <class 'str'>, size= 26, object= 1
	# 	 type= <class 'int'>, size= 14, object= 1
	#  type= <class 'tuple'>, size= 36, object= ('2', 2)
	# 	 type= <class 'str'>, size= 26, object= 2
	# 	 type= <class 'int'>, size= 14, object= 2
	#  type= <class 'tuple'>, size= 36, object= ('3', 3)
	# 	 type= <class 'str'>, size= 26, object= 3
	# 	 type= <class 'int'>, size= 14, object= 3
	#  type= <class 'tuple'>, size= 36, object= ('4', 4)
	# 	 type= <class 'str'>, size= 26, object= 4
	# 	 type= <class 'int'>, size= 14, object= 4
	#  type= <class 'tuple'>, size= 36, object= ('5', 5)
	# 	 type= <class 'str'>, size= 26, object= 5
	# 	 type= <class 'int'>, size= 14, object= 5
	#  type= <class 'tuple'>, size= 36, object= ('6', 6)
	# 	 type= <class 'str'>, size= 26, object= 6
	# 	 type= <class 'int'>, size= 14, object= 6
	#  type= <class 'tuple'>, size= 36, object= ('7', 7)
	# 	 type= <class 'str'>, size= 26, object= 7
	# 	 type= <class 'int'>, size= 14, object= 7
	#  type= <class 'tuple'>, size= 36, object= ('8', 8)
	# 	 type= <class 'str'>, size= 26, object= 8
	# 	 type= <class 'int'>, size= 14, object= 8
	#  type= <class 'tuple'>, size= 36, object= ('9', 9)
	# 	 type= <class 'str'>, size= 26, object= 9
	# 	 type= <class 'int'>, size= 14, object= 9