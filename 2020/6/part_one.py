import sys
from pathlib import Path


def count() -> int:
    total = 0
    group_values = set()
    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            line = line.strip()
            if not line:
                total += len(group_values)
                group_values = set()
            group_values.update(set(line))
    total += len(group_values)
    return total


if __name__ == '__main__':
    result = count()
    sys.stdout.write(f'Result: {result}\n')
