import sys
from pathlib import Path
from typing import List, Optional


def get_data() -> List[str]:
    with Path('./input.txt').open() as input_file:
        lines = [int(el) for el in input_file.read().splitlines()]
    return lines


def find_summands_for_value(value: int, lines: List[str]) -> Optional[int]:
    summands = {}
    for line in lines:
        if summands.get(line):
            return summands[line] * line
        summands[value - line] = line


def calculate() -> Optional[int]:
    lines = get_data()

    for index, line in enumerate(lines):
        list_without_value = lines[:index] + lines[index+1:]
        summands_multiplication = find_summands_for_value(
            2020 - line, list_without_value,
        )
        if summands_multiplication is not None:
            return summands_multiplication * line


if __name__ == '__main__':
    result = calculate()
    if result is None:
        sys.stdout.write('Oh now! There is no result!\n')
    sys.stdout.write(f'resilt is \n{result}\n')
