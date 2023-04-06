### Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import sys

# задача №1
 
# logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
# try:
#     num = sys.argv[1]
#     logging.info(f"The values of num are {num}, and type {type(num)}.")
#     num = int(num)
#     logging.info(f"The values of num are {num}.")
# except ValueError as err:
#     logging.exception("ValueError")

# SYSTEM = 16
# num_16 = ''

# x = num
# logging.info(f"The values of x are {x}.")
# while x > 0:
#     n = x % SYSTEM
#     if n < 10:
#         num_16 = str(n) + num_16
#     else:
#         if n == 10:
#             num_16 = 'A' + num_16
#         elif n == 11:
#             num_16 = 'B' + num_16
#         elif n == 12:
#             num_16 = 'C' + num_16
#         elif n == 13:
#             num_16 = 'D' + num_16
#         elif n == 14:
#             num_16 = 'E' + num_16
#         elif n == 15:
#             num_16 = 'F' + num_16
#         elif n == 16:
#             num_16 = 'G' + num_16

#     x //= SYSTEM


# logging.info(num_16)
# logging.info(hex(num))

# задача №2
# try:
#     logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
#     a = sys.argv[1]
#     b = sys.argv[2]
#     c = sys.argv[3]
#     logging.info(f"length of the side 'a' = {a}, 'b' = {b}, 'c' = {c}.")
# except ValueError as err:
#     logging.exception("ValueError")

# if (a + b) > c and (a + c) > b and (b + c) > a:
#     if a == b and a != c or a == c and a != b or b == c and b != a:
#         logging.info(f'a triangle with sides a = {a}, b = {b} and c = {c} is isosceles')
#     elif a == b == c:
#         logging.info(f'a triangle with sides a = {a}, b = {b} and c = {c} is equilateral')
#     else:
#         logging.info(f'a triangle with sides a = {a}, b = {b} and c = {c} is versatile')
# else:
#     logging.info('it is impossible to construct a triangle from these segments since one of the sides is greater than the sum of the other two')