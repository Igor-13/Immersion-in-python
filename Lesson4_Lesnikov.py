""" Урок №4 """

# Задание 4. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно
# сохраняйте все операции поступления и снятия средств в список.<br> balance = 0 CONST = 50 COMMISSION = 0.015


# MIN_COMMISSION = 30 MAX_COMMISSION = 600 number_of_operations = 0 PERCENTAGES = 0.03 AMOUNT_THRESHOLD = 5_000_000
# WEALTH_TAX = 0.1
#
#
# history = []

# def replenish(replenish):
#         global balance
#         global number_of_operations
#         global history
#         if balance > AMOUNT_THRESHOLD or replenish + balance >= AMOUNT_THRESHOLD:
#             replenish = replenish - (replenish * WEALTH_TAX)
#             history.append(f'replenish: {replenish}')
#         if replenish % CONST != 0:
#             print('Please deposit a multiple of 50!')
#             print(f'Your balance is equal to: {balance} y.e.')
#         else:
#             if replenish * COMMISSION < MIN_COMMISSION:
#                 replenish = replenish + 30
#                 balance = balance + replenish
#                 history.append(f'replenish: {replenish}')
#             elif replenish * COMMISSION > MAX_COMMISSION:
#                 replenish = replenish + 600
#                 balance = balance + replenish
#                 history.append(f'replenish: {replenish}')
#             else:
#                 balance = balance + (replenish + (replenish * COMMISSION))
#                 history.append(f'replenish: {replenish}')

#             number_of_operations += 1 
#             if number_of_operations > 3:
#                 balance = balance + (replenish * PERCENTAGES)
#                 history.append(f'replenish: {replenish}')
#                 number_of_operations = 0
#             print(f'Your balance is equal to: {balance} y.e.')

# def  take_off(take_off):
#         global balance
#         global number_of_operations   
#         global history        
#         if balance > AMOUNT_THRESHOLD:
#             take_off = take_off + (take_off * WEALTH_TAX)
#             history.append(f'take_off: {take_off}')

#         if take_off % CONST != 0:
#             print('Please deposit a multiple of 50!')
#             print(f'Your balance is equal to: {balance} y.e.')
#         else:
#             if take_off * COMMISSION < MIN_COMMISSION:
#                 take_off = take_off + 30
#                 balance = balance - take_off
#                 history.append(f'take_off: {take_off}')
#             elif take_off * COMMISSION > MAX_COMMISSION:
#                 take_off = take_off + 600
#                 balance = balance - take_off
#                 history.append(f'take_off: {take_off}')
#             else:
#                 balance = balance - (take_off + (take_off * COMMISSION))
#                 history.append(f'take_off: {take_off}')
#             if balance < 0:
#                 balance = balance + take_off
#                 print('Insufficient funds to withdraw')
#                 number_of_operations -= 1 
#             number_of_operations += 1 
#             if number_of_operations > 3:
#                 balance = balance + (take_off * PERCENTAGES)
#                 history.append(f'take_off: {take_off}')
#                 number_of_operations = 0
#             print(f'Your balance is equal to: {balance} y.e.')


# while exit != 'Exit':
#     action = str(input('What action do you want to perform? To withdraw money, click -> take_off. To deposit money to the account, click -> replenish. To exit, press Exit: '))
#     if action == 'replenish':
#         replenish(int(input('Enter the amount to top up your account: ')))
#     elif action == 'take_off':
#         take_off(int(input('enter the withdrawal amount: ')))
#     elif action == 'Exit':
#         print(f'Your balance is equal to: {balance} y.e.')
#         break

# print(history)

# ***********************************************************
# Урок 2. Напишите функцию для транспонирования матрицы <br>

# mtrx = [[1, 3], [2, 4]]
# tr_mtrx = [[0, 0], [0, 0]]
# def transport(mtrx):
#     tr_mtrx = [[0, 0], [0, 0]]
#     for i in range(len(mtrx)):
#         for n in range(len(mtrx[0])):
#             tr_mtrx[n][i] = mtrx[i][n]

#     for idx in tr_mtrx:
#         print(idx)

# transport(mtrx)

# ***********************************************************
# Задание 1/1. Напишите функцию, которая при запуске заменяет
# содержимое переменных оканчивающихся на s (кроме
# переменной из одной буквы s) на None.

# res = 1
# re = 2
# abs = 3
# ab = 4

# variable_dictionary = {
#     'res': res,
#     're': re,
#     'abs': abs,
#     'ab': ab

#     }
# def replacement(variable_dictionary):
#     for key, _ in variable_dictionary.items():
#         i = list(key)
#         if i[-1] == "s":
#             variable_dictionary[key] = None
#         else:
#             continue


# replacement(variable_dictionary)

# res = variable_dictionary['res']
# re = variable_dictionary['re']
# abs = variable_dictionary['abs']
# ab = variable_dictionary['ab']
# print(res, re, abs, ab)

# ***********************************************************
# Задание 1/2. Функция получает на вход словарь с названием компании в
# качестве ключа и списком с доходами и расходами (3-10
# чисел) в качестве значения.


# company = {
#     'sber': [500, -1000, 3000, -700, 900, -300],
#     'alfa': [300, -1500, 8000, -5400],
#     'vtb': [700, -900, 1000, -1500, 1000, -1300]
# }

# total_company = {}
# status = True
# for key, var in company.items():
#     total = sum(var)
#     total_company[key] = total

# for key, var in total_company.items():
#     if var < 0:
#         if var < 0:
#             status = False


# print(status)

# *********************************************************** Задание 2. Напишите функцию принимающую на вход только
# ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.<br>


# dictionary = {
#     'abs': 123,
#     'edc': 456,
#     'tgb': 789
# }
# revers = dict(zip(dictionary.values(), dictionary.keys()))
# print(revers)
