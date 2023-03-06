""" Урок №6 """
# Задание 1/1. Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную
# защищённую функцию.


# data = input('enter format date DD.MM.YYYY: ' )
# DAY31 = [1, 3, 5, 7, 8, 10, 12]
# DAY30 = [4, 6, 9, 11]
# FEBRUARY = [2]
# day, month, year, *_  = data.split('.')


# def examination(day, month, year, *_):
#     if len(_) == 0:
#         if int(year) % 4 == 0:
#             return _leap_year(day, month, year)
#         if 1 < int(year) < 9999:
#             if 1 < int(month) < 12:
#                 if int(month) in DAY31 and 1 <= int(day) <= 31:
#                     return True
#                 elif int(month) in DAY30 and 1 <= int(day) <= 30:
#                     return True
#                 elif int(month) in FEBRUARY and int(day) <= 28:
#                     return True
#     return False            

# def _leap_year(day, month, year):
#     if 1 < int(year) < 9999:
#         if 1 < int(month) < 12:
#             if int(month) in DAY31 and 1 <= int(day) <= 31:
#                 return True
#             elif int(month) in DAY30 and 1 <= int(day) <= 30:
#                 return True
#             elif int(month) in FEBRUARY and int(day) <= 29:
#                 return True
#     return False 

# print(examination(day, month, year, *_))
