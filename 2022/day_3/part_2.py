# https://adventofcode.com/2022/day/3
import os
import string
import sys
import time
from itertools import islice
from pathlib import Path
from typing import Iterator

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

letter_scores = {
    letter: index + 1
    for index, letter in enumerate(string.ascii_letters)
}


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def batched(iterable: Iterator[str], n: int) -> Iterator[Iterator[Iterator[str]]]:
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def get_group_score(group: Iterator[Iterator[str]]) -> int:
    score = 0

    intersection = None

    for line in group:
        if intersection is None:
            intersection = set(line)
        else:
            intersection = set(line).intersection(intersection)

    for common in intersection:
        score += letter_scores.get(common, 0)

    return score


def get_sum():
    score = 0
    data = _read_input()
    for group in batched(data, 3):
        score += get_group_score(group)
    return score


def main():
    start = time.time()

    result = get_sum()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
