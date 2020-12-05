import sys
from pathlib import Path
from typing import Tuple, Optional, List
from utils import get_code_by_seat, get_seat_by_code, get_seat_id, sortig_by_farthest


def get_seat_id(row: int, col: int):
    return row * 8 + col


def find_missin_seat(seats: List[str], lower_bound: int, upper_bound: int) -> Optional[Tuple[int]]:
    for row in range(lower_bound + 1, upper_bound):
        for col in range(8):
            seat_code = get_code_by_seat(row, col)
            if seat_code not in seats:
                return row, col


def find_my_seat() -> int:
    with Path('./input.txt').open() as input_file:
        seats = input_file.read().splitlines()
    seats.sort(key=sortig_by_farthest, reverse=True)
    
    farthest_seat = get_seat_by_code(seats[0])
    nearest_seat = get_seat_by_code(seats[-1])
    
    my_seat = find_missin_seat(seats, nearest_seat[0], farthest_seat[0])

    return get_seat_id(*my_seat)
    


if __name__ == '__main__':
    result = find_my_seat()
    sys.stdout.write(f'My seat is: {result}\n')
