# 7. Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. Каждая группа включает
# файлы с несколькими расширениями. В исходной папке должны остаться только те файлы, которые не подошли для
# сортировки.
import os
import shutil

image_path = "image"
video_path = "video"
txt_path = "txt"


def routing(fls: list):
    for i in fls:
        n = i.split('.')
        if n[-1] == 'jpg' or n[-1] == 'png':
            shutil.move(i, image_path)
        elif n[-1] == 'bin' or n[-1] == 'txt':
            shutil.move(i, txt_path)
        elif n[-1] == 'mkv' or n[-1] == '3g2':
            shutil.move(i, video_path)


if __name__ == '__main__':
    fls = os.listdir()
    routing(fls)
