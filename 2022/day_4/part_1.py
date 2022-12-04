# https://adventofcode.com/2022/day/3
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterator

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

PATTERN = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def has_contained(line: str) -> bool:
    [start_1, end_1, start_2, end_2] = values = list(map(int, line))
    min_value = min(values)
    max_value = max(values)

    return (start_1, end_1) == (min_value, max_value) or (start_2, end_2) == (min_value, max_value)


def get_total_fully_contain() -> int:
    total = 0

    for line in _read_input():
        if (matches := PATTERN.findall(line)) and has_contained(matches[0]):
            total += 1

    return total


def main():
    start = time.time()

    result = get_total_fully_contain()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
