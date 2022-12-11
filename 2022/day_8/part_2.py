# https://adventofcode.com/2022/day/8
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


@dataclass
class Tree:
    y: int
    x: int
    height: int
    forest: 'Forest'
    left_viewing_distance: int = 0
    right_viewing_distance: int = 0
    top_viewing_distance: int = 0
    bottom_viewing_distance: int = 0
    scenic_score: int = 0

    def set_scenic_score(self):
        self.set_top_viewing_distance()
        self.set_left_viewing_distance()
        self.set_bottom_viewing_distance()
        self.set_right_viewing_distance()

        self.scenic_score = (
            self.top_viewing_distance *
            self.left_viewing_distance *
            self.bottom_viewing_distance *
            self.right_viewing_distance
        )

        self.forest.max_scenic_score = max(self.forest.max_scenic_score, self.scenic_score)

    def set_left_viewing_distance(self) -> None:
        if self.x == 1:
            self.left_viewing_distance = 1
            return

        forest_line = self.forest.tries[self.y]

        for another_tree in reversed(forest_line[:self.x]):
            self.left_viewing_distance += 1
            if self.height <= another_tree.height:
                return

    def set_right_viewing_distance(self) -> None:
        if self.x == self.forest.x_length - 1:
            self.right_viewing_distance = 1
            return

        forest_line = self.forest.tries[self.y]

        for another_tree in forest_line[self.x + 1:]:
            self.right_viewing_distance += 1

            if self.height <= another_tree.height:
                return

    def set_top_viewing_distance(self) -> None:
        if self.y == 1:
            self.top_viewing_distance = 1
            return

        for y in range(self.y-1, -1, -1):
            another_tree = self.forest.tries[y][self.x]

            self.top_viewing_distance += 1
            if self.height <= another_tree.height:
                return

    def set_bottom_viewing_distance(self) -> None:
        if self.y == self.forest.y_length - 1:
            self.bottom_viewing_distance = 1
            return

        for y in range(self.y + 1, self.forest.y_length + 1):
            another_tree = self.forest.tries[y][self.x]

            self.bottom_viewing_distance += 1
            if self.height <= another_tree.height:
                return


@dataclass
class Forest:
    tries: list[list[Tree]]
    total_visible: int = 0
    x_length: int = 0
    y_length: int = 0
    max_scenic_score: int = 0

    def find_max_scenic_score(self) -> int:
        for forest_line in self.tries[1:]:
            for tree in forest_line[1:]:
                tree.set_scenic_score()

        return self.max_scenic_score


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def _iter_input(objects: Iterable[Any]) -> Iterator[Any]:
    return filter(lambda _l: bool(_l), map(str.strip, objects))


def build_forest() -> Forest:
    forest = Forest([[]])
    y = x = 0

    for y, line in enumerate(_iter_input(_read_input())):

        forest.tries.append([])
        for x, el in enumerate(_iter_input(line)):

            tree = Tree(y, x, height=int(el), forest=forest)
            forest.tries[y].append(tree)

        forest.x_length = max(forest.x_length, x)

    forest.y_length = max(forest.y_length, y)

    return forest


def main() -> None:
    start = time.time()

    forest = build_forest()
    result = forest.find_max_scenic_score()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
