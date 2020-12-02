import sys
from pathlib import Path
from typing import List, Optional



def find_parts_for_value(value: int, lines: List[str]) -> Optional[int]:
    data = {}
    for line in lines:
        if data.get(line):
            return data[line] * line
        data[value - line] = line


def calculate() -> Optional[int]:
    with Path('./input.txt').open() as input_file:
        lines = [int(el) for el in input_file.read().splitlines()]

    for index, line in enumerate(lines):
        remainder = 2020 - line
        parts_multiplication = find_parts_for_value(remainder, lines[:index]+lines[index+1:])
        if parts_multiplication:
            return parts_multiplication * line


def main():
    result = calculate()
    if result is None:
        sys.stdout.write('Oh now! There is no result!\n')
    sys.stdout.write(f'resilt is \n{result}\n')



if __name__ == '__main__':
    main()