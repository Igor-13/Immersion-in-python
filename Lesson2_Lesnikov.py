""" Урок №2 """
import fractions
# Задание 1/1. Напишите программу банкомат.
balance = 0
CONST = 50
COMMISSION = 0.015
MIN_COMMISSION = 30
MAX_COMMISSION = 600
number_of_operations = 0
PERCENTAGES = 0.03
AMOUNT_THRESHOLD = 5_000_000
WEALTH_TAX = 0.1
while exit != 'Exit':
    action = str(input('What action do you want to perform? To withdraw money, click -> take_off. To deposit money to '
                       'the account, click -> replenish. To exit, press Exit: '))

    if action == 'replenish':
        replenish = int(input('Enter the amount to top up your account: '))
        if balance > AMOUNT_THRESHOLD or replenish + balance >= AMOUNT_THRESHOLD:
            replenish = replenish - (replenish * WEALTH_TAX)

        if replenish % CONST != 0:
            print('Please deposit a multiple of 50!')
            print(f'Your balance is equal to: {balance} y.e.')
        else:
            if replenish * COMMISSION < MIN_COMMISSION:
                replenish = replenish + 30
                balance = balance + replenish
            elif replenish * COMMISSION > MAX_COMMISSION:
                replenish = replenish + 600
                balance = balance + replenish
            else:
                balance = balance + (replenish + (replenish * COMMISSION))

            number_of_operations += 1
            if number_of_operations > 3:
                balance = balance + (replenish * PERCENTAGES)
                number_of_operations = 0
            print(f'Your balance is equal to: {balance} y.e.')
    elif action == 'take_off':
        take_off =  int(input('enter the withdrawal amount: '))
        if balance > AMOUNT_THRESHOLD:
            take_off = take_off + (take_off * WEALTH_TAX)

        if take_off % CONST != 0:
            print('Please deposit a multiple of 50!')
            print(f'Your balance is equal to: {balance} y.e.')
        else:
            if take_off * COMMISSION < MIN_COMMISSION:
                take_off = take_off + 30
                balance = balance - take_off
            elif take_off * COMMISSION > MAX_COMMISSION:
                take_off = take_off + 600
                balance = balance - take_off
            else:
                balance = balance - (take_off + (take_off * COMMISSION))
            if balance < 0:
                balance = balance + take_off
                print('Insufficient funds to withdraw')
                number_of_operations -= 1
            number_of_operations += 1
            if number_of_operations > 3:
                balance = balance + (take_off * PERCENTAGES)
                number_of_operations = 0
            print(f'Your balance is equal to: {balance} y.e.')
    elif action == 'Exit':
        print(f'Your balance is equal to: {balance} y.e.')
        break

# Задание 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.

num = int(input('Enter num: '))
SYSTEM = 16
num_16 = ''

x = num
while x > 0:
    n = x % SYSTEM
    if n < 10:
        num_16 = str(n) + num_16
    else:
        if n == 10:
            num_16 = 'A' + num_16
        elif n == 11:
            num_16 = 'B' + num_16
        elif n == 12:
            num_16 = 'C' + num_16
        elif n == 13:
            num_16 = 'D' + num_16
        elif n == 14:
            num_16 = 'E' + num_16
        elif n == 15:
            num_16 = 'F' + num_16
        elif n == 16:
            num_16 = 'G' + num_16

    x //= SYSTEM


print(num_16)
print(hex(num))


# Задание 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

a = str(input('fraction 1: '))
b = str(input('fraction 2: '))
fract_1 = a.split('/')
fract_2 = b.split('/')

fract_1[0], fract_1[1] = int(fract_1[0]), int(fract_1[1])
fract_2[0], fract_2[1] = int(fract_2[0]), int(fract_2[1])

a_fr = fractions.Fraction(fract_1[0], fract_1[1])
b_fr = fractions.Fraction(fract_2[0], fract_2[1])
c_fr = a_fr + b_fr
print(f'fractions sum: {c_fr}')

if fract_1[1] > fract_2[1]:
    denom_max = fract_1[1]
else:
    denom_max = fract_2[1]

while(True):
    if (denom_max % fract_1[1] == 0) and (denom_max % fract_2[1] == 0):
        common_denom = denom_max
        break
    else:
        denom_max += 1

fract_1[0] = fract_1[0] * (common_denom / fract_1[1])
fract_2[0] = fract_2[0] * (common_denom / fract_2[1])


print(f'sum: {int(fract_1[0]) + int(fract_2[0])}/{common_denom}')



multfract_1 = a.split('/')
multfract_2 = b.split('/')

multfract_1[0], multfract_1[1] = int(multfract_1[0]), int(multfract_1[1])
multfract_2[0], multfract_2[1] = int(multfract_2[0]), int(multfract_2[1])

a_mfr = fractions.Fraction(multfract_1[0], multfract_1[1])
b_mfr = fractions.Fraction(multfract_2[0], multfract_2[1])
c_mfr = a_mfr * b_mfr
print(f'fractions multiplication: {c_mfr}')


denominator_1 = multfract_1[1]
denominator_2 = multfract_2[1]

while(True):
    if multfract_1[0] % denominator_2 == 0 and multfract_2[1] %  denominator_2 == 0:
        multfract_1[0] = int(multfract_1[0] / denominator_2)
        multfract_2[1] = int(multfract_2[1] / denominator_2)
        break
    else:
        denominator_2 -= 1


while(True):
    if multfract_2[0] % denominator_1 == 0 and multfract_1[1] %  denominator_1 == 0:
        multfract_2[0] = int(multfract_2[0] / denominator_1)
        multfract_1[1] = int(multfract_1[1] / denominator_1)
        break
    else:
        denominator_1 -= 1


print(f'multiplication: {multfract_1[0] * multfract_2[0]}/{multfract_1[1] * multfract_2[1]}')