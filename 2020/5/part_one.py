import sys
from pathlib import Path


def get_code_id(code: str) -> int:
    """
    convert code to binary and then to int
    FFFFFFFLLR -> 0000000001 -> 1
    FFFFFFFLRL -> 0000000010 -> 2
    ...
    BFBBBBBRRR -> 1011111111 -> 767
    BBBBBBBRRR -> 1111111111 -> 1023
    """
    return int(
        '0b'+code.replace('B', '1')
        .replace('R', '1')
        .replace('F', '0')
        .replace('L', '0'),
        2,
    )


def find_max_seat_id() -> int:
    ids = set()
    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            ids.add(get_code_id(line.strip()))
    return max(ids)


if __name__ == '__main__':
    result = find_max_seat_id()
    sys.stdout.write(f'Result: {result}\n')
