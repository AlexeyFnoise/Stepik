#Проверка рулетки
a = int(input())
if a < 0 or a > 36:
    print('ошибка ввода')
elif a == 0:
    print('зеленый')
else:
    if (a % 2 == 0) and (1 <= a <= 10 or 19 <= a <= 28):
        print('черный')
    elif (a % 2 == 0) and (11 <= a <= 18 or 29 <= a <= 36):
        print('красный')
    else:
        if a % 2 != 0 and (11 <= a <= 18 or 28 <= a <= 36):
            print('черный')
        elif (a % 2 != 0) and (1 <= a <= 10 or 19 <= a <= 28):
            print('красный')

# Проверка отрезков
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:                                  # отсекаем отсутствие пересечений и общей точки
    print('пустое множество')
elif a1 == b2:                                          # первое условие общей точки
    print(a1)
elif a2 == b1:                                          # второе условие общей точки
    print(a2)
else:                                                   # осталось найти только пересечение
    if a1 > a2:                                         # получаем первую точку пересечения путем отсечения лишней точки
        a2 = a1
    if b1 < b2:                                         # получаем вторую точку пересечения
        b2 = b1
    print(a2, b2)

##Начало столетия
s = int(input())
b = s % 10
g = s % 100 // 10
if b == 0 and g == 0:
    print('YES')
else:
    print('NO')

##Шахматная доска

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

# Римские цифры
a = int(input())
if a == 1:
    print('I')
elif a == 2:
    print('II')
elif a == 3:
    print('III')
elif a == 4:
    print('IV')
elif a == 5:
    print('V')
elif a == 6:
    print('VI')
elif a == 7:
    print('VII')
elif a == 8:
    print('VIII')
elif a == 9:
    print('IX')
elif a == 10:
    print('X')
else:
    print('ошибка')

##YES or NO – вот в чём вопрос ❓
a = int(input())
if a % 2 != 0:
    print('YES')
else:
    if 2 <= a <= 5:
        print('NO')
    elif 6 <= a <= 20:
        print('YES')
    elif a > 20:
        print('NO')

#Ход слона ♗🌶️
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')

#Ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")

#Ход ферзя
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

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

#   Манхэттенское расстояние ↔️
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
    print('Нет корней')         #   если D=0, то уравнение имеет один действительный корень, который вычисляется по следующей формуле:
elif d == 0:
    x = -(b / (2 * a))
    print(x)                    #   если D>0, уравнение имеет два действительных корня, которые вычисляются по следующим формулам:
elif d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))

#   Правильный многоугольник 🔶
n, a = int(input()), float(input())
from math import pi, tan
print((n * a ** 2) / (4 * tan(pi / n)))

#   Python is awesome 🐍 цик for
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

#   Квадрат числа
for i in range(int(input()) + 1):
    print('Квадрат числа', i, 'равен', i ** 2)

#   Звёздный треугольник ⭐
n = int(input())
for i in range(n):
    print('*' * n)
    n = n - 1

#   Популяция 🦠
m, p, n, = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m + (m * (p / 100))

#   Последовательность чисел 1
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)

#   Последовательность чисел 2 🌶️
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif n < m:
    for i in range(m, n - 1, -1):
        print(i)
else:
    print(n)

# Последовательность чисел 3 🌶️
m, n = int(input()), int(input())
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)

#   Последовательность чисел 4
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)

#   Таблица умножения
n = int(input())
for i in range(1, 10 + 1):
    print(n, 'x', i, '=', n * i)

#   Количество чисел
a, b = int(input()), int(input())
triger = 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == [4,9]:# Чтобы не писать два условия,
        triger += 1           # можно в списки требуемые числа отправить
print(triger)                 # if i**3 % 10 in [4, 9]:

#   Последовательность Фибоначчи 🌶️
n = int(input())
m1, m2 = 0, 1
m3 = 1
for i in range(n):
    print(m3, end = ' ')
    m3 = m1 + m2
    m1, m2 = m2, m3

#   Цикл While
#   До КОНЦА 1
count = 0
while input() not in ('стоп', 'хватит', 'достаточно'):
    count += 1
print(count)

#   Пока делимся
a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())

#   Сумма чисел
summ = 0
step = int(input())
while step >= 0:
    summ += step
    step = int(input())
print(summ)

#   Количество пятёрок 5️⃣
ball = int(input())
count = 0
while 0 < ball < 6:
    if ball == 5:
        count += 1
    ball = int(input())
print(count)

#   Ведьмаку заплатите чеканной монетой 💰
a = int(input())
count = 0
while a >= 25:
    a -= 25
    count += 1
while a >= 10:
    a -= 10
    count += 1
while a >= 5:
    a -= 5
    count += 1
while a >= 1:
    a -= 1
    count += 1
print(count)

#   Обратный порядок 1
a = int(input())
while a != 0:
    last_digit = a % 10
    print(last_digit)
    a = a // 10

#   Обратный порядок 2
new_digital = ''                        #Создаем пустую строку для обратного числа
a = int(input())
while a != 0:
    last_digit = a % 10
    new_digital += str(last_digit)      #Добавляем к нашему новому числу через преобразование в строку
    a = a // 10
print(new_digital)

#   max и min
new_digital = int(input())
mx = 0                                         #Задаем максимальное значение 0
mn = 9                                         #Задаем минимальное значение 9, так как сравнивать с 0 не вариант
while new_digital != 0:
    last_digit = new_digital % 10
    if last_digit >= mx:                        #Сравниваем последнюю цифру с ранее MAX значением
        mx = last_digit
    if last_digit < mn:                         #Сравниваем последнюю цифру с ранее MIN значанием
            mn = last_digit
    new_digital //= 10
print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)

#   Все вместе
a = int(input())
summ = 0
umnoz = 1
count = 0
temp = 0
first_digital = 0
last_digit = a % 10
while a != 0:
    temp = a % 10
    summ += temp
    umnoz *= temp
    count += 1
    a, first_digital = a // 10, a
srednee = summ / count
print(summ, count, umnoz, srednee, first_digital, first_digital + last_digit, sep='\n')

#   Вторая цифра
n = int(input())
two_digital = 0
while n:
    if len(str(n)) == 2:                #Пока длина строки не равна 2 символам, удаляем последнюю цифру
        two_digital = n % 10            #Длина строки стала 2, берем вторую цифру и записываем в переменную
    n //= 10
print(two_digital)

#   Одинаковые цифры
n = int(input())
count = 'YES'
temp = n % 10
while n:
    if temp != n % 10:
        count = 'NO'
    n //= 10
print(count)

#   Упорядоченные цифры 🌶️
n = int(input())
temp = 0
count = 'YES'
while n:
    if n % 10 >= temp:
        temp = n % 10
    else:
        count = 'NO'
    n //= 10
print(count)

n = int(input())
max_digit = - 1   # 3 ошибка
while n != 0:   # 2 ошибка
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: # 4 ошибка
            max_digit = digit # 5 ошибка
    n = n // 10   # 1 ошибка
if max_digit == - 1:
    print('NO')
else:
    print(max_digit)


#   7.6 break, continue и else
#   Наименьший делитель
n = int(input())
temp = 2
while n:
    if n % temp == 0:
        break
    else:
        temp += 1
print(temp)

# Следуй правилам 📋
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    elif 17 <= i <= 37:
        continue
    else:
        if 78 <= i <= 87:
            continue
    print(i)

count = 0
p = 0
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count, p, sep='\n')
else:
    print('NO')

mx = -10**6 # неверно задана переменная (сравнивать будет с минимальным)
s = 0
for _ in range(10):  # неверно задан диапазон (было 11), замена "i" на "_"
    x = int(input())
    if x < 0:
        s += x  # неверно задана формула (было равенство "=")
        if x > mx:  # смещен блок кода, чтобы условие работало только для x < 0
            mx = x
if s == 0:  # не был задано условие для вывода при отсутствии отрицательных чисел
    print('NO')
else:
    print(s)
    print(mx)

#   7.8 Вложенные циклы. Часть 1
#   Таблица-2
n = int(input())
for i in range (n):
    for j in range(5):
        print(i, end=' ')
    print()

#   Таблица-3
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

# Звёздный треугольник 🌟🌶️🌶️
n = int(input())
for i in range(1, n // 2 + 2, 1):
    print('*' * i)
for i in range(n // 2 , 0, -1):
    print('*' * i)

#   Численный треугольник 1
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end='')
    print()

# 12 месяцев
for n in range(1, 20):
    for k in range(1, 20):
        for m in range(1, 20):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
                break
# Ответ
#   1 4 7
#   2 1 9

#   Старинная задача 🐮🌶️
for n in range(100):
    for k in range(100):
        for m in range(100):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                print(n, k, m)

#   Гипотеза Эйлера о сумме степеней 🌶️🌶️
for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)

    #   Численный треугольник 2
n = int(input())
count = 1
for i in range(1, n + 1):
    for k in range(i):
        print(count, end=' ')
        count += 1
    print()

#   Численный треугольник 3 🌶️
n = int(input())
count = 1

# Первый цикл перебирает строки
for i in range(1, n + 1):
    # Второй вложенный цикл начинает писать от 1 до N
    for _ in range(i):
        print(count, end='')
        if count != i:
            count += 1
    # После завершения следует третий вложенный цикл, который пишет в обратном порядке
    else:
        for _ in range(i - 1):
            count -= 1
            print(count, end='')
    # В конце строки переход на новую строку и обнуление счетчика
    print()
    count = 1

#   Делители-1 🌶️
a, b = int(input()), int(input())
sum = 0
rezultat = 0
number = 0

for i in range(a, b + 1):
    for k in range(1, i + 1):
        if i % k == 0:
            sum += k
    if sum >= rezultat:
        rezultat = sum
        number = i
    sum = 0
print(number, rezultat)

#   Делители-2
n = int(input())

for i in range(1, n + 1):
    print(i, end='')
    for k in range(1, i + 1):
        if i % k == 0:
            print('+', end='')
    print()

#   Цифровой корень 🌶️
n = int(input())

while n > 9:
    summ = 0
    while n != 0:
        summ += (n % 10)
        n //= 10
    n = summ
print(n)

#   Сумма факториалов ❗
n = int(input())

facktorial = 1
summ_fuck = 0
for i in range(1, n + 1):
    facktorial *= i
    summ_fuck += facktorial
print(summ_fuck)

#   Простые числа 👌
a, b = int(input()), int(input())

for i in range(a, b + 1):
    counter = 1
    if i == 1:
        continue
    for k in range(2, i + 1):
        if i % k == 0:
            counter += 1
        if counter > 2:
            break
    else:
        print(i)

#   9.1 Индексация
#   В столбик 1
s = str(input())

for i in range(0, len(s), 2):
    print(s[i])

#   В столбик 2
s = str(input())
for i in range(-1, -(len(s)) - 1, -1):
    print(s[i])

#   Цифра 1
s = str(input())
sum_numbers = 0
for i in range(len(s)):
    sum_numbers += int(s[i])
print(sum_numbers)

#   Цифра 2
s = str(input())
digital = '0123456789'

for i in range(len(s)):
    if s[i] in digital:
        print('Цифра')
        break
else:
    print('Цифр нет')

#   Сколько раз?
s = str(input())
n, m = 0, 0

for i in s:
    if i == '+':
        n += 1
    if i == '*':
        m += 1
print('Символ + встречается', n, 'раз')
print('Символ * встречается', m, 'раз')

#   Одинаковые соседи
s, count = str(input()), 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
print(count)

#   Гласные и согласные 🔠
s, glass_count, soglass_count = str(input()), 0, 0
glass = 'ауоыиэяюе'
soglass = 'бвгджзйклмнпрстфхцчшщ'

for i in s:
    # Метод str.lower() переводит в нижний регистр ВСЮ строку
    # Лучше использовать вариант i.lower() - вызов метода для данной переменной
    if i.lower() in glass:
        glass_count += 1
    elif i.lower() in soglass:
        soglass_count += 1

print('Количество гласных букв равно',glass_count)
print('Количество согласных букв равно',soglass_count)

#   Decimal to Binary 🔟
n = int(input())
s = ''
s2 = ''

while n > 0:
    s += str(n % 2)
    n //= 2
for i in range(-1, -(len(s)) - 1, -1):
    s2 += s[i]
print(s2)

#   9.2 Срезы
#   Палиндром
s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Перебор через [] и сравнение с оригиналом
if s == s[::-1]:
    print('YES')
else:
    print('NO')

#   Делаем срезы 1
'''
На вход программе подаётся одна строка. Напишите программу, которая выводит:
1.общее количество символов в строке;
2.исходную строку, повторённую 3 раза;
3.первый символ строки;
4.первые три символа строки;
5.последние три символа строки;
6.строку в обратном порядке;
7.строку с удалённым первым и последним символами.
'''
s = input()
print(len(s), (s * 3), s[:1], s[:3], s[-3:], s[::-1], s[1:-1], sep='\n')

#   Две половинки
# Задача на замену половинок строки(четное количество символов и не четное)

s = input()

long = len(s) // 2
if len(s) % 2 == 0:
    print(s[long:] + s[:long])
else:
    print(s[long + 1:] + s[:long + 1])


#   9.3 Методы строк. Часть 1
#   Заглавные буквы 🔠
s = input()

# Проверка исходной сроки через s.title()
# s.title() - Метод title() возвращает копию строки s,
# в которой первый символ каждого слова переводится в верхний регистр.
if s == s.title():
    print('YES')
else:
    print('NO')

#   sWAP cASE 🔃
s = input()
# Метод str.swapcase() меняет у всех символов регистр на противоположный
print(s.swapcase())

#   Нижний регистр 🔽
s = input()
s1 = s.lower()
count = 0

for i in range(len(s)):
    if s[i] == s1[i] and s[i] not in '1234567890':
        count += 1
else:
    print(count)

#   9.4 Методы строк. Часть 2
#   Минутка генетики 🧬
s = input().lower()
s1 = 'агцт'
adenin = 'Аденин: ' + str(s.count(s1[0]))
guanin = 'Гуанин: ' + str(s.count(s1[1]))
citozin = 'Цитозин: ' + str(s.count(s1[2]))
Timin = 'Тимин: ' + str(s.count(s1[3]))

print(adenin, guanin, citozin, Timin, sep='\n')

#   Очень странные дела 📻
n = int(input())
count = 0

for _ in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1
else:
    print(count)

#   Количество цифр
s = input()
cnt = 0

# перебираем все элементы строки S
for i in s:
    # сравниваем элемент с цифрами от 0 до 9
    if i in '0123456789':
        cnt += 1
print(cnt)

#   .com or .ru 🌐
s = input()
# Проверка окончания строки через метод str.endswith()
if s.endswith('.ru') or s.endswith('.com'):
    print('YES')
else:
    print('NO')

#   Самый частотный символ
s = input()
mx = 0
s1 = ''
for i in s:
    if s.count(i) >= mx:
        mx = s.count(i)
        s1 = i
print(s1)

#   Первое и последнее вхождение
s = input()
const = 'f'

#   Собраем количество вхождений символа 'F'
if s.count(const) == 1:
    print(s.find(const))
elif s.count(const) > 1:
    # через str.find(), str.rfind() выводим первый и последние индексы вхождения
    print(s.find(const), s.rfind(const))
else:
    print('NO')

#   Удаление фрагмента
s, const = input(), 'h'
stemp = s[s.find(const):s.rfind(const) + 1]
print(s.replace(stemp,''))

#   9.5 Методы строк. Часть 3
#   Плохие комментарии 😈
#   Ваша задача – написать программу, которая поможет Сэму проверять комментарии
s = ''
for i in range(1, int(input())+1):
    s = input()
    if s.isspace() or s == '':
        print(i, ': COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i, ': ', s, sep='')

#   Автомобильный номер 🚘🌶️
s = input()
Flag = True
cnst = 'АВЕКМНОРСТУХ'

for i in range(len(s)):
    if i == 0 or 4 <= i <= 5:
        if s[i] in cnst:
            continue
        else:
            Flag = False
            break
    if 1 <= i <= 3 or 7 <= i <= 9:
        if s[i].isdigit():
            continue
        else:
            Flag = False
            break
    if i == 6:
        if s[i] == '_':
            continue
        else:
            Flag = False
            break
if Flag and 11 > len(s) > 8:
    print('YES')
else:
    print('NO')

#   Проверь никнейм 👩🌶️
s = input()
#print(s.startswith('@'), len(s), s.islower(), s[1:].isalnum())
if s.startswith('@') and 5 <= len(s) <= 15 and s[1:].isalnum():
    if s[1:].isdigit() or s.islower():
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')

#   9.6 Форматирование строк
year = 2010
place = '10k'
valuta = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, place, valuta)
print(s)

#   Курсы валют 💹
date = input()
euro = input()
uan = input()
print(f'На {date}: 1€ = {euro}₽, 1¥ = {uan}₽')

#   Сумма кубов 🆚 Куб суммы
a, b = int(input()), int(input())
kub = (a + b) ** 3
summ_kub = a **3 + b ** 3
print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {summ_kub}')
print(f'  Куб суммы: ({a} + {b})**3 = {kub}')

#   (Не) Активное похудение 🏃🌶️
day_n, kg = int(input()), float(input())
count = day_n * 0.2
if 100 - count >= kg:
    print('Все идет по плану')
else:
    print('Что-то пошло не так')
print(f'#{day_n} ДЕНЬ: ТЕКУЩИЙ ВЕС = {kg} кг, ЦЕЛЬ по ВЕСУ = {100 - count} кг')

#   Какая следующая буква? 🔜
n = ord(input())
#1040 - буква А 1071 - буква Я
if 1040 <= n < 1071:
    print(chr(n + 1))
elif n == 1071:
    print('Дальше букв нет')

#   Символы в диапазоне
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')

#   Простой шифр
s = input()
for i in s:
    print(ord(i), end=' ')

#   Самое тяжёлое слово 🗿
#   Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
#   Напишите программу, которая принимает 4 слова и находит среди них самое тяжёлое слово.
max_word = ''
max_summ_unicode = 0
for _ in range(4):
    s = str(input())
    summ_unicode = 0
    for i in s:
        summ_unicode += ord(i)
    if summ_unicode > max_summ_unicode:
        max_word = s
        max_summ_unicode = summ_unicode
print(max_word)

#   Стоимость ответа 💬
s = input()
oplata = 0
for i in s:
    oplata += (ord(i) * 3)
print(f"Текст сообщения: '{s}'")
print(f'Стоимость сообщения: {oplata}🐝')

#   Накручиваем стоимость ответа ⬆️🌶️
s = str(input())
symbol_en, symbol_rus = 'eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ'
oplata_old, oplata_new = 0, 0
for i in s:
    oplata_old += (ord(i) * 3)
for i in range(len(s)):
    for j in range(len(symbol_en)):
        if s[i] == symbol_en[j]:
            s = s.replace(symbol_en[j],symbol_rus[j])
for i in s:
    oplata_new += (ord(i) * 3)
print(f'Старая стоимость: {oplata_old}🐝', f'Новая стоимость: {oplata_new}🐝', sep='\n')

#   Шифр Цезаря 🌶️
step = int(input())
s = input().lower()
s1 = ''
for i in range(len(s)):
    if ord(s[i]) - step < ord('a') or ord(s[i]) > ord('z'):
        s1 += chr(ord(s[i]) - step + 26)
    else:
        s1 += chr(ord(s[i]) - step)
print(s1)
# Решение от курса +
# n = int(input())
# s = input()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# for c in s:
#     # ищем индекс текущей буквы в строке алфавита
#     ind = alphabet.index(c)
#     # находим новую букву
#     new_c = alphabet[ind - n]
#
#     print(new_c, end='')

#   Сбой в системе ⚠️🌶️🌶️

#   Строковые минимум и максимум
i = input()
min_s, max_s = i, i
while i != 'КОНЕЦ':
    min_s = min(min_s, i)
    max_s = max(max_s, i)
    i = input()

print(f'Минимальная строка ⬇️: {min_s}', f'Максимальная строка ⬆️: {max_s}', sep='\n')

#   Необычное сравнение 📊
s1, s2 = input().lower(), input().lower()
s1_new, s2_new = '', ''
for i in range(len(s1)):
    if s1[i].isalpha():
        s1_new += s1[i]
for i in range(len(s2)):
    if s2[i].isalpha():
        s2_new += s2[i]
print(s1_new, s2_new)
if s1_new == s2_new:
    print('YES')
else:
    print('NO')

#   Сортируем слова 📶
s1, s2, s3 = input(), input(), input()
temp = s1 + s2 + s3
s_max = max(s1,s2,s3)
s_min = min(s1,s2,s3)
temp = temp.replace(s_max, '')
temp = temp.replace(s_min, '')
print(s_min, temp, s_max )

#   Порядок книг 📚🌶️
n = int(input())
temp = input()
for _ in range(n-1):
    s = input()
    if temp[0:temp.find(' ')] < s[0:s.find(' ')]:
        temp = s
        continue
    elif temp[0:temp.find(' ')] == s[0:s.find(' ')]:
        if temp[temp.find('«'):] < s[s.find('«'):]:
            temp = s
            continue
        else:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')


#   Второе вхождение 2️⃣
# s = input()
#
# if s.count("f") == 0:
#     print(-2)
# elif s.count("f") == 1:
#     print(-1)
# else:
#     Использование двух методов к 1 строке!
#     res = s.replace("f", ".", 1).find("f")
#     print(res)

#   11.1 Введение в списки
#   Список букв
n = int(input())
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z']
print(s[1:n + 1])

# или решение от степика
n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)

print(list(s))



#   11.3 Методы списков. Часть 1
#   Все сразу 1 🌶️
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], sep='\n')
if (5 and 17) in numbers:
    print('YES')
else:
    print('NO')
print(numbers[1:-1])

#   Список строк
n = int(input())
#Создаем пусто список
spisok = []
for i in range(n):
    # Через метод .append добавляем по очереди строки
    spisok.append(input())
print(spisok)

#   Алфавит
spisok = []
for i in range(26):
    spisok.append(chr(ord('a') + i) * (i + 1))
print(spisok)

#   Список кубов
n = int(input())
ls = []
for i in range(1, n + 1):
    ls.append(int(input()) ** 3)
print(ls)

#   Список делителей
n = int(input())
ls = []
for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)
print(ls)

#   Суммы двух
n = int(input())
ls = []
ls2 = []
for i in range(n):
    ls.append(int(input()))
for i in range(len(ls) - 1):
    ls2.append(ls[i] + ls[i + 1])
print(ls2)

#   Удалите нечётные индексы
n, ls = int(input()), []
for i in range(n):
    ls.append(int(input()))
del ls[1::2]
print(ls)

#   k-ая буква слова 🌶️
n = int(input())
ls = []
s = ''

for i in range(n):
    ls.append(str(input()))

k = int(input())

for i in range(len(ls)):
    s = ls[i]
    if len(s) < k:
        continue
    else:
        print(s[k - 1], end='')

#   Символы всех строк
n = int(input())
ls = []
for i in range(n):
    ls.extend(input())
print(ls)

#   Значение функции
n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
print(*ls, sep='\n')
print()
for s in ls:
    print(s ** 2 + 2 * s + 1)

#   Remove outliers
n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))
mx_ls = max(ls)
mn_ls = min(ls)
for i in range(len(ls)):
    if ls[i] == mx_ls:
        del ls[i]
        break
for i in range(len(ls)):
    if ls[i] == mn_ls:
        del ls[i]
        break
print(*ls, sep='\n')

#   Без дубликатов
n = int(input())
ls = []
ls_unic = []

# Запрашиваем список данных
for _ in range(n):
    ls.append(input())
# Цикл по списку
for i in range(len(ls)):
    # Проверяем, состоит ли текущий элемент в новом списке.
    # Если нет, то добавляем. Так до конца текущего списка.
    if ls[i] not in ls_unic:
        ls_unic.append(ls[i])
print(*ls_unic, sep='\n')

#   Google search - 1
n = int(input())
ls = []
for _ in range(n):
    ls.append(input())
#   Считываем контрольную строку(слово), переводим в нижни регистр
s = input().lower()
for i in range(len(ls)):
    #   Проверяем, состоит ли наша строка S в элементе списка, который тоже переведен в нижний регистр
    if s in ls[i].lower():
        print(ls[i])
#
# #   Google search - 2 🌶️🌶️
# n = int(input())
# ls = []
# ls_input = []
# for _ in range(n):
#     ls.append(input())
# n_search = int(input())
# for _ in range(n_search):
#     ls_input.append(input().lower())
# for i in range(len(ls)):
#     for j in range(len(ls_input)):
#         if ls_input[j].lower() in ls[i].lower():
#             continue
#         else:
#             break
#     else:
#         print(ls[i])
#
# #   Negatives, Zeros and Positives
# n, tmp = int(input()), 0
# ls_zero, ls_minus, ls_plus = [], [], []
# for _ in range(n):
#     tmp = int(input())
#     if tmp == 0:
#         ls_zero.append(tmp)
#     elif tmp < 0:
#         ls_minus.append(tmp)
#     elif tmp > 0:
#         ls_plus.append(tmp)
# print(*ls_minus,*ls_zero,*ls_plus, sep='\n')


#   Построчный вывод
# ввести строку и сразу преобразовать её в список через input().split()
ls = input().split()
print(*ls, sep='\n')
#     Использование двух методов к 1 строке!
#     res = s.replace("f", ".", 1).find("f")
#     print(res)

#   11.1 Введение в списки
#   Список букв
n = int(input())
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z']
print(s[1:n + 1])

# или решение от степика
n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)

print(list(s))



#   11.3 Методы списков. Часть 1
#   Все сразу 1 🌶️
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], sep='\n')
if (5 and 17) in numbers:
    print('YES')
else:
    print('NO')
print(numbers[1:-1])

#   Список строк
n = int(input())
#Создаем пусто список
spisok = []
for i in range(n):
    # Через метод .append добавляем по очереди строки
    spisok.append(input())
print(spisok)

#   Алфавит
spisok = []
for i in range(26):
    spisok.append(chr(ord('a') + i) * (i + 1))
print(spisok)

#   Список кубов
n = int(input())
ls = []
for i in range(1, n + 1):
    ls.append(int(input()) ** 3)
print(ls)

#   Список делителей
n = int(input())
ls = []
for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)
print(ls)

#   Суммы двух
n = int(input())
ls = []
ls2 = []
for i in range(n):
    ls.append(int(input()))
for i in range(len(ls) - 1):
    ls2.append(ls[i] + ls[i + 1])
print(ls2)

#   Удалите нечётные индексы
n, ls = int(input()), []
for i in range(n):
    ls.append(int(input()))
del ls[1::2]
print(ls)

#   k-ая буква слова 🌶️
n = int(input())
ls = []
s = ''

for i in range(n):
    ls.append(str(input()))

k = int(input())

for i in range(len(ls)):
    s = ls[i]
    if len(s) < k:
        continue
    else:
        print(s[k - 1], end='')

#   Символы всех строк
n = int(input())
ls = []
for i in range(n):
    ls.extend(input())
print(ls)

#   Значение функции
n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
print(*ls, sep='\n')
print()
for s in ls:
    print(s ** 2 + 2 * s + 1)

#   Remove outliers
n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))
mx_ls = max(ls)
mn_ls = min(ls)
for i in range(len(ls)):
    if ls[i] == mx_ls:
        del ls[i]
        break
for i in range(len(ls)):
    if ls[i] == mn_ls:
        del ls[i]
        break
print(*ls, sep='\n')

#   Без дубликатов
n = int(input())
ls = []
ls_unic = []

# Запрашиваем список данных
for _ in range(n):
    ls.append(input())
# Цикл по списку
for i in range(len(ls)):
    # Проверяем, состоит ли текущий элемент в новом списке.
    # Если нет, то добавляем. Так до конца текущего списка.
    if ls[i] not in ls_unic:
        ls_unic.append(ls[i])
print(*ls_unic, sep='\n')

#   Google search - 1
n = int(input())
ls = []
for _ in range(n):
    ls.append(input())
#   Считываем контрольную строку(слово), переводим в нижни регистр
s = input().lower()
for i in range(len(ls)):
    #   Проверяем, состоит ли наша строка S в элементе списка, который тоже переведен в нижний регистр
    if s in ls[i].lower():
        print(ls[i])

#   Google search - 2 🌶️🌶️
n = int(input())
ls = []
ls_input = []
for _ in range(n):
    ls.append(input())
n_search = int(input())
for _ in range(n_search):
    ls_input.append(input().lower())
for i in range(len(ls)):
    for j in range(len(ls_input)):
        if ls_input[j].lower() in ls[i].lower():
            continue
        else:
            break
    else:
        print(ls[i])

#   Negatives, Zeros and Positives
n, tmp = int(input()), 0
ls_zero, ls_minus, ls_plus = [], [], []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        ls_zero.append(tmp)
    elif tmp < 0:
        ls_minus.append(tmp)
    elif tmp > 0:
        ls_plus.append(tmp)
print(*ls_minus,*ls_zero,*ls_plus, sep='\n')

#   Windows OS
'''
Примечание. В Python символ \ обычно используется для создания специальных символьных последовательностей,
которые представляют собой управляющие символы или экранированные последовательности. Например,
\n представляет символ новой строки, \t представляет символ табуляции и так далее. Однако если символ \ 
используется как часть строки, его следует экранировать, то есть использовать два обратных слэша \\
'''
s = input().split('\\')
print(*s, sep='\n')

#Количество совпадающих пар
s = input().split()
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            count += 1
else:
    print(count)

#11.6 Методы списков. Часть 2

#Переставить min и max
ls = input().split()
for i in range(len(ls)):
    ls[i] = int(ls[i])
ls_min = ls.index(min(ls))
ls_max = ls.index(max(ls))
ls[ls_max], ls[ls_min] = ls[ls_min], ls[ls_max]
print(*ls)

#Количество артиклей
s = input().lower()
ls = s.split()
count = ls.count('a') + ls.count('an') + ls.count('the')
print(f'Общее количество артиклей: {count}')

#Взлом Братства Стали 🌶️
num_str = input()
num_str = int(num_str[1:])
s = ''
ls = []
#rstrip() метод строки, удаляет все пробелы в конце
for i in range(num_str):
    ls.append(str(input()))
    s = ls[i]
    if '#' in ls[i]:
        s = s[:s.find('#')]
    s = s.rstrip()
    ls[i] = s
print(*ls, sep='\n')

#Сортировка чисел
ls = input().split()
for i in range(len(ls)):
    ls[i] = int(ls[i])
ls.sort()
print(*ls)
ls.sort(reverse=True)
print(*ls)

#11.7 Списочные выражения#11.7 Списочные выражения
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

#Перебираем список через for, i принимает значение элемента списка(в виде строки).
#Далее обычный срез строки с 1 элемента строки до конца
new_keywords = [i[1:] for i in keywords]

print(new_keywords)

#Используя списочное выражение, дополните приведённый ниже код так,
# чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).
palindromes = [str(i) for i in range(100, 1001)]
palindromes = [int(i) for i in palindromes if i == i[::-1]]
print(palindromes)

#Списочное выражение 1
palindromes = [i ** 2 for i in range(1, int(input()) + 1)]
print(*palindromes, sep='\n')

#Списочное выражение 2
ls = [int(el) ** 3 for el in input().split()]
print(*ls)

#В одну строку 1
print(*[i for i in input().split()], sep='\n')

#В одну строку 2
#Работаем со строкой. Проверяем элемент строки на циферность через isgidit.
#Если True, то собираем в список. Далее выводим список без пробелов через \n
print(*[i for i in input() if i.isdigit()], sep='')

#В одну строку 3
# Собираем список из строки, при этом собираем квадраты четных чисел
ls = [int(i) ** 2 for i in input().split() if int(i) % 2 == 0]
#Шерстим созданный список
for i in ls:
    #Проверяем равна ли после последняя цифра 4, если нет, то выводим
    if int(i) % 10 != 4:
        print(i, end=' ')

#Отсортируйте список по возрастанию, реализовав алгоритм сортировки выбором.
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
a_new = []
while len(a):
    a_new.append(min(a))
    a.pop(a.index(min(a)))
print(a_new)


#13.1 Функции без параметров
def draw_box():
    for i in range(14):
        if i != 0 and i != 13:
            print('*' + ' ' * 8 + '*')
        else:
            print('*' * 10)
draw_box()

#Звёздный треугольник 1
def draw_box():
    for i in range(1, 11):
        print(i * '*')

draw_box()

#Звёздный треугольник
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, (base // 2) + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

#ФИО
# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

#Сумма цифр
# объявление функции
def print_digit_sum(num):
    ls = [int(i) for i in str(num)]
    print(sum(ls))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

#13.4 Функции с возвратом значения. Часть 1
#Количество дней

def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28

n = int(input())
print(get_days(n))

#Делители 1
# объявление функции
def get_factors(num):
    lis = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            lis.append(int(i))
    lis.append(int(num))
    return lis

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


#Делители 2
def number_of_factors(num):
    count = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
    count += 1
    return count

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))

## Или !!!
def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())
# вызываем функцию
print(number_of_factors(n))

#Найти всех
#Функция возвращает все вхождения заданного символа строки.
def find_all(text, symbol):
    lis = [int(i) for i in range(len(text)) if text[i] == symbol]
    return lis

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

#Merge lists 1
def merge(lis1, lis2):
    lis3 = lis1 + lis2
    lis3.sort()
    return lis3

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

#Merge lists 2
def quick_merge(lis):
    lis_main = []
    for i in range(len(lis)):
        for j in lis[i]:
            lis_main.append(int(j))
    lis_main.sort()
    return lis_main

n = int(input())
lis_old = [input().split() for _ in range(n)]
print(*quick_merge(lis_old))

#Is the Triangle Valid?
def is_valid_triangle(n1, n2, n3):
    if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
        return True
    else:
        return False
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

#Is the Number Prime? 🌶️ Является ли число простым
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

#Next Prime 🌶️🌶️
# объявление функции
def get_next_prime(num):
    #Берем следующее число от заданого
    nm = num + 1
    while not is_prime(nm):
        nm += 1
    return nm
# считываем данные
n = int(input())
# вызываем функцию
print(get_next_prime(n))

#Good password 🌶️
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    if password.lower() == password:
        return False
    if password.upper() == password:
        return False
    for i in password:
        if i in '0123456789':
            return True
    else:
            return False
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

#Ровно в одном 1️⃣
# объявление функции
def is_one_away(word1, word2):
    cont = 0
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cont += 1
    else:
        if cont != 1:
            return False
        else:
            return True

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

#Палиндром 🌶️
# объявление функции
def is_palindrome(text):
    #Собираем список всех букв строки, делая их в нижнем регистре
    les = [i.lower() for i in text if i.isalpha()]
    #Собираем новую строку из списка
    s = ''.join(les)
    #Сравниваем строку с перевернутой версией себя же
    if s == s[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

#Правильная скобочная последовательность 🌶️
# объявление функции
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return text == ''

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

#Змеиный регистр 🐍
# объявление функции
def convert_to_python_case(text):
    s = ''
    for i in range(len(text)):
        if i == 0:
            s += text[i].lower()
            continue
        if text[i].isupper() and i > 0:
            s += '_' + text[i].lower()
            continue
        if text[i].islower() or text[i].isdigit():
            s += text[i]
    return s

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

#13.6 Функции с возвратом значения. Часть 3
# Середина отрезка
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

#Площадь и длина 📏
# объявление функции
def get_circle(radius):
   from math import pi
   radius = float(radius)
   c = 2 * pi * radius
   s = pi * radius ** 2
   return c, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)