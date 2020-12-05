import sys
from pathlib import Path
from utils import get_seat_by_code, get_seat_id, sortig_by_farthest


def find_my_seat() -> int:
    with Path('./input.txt').open() as input_file:
        seats = input_file.read().splitlines()
    seats.sort(key=sortig_by_farthest, reverse=True)

    missed_seat = None
    last_id = None
    for seat in seats:
        seat_id = get_seat_id(*get_seat_by_code(seat))
        if last_id is not None and last_id - seat_id > 1:
            missed_seat = last_id - 1
            break
        last_id = seat_id

    return missed_seat


if __name__ == '__main__':
    result = find_my_seat()
    sys.stdout.write(f'My seat is: {result}\n')
