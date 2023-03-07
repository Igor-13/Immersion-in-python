# 3. Напишите функцию, которая открывает на чтение созданных в прошлых задачах файлы с числами и именами
from pathlib import Path
from typing import TextIO


def read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if line == '':
        fd.seek(0)
        return read_or_begin(fd)
    return line[:-1]


def unification_file(numbers: Path, strings: Path, result: Path) -> None:
    f_num = open(numbers, 'r', encoding='utf-8')
    f_str = open(strings, 'r', encoding='utf-8')
    f_res = open(result, 'w', encoding='utf-8')
    with (f_num, f_str, f_res):
        len_str = sum(1 for _ in f_str)
        len_num = sum(1 for _ in f_num)
        for _ in range(max(len_str, len_num)):
            name = read_or_begin(f_str)
            two_num = read_or_begin(f_num)
            num_i, num_f = two_num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_res.write(f'{name.lower()}{-mult}\n')
            elif mult > 0:
                f_res.write(f'{name.upper()}{int(-mult)}\n')


if __name__ == '__main__':
    unification_file(Path('num.txt'), Path('strings.txt'), Path('result.txt'))
