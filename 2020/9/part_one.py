import sys
from pathlib import Path


def has_summands(group: list, total: int) -> bool:
    for first in group:
        second = total - first
        if second == first:
            continue
        if second in group:
            return True
    return False


def find_invalid() -> int:
    step = 25
    with Path('./input.txt').open() as input_file:
        lines = [int(line) for line in input_file.read().splitlines()]

    for i in range(step, len(lines)):
        element = lines[i]
        previous = lines[i - step: i]
        if not has_summands(previous, element):
            return element


if __name__ == '__main__':
    result = find_invalid()
    sys.stdout.write(f'Result: {result}\n')
