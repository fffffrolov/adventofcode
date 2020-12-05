import sys
from pathlib import Path


def get_code_id(code: str) -> int:
    '''
    convert code to binary and then to int
    FFFFFFFLLR -> 0000000001 -> 1
    FFFFFFFLRL -> 0000000010 -> 2
    ...
    BFBBBBBRRR -> 1011111111 -> 767
    BBBBBBBRRR -> 1111111111 -> 1023
    '''
    return int(
        '0b'+code.replace('B', '1')
        .replace('R', '1')
        .replace('F', '0')
        .replace('L', '0'), 
        2
    )


def get_missed_seat(seats: set) -> int:
    last_id = None
    for seat_id in sorted(seats):
        if last_id is not None and seat_id - last_id > 1:
            return seat_id - 1
        last_id = seat_id


def find_my_seat() -> int:
    with Path('./input.txt').open() as input_file:
        ids = set(
            get_code_id(line.strip())
            for line in input_file.readlines()
        )
    return get_missed_seat(ids)


if __name__ == '__main__':
    result = find_my_seat()
    if result is None:
        sys.stdout.write('Probably this is not my plane\n')
    else:
        sys.stdout.write(f'My seat id is: {result}\n')
