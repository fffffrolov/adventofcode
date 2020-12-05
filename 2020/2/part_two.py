import re
import sys
from pathlib import Path


def test_password(password: str, letter: str, pos_1: str, pos_2: str) -> bool:
    pos_1 = int(pos_1) - 1
    pos_2 = int(pos_2) - 1
    first_and_not_seccond = f'^(?!.{{{pos_2}}}{letter})(.{{{pos_1}}}{letter}).*$'
    not_first_and_seccond = f'^(?!.{{{pos_1}}}{letter})(.{{{pos_2}}}{letter}).*$'
    regex = re.compile(f'{first_and_not_seccond}|{not_first_and_seccond}')
    return True if regex.match(password) else False


def count() -> int:
    total = 0
    template = r'(?P<pos_1>\d+)-(?P<pos_2>\d+) (?P<letter>\w{1}): (?P<password>\w+)'
    with Path('./input.txt').open() as input_file:
        for line in input_file.read().splitlines():
            password = re.match(template, line)
            total += test_password(**password.groupdict())
    return total


if __name__ == '__main__':
    total = count()
    sys.stdout.write(f'Total: {total}\n')
