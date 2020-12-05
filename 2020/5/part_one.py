import sys
from pathlib import Path
from utils import get_seat_by_code, get_seat_id, sortig_by_farthest


def find_bigger_seat_id() -> int:
    with Path('./input.txt').open() as input_file:
        seats = input_file.read().splitlines()
    seats.sort(key=sortig_by_farthest, reverse=True)
    farthest_seat = get_seat_by_code(seats[0])
    return get_seat_id(*farthest_seat)


if __name__ == '__main__':
    result = find_bigger_seat_id()
    sys.stdout.write(f'Result: {result}\n')
