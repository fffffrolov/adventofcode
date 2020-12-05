import sys
from pathlib import Path
from typing import Optional


def calculate() -> Optional[int]:
    summands = {}
    with Path('./input.txt').open() as input_file:
        lines = input_file.read().splitlines()

    for line in lines:
        number = int(line)
        if summands.get(number):
            return summands[number] * number
        summands[2020 - int(number)] = number


if __name__ == '__main__':
    result = calculate()
    if result is None:
        sys.stdout.write('Oh now! There is no result!\n')
    sys.stdout.write(f'resilt is \n{result}\n')
