import sys
from pathlib import Path
from typing import List, Tuple


def has_summands(group: list, total: int) -> bool:
    for first in group:
        second = total - first
        if second == first:
            continue
        if second in group:
            return True
    return False


def read_input() -> List[int]:
    with Path('./input.txt').open() as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def find_invalid(lines) -> Tuple[int, int]:
    step = 25
    with Path('./input.txt').open() as input_file:
        lines = [int(line) for line in input_file.read().splitlines()]

    for i in range(step, len(lines)):
        element = lines[i]
        previous = lines[i - step: i]
        if not has_summands(previous, element):
            return element, i


def find_encryption_weakness() -> int:
    lines = read_input()

    invalid_number, invalid_index = find_invalid(lines)

    sequences = []
    for el in lines[:invalid_index]:
        for sequence in sequences:
            sequence.append(el)
            if sum(sequence) == invalid_number:
                return min(sequence) + max(sequence)

        for ind, sequence in enumerate(sequences):
            if sum(sequence) > invalid_number:
                sequences.pop(ind)

        sequences.append([el])


if __name__ == '__main__':
    result = find_encryption_weakness()
    sys.stdout.write(f'Result: {result}\n')
