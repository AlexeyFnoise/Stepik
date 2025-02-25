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

