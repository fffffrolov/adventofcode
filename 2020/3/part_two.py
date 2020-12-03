from functools import reduce
import sys
from pathlib import Path


def get_next_index(index: int, width: int, steps: int) -> int:
    return (index + steps) % width


def slither() -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [0] * len(slopes)
    indexes = [0] * len(slopes)
    line_num = 0
    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            if line_num != 0:
                line = line.strip()
                for slope_type, slope in enumerate(slopes):
                    if line_num % slope[1] != 0:
                        continue
                    indexes[slope_type] = get_next_index(indexes[slope_type], len(line), slope[0])
                    if line[indexes[slope_type]] == '#':
                        trees[slope_type] += 1
            line_num += 1
    return reduce((lambda x, y: x * y), trees)


if __name__ == '__main__':
    result = slither()
    sys.stdout.write(f'Total: {result}\n')
