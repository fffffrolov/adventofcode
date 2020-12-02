import sys
from pathlib import Path
from typing import List, Optional


def calculate() -> Optional[int]:
    data = {}
    with Path('./input.txt').open() as input_file:
        lines = input_file.read().splitlines()
    
    for line in lines:
        number = int(line)
        if data.get(number):
            return data[number] * number
        data[2020 - int(number)] = number


def main():
    result = calculate()
    if result is None:
        sys.stdout.write('Oh now! There is no result!\n')
    sys.stdout.write(f'resilt is \n{result}\n')


if __name__ == '__main__':
    main()
