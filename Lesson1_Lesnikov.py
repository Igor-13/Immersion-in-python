""" Урок №1 """
# Задание 1/1. Нарисовать в консоли ёлку спросив у пользователя количество
# рядов.
rows = int(input('Enter the number of rows: '))
spase = ' '
stars = '*'
while rows > 0:
    print((spase * (rows - 1)) + stars + (spase * (rows - 1)), end='\n')
    stars += '**'
    rows -= 1
# Задание 1/2. Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
# школьной тетрадке.

print(" " * 20, 'ТАБЛИЦА УМНОЖЕНИЯ')
multiplier_1 = 2
multiplier_2 = 2
result = 0
while result < 60:
    result = multiplier_1 * multiplier_2
    if multiplier_1 > 5:
        print(end='\n')
        multiplier_1 = 2
        multiplier_2 += 1
    else:
        print(f'{multiplier_1} x {multiplier_2} = {result}', end="\t")
        multiplier_1 += 1

print(end='\n')
multiplier_1 = 6
multiplier_2 = 2

while result < 100:
    result = multiplier_1 * multiplier_2
    if multiplier_1 > 9:
        print(end='\n')
        multiplier_1 = 6
        multiplier_2 += 1
    else:
        print(f'{multiplier_1} x {multiplier_2} = {result}', end="\t")
        multiplier_1 += 1

# Задание №2 .Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b,
# c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
# существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a = int(input('Enter the length of the side "a" of the triangle "abc": '))
b = int(input('Enter the length of the side "b" of the triangle "abc": '))
c = int(input('Enter the length of the side "c" of the triangle "abc": '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b and a != c or a == c and a != b or b == c and b != a:
        print(f'a triangle with sides a = {a}, b = {b} and c = {c} is isosceles')
    elif a == b == c:
        print(f'a triangle with sides a = {a}, b = {b} and c = {c} is equilateral')
    else:
        print(f'a triangle with sides a = {a}, b = {b} and c = {c} is versatile')
else:
    print('it is impossible to construct a triangle from these segments since one of the sides is greater than the '
          'sum of the other two')

# Задание №3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте
# правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте
# ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Enter a positive number: '))
idx = num
divider = 1
counter = 0
if 0 < num < 100000:
    while idx > 0:
        if num % divider == 0:
            counter += 1
            divider += 1
            idx -= 1
        else:
            divider += 1
            idx -= 1
    if counter == 2:
        print(f'number {num} - simple')
    else:
        print(f'number {num} - composite ')
else:
    print('enter the correct number')
