# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога. принимать параметр расширение конечного
# файла. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и
# расширение. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os
from random import randint


def re_name(end_name: str, n_count: int, extension: str, end_extension: str, range_name: list):
    idx = 1
    fls = os.listdir()
    for i in fls:
        n = i.split('.')
        if n[-1] == extension:
            num = '0' * n_count
            new_name = i[range_name[0]:range_name[1]]
            new_name = new_name + end_name
            num_name = num + str(idx)
            if len(num_name) > 3:
                num_name = num_name[1:]
            idx += 1
            new_name = new_name + num_name
            new_name = new_name + '.' + end_extension
            os.rename(i, new_name)


if __name__ == '__main__':
    re_name('_lesson7_', n_count=3, extension='zip', end_extension='bin', range_name=[2, 4])
