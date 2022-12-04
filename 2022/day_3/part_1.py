# https://adventofcode.com/2022/day/3
import os
import string
import sys
import time
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


def get_line_score_v1(line: str) -> int:
    score = 0

    total = len(line)
    first, second = set(line[:total//2]), set(line[total//2:])
    for commoin in first.intersection(second):
        score += letter_scores.get(commoin, 0)

    return score


def get_line_score_v2(line: str) -> int:
    score = 0
    part_2_map = {}
    total = len(line)

    for letter in line[total//2:]:
        part_2_map[letter] = letter_scores.get(letter, 0)

    for letter in line[:total//2]:
        score += part_2_map.get(letter, 0)

    return score


def get_sum() -> int:
    score = 0
    for line in _read_input():
        score += get_line_score_v1(line)
    return score


def main():
    start = time.time()

    result = get_sum()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
