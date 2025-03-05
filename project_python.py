# ##Проверка рулетки
# a = int(input())
# if a < 0 or a > 36:
#     print('ошибка ввода')
# elif a == 0:
#     print('зеленый')
# else:
#     if (a % 2 == 0) and (1 <= a <= 10 or 19 <= a <= 28):
#         print('черный')
#     elif (a % 2 == 0) and (11 <= a <= 18 or 29 <= a <= 36):
#         print('красный')
#     else:
#         if a % 2 != 0 and (11 <= a <= 18 or 28 <= a <= 36):
#             print('черный')
#         elif (a % 2 != 0) and (1 <= a <= 10 or 19 <= a <= 28):
#             print('красный')
#
# ## Проверка отрезков
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if a2 > b1 or a1 > b2:  # отсекаем отсутствие пересечений и общей точки
#     print('пустое множество')
# elif a1 == b2:  # первое условие общей точки
#     print(a1)
# elif a2 == b1:  # второе условие общей точки
#     print(a2)
# else:  # осталось найти только пересечение
#     if a1 > a2:  # получаем первую точку пересечения путем отсечения лишней точки
#         a2 = a1
#     if b1 < b2:  # получаем вторую точку пересечения
#         b2 = b1
#     print(a2, b2)
#
# ##Начало столетия
# s = int(input())
# b = s % 10
# g = s % 100 // 10
# if b == 0 and g == 0:
#     print('YES')
# else:
#     print('NO')
#
# ##Шахматная доска
#
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')
#
# # Римские цифры
# a = int(input())
# if a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print('ошибка')
#
# ##YES or NO – вот в чём вопрос ❓
# a = int(input())
# if a % 2 != 0:
#     print('YES')
# else:
#     if 2 <= a <= 5:
#         print('NO')
#     elif 6 <= a <= 20:
#         print('YES')
#     elif a > 20:
#         print('NO')
#
# #Ход слона ♗🌶️
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
#
# if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
#     print('YES')
# else:
#     print('NO')
#
# #Ход коня
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
#     print("YES")
# else:
#     print("NO")
#
# #Ход ферзя
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
#

#Площадь треугольника
a, b = float(input()), float(input())
s = (a * b) / 2
print(s)

#Две старушки 👵
a = float(input())
b = float(input())
c = float(input())
print(a/(c+b))

#Обратное число
a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    print(a ** (-1))

#451 градус по Фаренгейту 🌡️
tf = float(input())
tc = (5 * (tf - 32)) / 9
print(tc)

#Dog age 🐶
a = float(input())
if a <= 2:
    print(a * 10.5)
else:
    a = 21 + (a -2) *4
    print(a)

#Дробная часть

a = float(input())
print(a - int(a))

#Наибольшее и наименьшее
a1, a2, a3, a4, a5 = int(input()), int(input()), int(input()), int(input()), int(input())

print('Наименьшее число =', min(a1, a2, a3, a4, a5))
print('Наибольшее число =', max(a1, a2, a3, a4, a5))

#Сортировка трёх 🔀🌶️
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

#Интересное число 🤔
x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print("Число интересное")
else:
    print("Число неинтересное")

#Абсолютная сумма

a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())

a1, a2, a3, a4, a5 = abs(a1), abs(a2), abs(a3), abs(a4), abs(a5)
print(a1 + a2 + a3 + a4 + a5)

#Манхэттенское расстояние ↔️

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

print(abs(p1 - q1) + abs(p2 - q2))

#Длина строки
a = str(input())
print('Футбольная команда ' + a + 'имеет длину ' + str(len(a)) + ' символов')

#Три города 🏙️
s1, s2, s3 = input(), input(), input()
m = min(len(s1), len(s2), len(s3))
m2 = max(len(s1), len(s2), len(s3))
if m == len(s1):
    m = s1
elif m == len(s2):
    m = s2
else:
    m = s3
if m2 == len(s1):
    m2 = s1
elif m2 == len(s2):
    m2 = s2
else:
    m2 = s3
print(m, m2, sep='\n')

#Арифметические строки 🌶️

a, b, c = len(input()), len(input()), len(input())
max1 = max(a, b, c)
min1 = min(a, b, c)
sr = a + b + c - max1 - min1
if max1 - sr == sr - min1:
    print('YES')
else:
    print('NO')

#Цвет настроения синий 🟦
s = input()
if 'синий' in s:
    print('YES')
else:
    print('NO')

d = input()
if '@' in d and '.' in d:
    print('YES')
else:
    print('NO')

#Площадь и длина
r = float(input())
from math import pi

s = pi * r ** 2
c = 2 * pi * r
print(s, c, sep='\n')

#Средние значения
a, b = float(input()), float(input())
from math import sqrt

a1 = (a + b) / 2
g1 = sqrt(a * b)
gar = (2 * a * b) / (a + b)
kvadr = sqrt((a ** 2 + b ** 2) / 2)
print(a1, g1, gar, kvadr, sep='\n')

#Тригонометрическое выражение
import math
x = float(input())
x = math.radians(x) #Тригонометрические функции принимают аргумент в радианах.
# Чтобы перевести градусы в радианы, воспользуйтесь формулой
tr = math.sin(x) + math.cos(x) + math.tan(x) ** 2
print(tr)

#Пол и потолок
x = float(input())
from math import floor, ceil
print(floor(x) + ceil(x))

# Квадратное уравнение 🌶️🌶️
a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c
#   Количество действительных корней квадратного уравнения определяется дискриминантном,
#   который вычисляется по следующей формуле D=b**2-4ac
#   если D<0, то уравнение не имеет действительных корней
if d < 0:
    print('Нет корней')
#   если D=0, то уравнение имеет один действительный корень, который вычисляется по следующей формуле:
elif d == 0:
    x = -(b / (2 * a))
    print(x)
#   если D>0, уравнение имеет два действительных корня, которые вычисляются по следующим формулам:
elif d > 0:
    x1 = (-(b) - d ** 0.5) / (2 * a)
    x2 = (-(b) + d ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))

#   Правильный многоугольник 🔶
n, a = int(input()), float(input())
from math import pi, tan
print((n * a ** 2) / (4 * tan(pi / n)))

#   Python is awesome 🐍 цик for

#   for название_переменной_цикла in range(количество_повторений):
#       блок кода
for i in range(10):
    print('Python is awesome!')

#   Последовательность символов
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

#   Повторяй за мной 1
s = input()
r = int(input())
for i in range(r):
    print(s)

#   Звёздный прямоугольник ⭐
for i in range(int(input())):
    print("*******************")

#   Повторяй за мной 2
a = input()
for i in range(10):
    print(i, a)