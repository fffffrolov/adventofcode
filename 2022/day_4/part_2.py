# https://adventofcode.com/2022/day/4
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


def is_overlap(line: str) -> bool:
    [start_1, end_1, start_2, end_2] = list(map(int, line))

    not_overlap = (start_1 < start_2 and end_1 < start_2) or (start_2 < start_1 and end_2 < start_1)

    return not not_overlap


def get_total_overlapped() -> int:
    total = 0

    for line in _read_input():
        if (matches := PATTERN.findall(line)) and is_overlap(matches[0]):
            total += 1

    return total


def main():
    start = time.time()

    result = get_total_overlapped()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
