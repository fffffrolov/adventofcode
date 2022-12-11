# https://adventofcode.com/2022/day/9
import os
import sys
import time
from pathlib import Path
from typing import Any, Iterable, Iterator

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
ROPE_LENGTH = 10
ROPE: list[list[int, int]] = [[0, 0] for _ in range(ROPE_LENGTH)]
TAIL_PATH = {(0, 0)}


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def _iter_input(objects: Iterable[Any]) -> Iterator[Any]:
    return filter(lambda _l: bool(_l), map(str.strip, objects))


def read_move(step: str) -> tuple[int, int, int]:
    direction, moves = step.split(' ')

    index = 0 if direction in ('R', 'L') else 1
    step = 1 if direction in ('R', 'U') else -1

    return int(moves), index, step


def move_head(moves: int, index: int, step: int = 1) -> None:
    for _ in range(moves):
        ROPE[0][index] += 1 * step
        for rope_index in range(1, ROPE_LENGTH):
            if need_to_move_next_part(rope_index):
                move_next_part(rope_index)


def need_to_move_next_part(index: int) -> bool:
    if index >= len(ROPE) or index == 0:
        return False

    part = ROPE[index]
    previous_part = ROPE[index-1]

    return abs(previous_part[0] - part[0]) > 1 or abs(previous_part[1] - part[1]) > 1


def move_next_part(index: int) -> None:
    previous_part = ROPE[index - 1]

    for ind in (0, 1):
        if previous_part[ind] > ROPE[index][ind]:
            ROPE[index][ind] += 1
        elif previous_part[ind] < ROPE[index][ind]:
            ROPE[index][ind] -= 1

    if index == ROPE_LENGTH - 1:
        TAIL_PATH.add(tuple(ROPE[index]))


def main() -> None:
    start = time.time()

    for line in _iter_input(_read_input()):
        move = read_move(line)
        move_head(*move)

    result = len(TAIL_PATH)

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
