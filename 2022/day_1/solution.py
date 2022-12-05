# https://adventofcode.com/2022/day/1
import os
import sys
import time
from pathlib import Path

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def _read_input() -> str:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        return input_file.read()


def find_max(input_data: str) -> int:
    max_value = 0

    for elf in input_data.strip().split('\n\n'):
        max_value = max(
            max_value, sum([int(item) for item in elf.split('\n')]),
        )

    return max_value


def find_top(input_data: str, limit: int = 3) -> int:
    values = []

    for elf in input_data.strip().split('\n\n'):
        values.append(sum([int(item) for item in elf.split('\n')]))

    values = sorted(values, reverse=True)

    return values[:limit]


def main() -> None:
    start = time.time()

    data = _read_input()
    max_value = find_max(data)
    top_three = sum(find_top(data, 3))

    end = time.time()

    sys.stdout.write(
        f'max is {max_value}\ntop three is {top_three}\ntime: {(end - start)*1000.0:.3f}ms\n',
    )


if __name__ == '__main__':
    main()
