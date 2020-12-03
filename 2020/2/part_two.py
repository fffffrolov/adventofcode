import re
import sys
from pathlib import Path


def test_password(password: str, letter: str, pos_1: str, pos_2: str) -> bool:
    pos_1 = int(pos_1) - 1
    pos_2 = int(pos_2) - 1
    regex = re.compile(f'^(?!.{{{pos_1}}}{letter})(.{{{pos_2}}}{letter}).*$|^(?!.{{{pos_2}}}{letter})(.{{{pos_1}}}{letter}).*$')
    return True if regex.match(password) else False


def count() -> int:
    total = 0
    with Path('./input.txt').open() as input_file:
        for line in input_file.read().splitlines():
            data = re.match(r'(?P<pos_2>\d+)-(?P<pos_1>\d+) (?P<letter>\w{1}): (?P<password>\w+)', line) 
            total += test_password(**data.groupdict())
    return total
        
    
def main():
    total = count()
    sys.stdout.write(f'Total: {total}\n')


if __name__ == '__main__':
    main()
