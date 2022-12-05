# https://adventofcode.com/2022/day/5
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterator, Optional

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

PATTERN = re.compile(r'(\d+)')

STACKS = [
    ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    ['M', 'F', 'V'],
    ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    ['D', 'Q', 'R', 'T', 'F'],
    ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    ['W', 'F', 'R', 'L', 'C', 'T'],
    ['T', 'Z', 'N', 'S'],
    ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N'],
]


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def parse_step(line: str) -> Optional[list[int, int, int]]:
    if (matches := PATTERN.findall(line)):
        return list(map(int, matches))
    return None


def make_step(amount: int, from_stack: int, to_stack: int) -> None:
    STACKS[to_stack] += STACKS[from_stack][-amount:]
    STACKS[from_stack] = STACKS[from_stack][:-amount]


def make_steps() -> None:
    for line in _read_input():
        if line.startswith('move') and (step := parse_step(line)):
            make_step(step[0], step[1] - 1, step[2] - 1)


def get_state() -> str:
    return ''.join(stack[-1] for stack in STACKS if stack)


def main() -> None:
    start = time.time()

    make_steps()
    result = get_state()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
