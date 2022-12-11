# https://adventofcode.com/2022/day/8
import os
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


@dataclass
class Tree:
    height: int
    forest: 'Forest'
    visible: bool = False

    def set_is_visible(self) -> None:
        if not self.visible:
            self.forest.total_visible += 1

        self.visible = True

    def is_visible_from_left_or_top(self, y: int, x: int) -> None:
        result = False

        if x == 0 or y == 0:
            result = True

        if self.height > self.forest.left_max[y]:
            self.forest.left_max[y] = self.height
            result = True

        if self.height > self.forest.top_max[x]:
            self.forest.top_max[x] = self.height
            result = True

        if result:
            self.set_is_visible()

    def is_visible_from_right_or_bottom(self, y: int, x: int) -> None:
        result = False

        if x == self.forest.x_length or y == self.forest.y_length:
            result = True

        if self.height > self.forest.right_max[y]:
            self.forest.right_max[y] = self.height
            result = True

        if self.height > self.forest.bottom_max[x]:
            self.forest.bottom_max[x] = self.height
            result = True

        if result:
            self.set_is_visible()


@dataclass
class Forest:
    tries: Optional[list[list[Tree]]] = None
    total_visible: int = 0
    x_length: int = 0
    y_length: int = 0

    left_max: dict[int, int] = field(default_factory=lambda: defaultdict(lambda: 0))     # → for each column
    top_max: dict[int, int] = field(default_factory=lambda: defaultdict(lambda: 0))      # ↓ for each row
    right_max: dict[int, int] = field(default_factory=lambda: defaultdict(lambda: 0))    # ← for each column
    bottom_max: dict[int, int] = field(default_factory=lambda: defaultdict(lambda: 0))   # ↑ for each row


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def _iter_input(objects: Iterable[Any]) -> Iterator[Any]:
    return filter(lambda _l: bool(_l), map(str.strip, objects))


def walk_top_left(forest: Forest) -> None:
    y = x = 0

    forest.tries = []
    for y, line in enumerate(_iter_input(_read_input())):

        forest.tries.append([])
        for x, el in enumerate(_iter_input(line)):

            tree = Tree(height=int(el), forest=forest)
            tree.is_visible_from_left_or_top(y, x)

            forest.tries[y].append(tree)

        forest.x_length = max(forest.x_length, x)

    forest.y_length = max(forest.y_length, y)


def walk_bottom_right(forest: Forest) -> None:
    for y in range(forest.y_length, -1, -1):
        for x in range(forest.x_length, -1, -1):
            forest.tries[y][x].is_visible_from_right_or_bottom(y, x)


def main() -> None:
    start = time.time()

    forest = Forest()

    walk_top_left(forest)
    walk_bottom_right(forest)

    result = forest.total_visible

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
