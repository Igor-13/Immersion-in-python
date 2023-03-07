# 6. Дорабатываем функции из предыдущих задач. Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). Существующие файла не
# должны удаляться/изменяться в случае совпадения имён.
import os

from task_4 import make_files
import shutil

image_new = "new"


def generat(dr: str, count: int):
    make_files('bin', count)
    fls = os.listdir()
    if os.path.exists(image_new):
        for _ in fls:
            n = _.split('.')
            if n[-1] == 'bin':
                shutil.move(_, dr)
    else:
        os.mkdir("new")
        generat(image_new, count)


if __name__ == '__main__':
    generat(image_new, 3)
