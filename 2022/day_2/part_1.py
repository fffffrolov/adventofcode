import os
import sys
import time
from pathlib import Path
from typing import Iterator

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

POINTS_MAXTRIX = {
    'A': {
        'X': 1 + 3,
        'Y': 2 + 6,
        'Z': 3 + 0,
    },
    'B': {
        'X': 1 + 0,
        'Y': 2 + 3,
        'Z': 3 + 6,
    },
    'C': {
        'X': 1 + 6,
        'Y': 2 + 0,
        'Z': 3 + 3,
    },
}


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def round_score(letter_1: str, letter_2: str) -> int:
    return POINTS_MAXTRIX[letter_1][letter_2]


def get_total_score() -> int:
    score = 0
    for round_code in _read_input():
        if round_code:
            score += round_score(*round_code.strip().split(' '))

    return score


def main():
    start = time.time()

    result = get_total_score()

    end = time.time()

    sys.stdout.write(
        f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
