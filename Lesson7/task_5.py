# 5. Создайте новую функцию которая генерирует файлы с разными расширениями.
from task_4 import make_files


def main_maker(extensions: dict):
    # def main_maker(**kwargs: dict)
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':
    data = {
        'jpg': 2,
        'mkv': 3,
        'zip': 3,
    }
    main_maker(data)
