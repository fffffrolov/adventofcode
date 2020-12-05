from typing import Tuple


def get_number_by_code(code: str, max_value: int) -> int:
    lower = 0
    upper = max_value - 1

    for step in code:
        result = lower + (upper - lower) // 2
        if step == 'B' or step== 'R':
            result = result + 1
            lower = result
        else:
            upper = result
    return result


def get_seat_by_code(code: str) -> Tuple[int]:
    row = get_number_by_code(code[:7], 128)
    col = get_number_by_code(code[7:], 8)
    return row, col


def get_code_by_number(value: int,
                       seats_count: int,
                       under_half_value: str,
                       over_half_value: str) -> str:
    direction_map = ''
    lower_limit = 0
    upper_limit = seats_count - 1
    while upper_limit - lower_limit > 1:
        center = lower_limit + (upper_limit - lower_limit) / 2
        if value > center:
            lower_limit = center
            direction_map += over_half_value
        else:
            upper_limit = center
            direction_map += under_half_value
    return direction_map


def get_code_by_seat(row: int, col: int) -> str:
    row_map = get_code_by_number(row, 128, 'F', 'B')
    col_map = get_code_by_number(col, 8, 'L', 'R')
    return row_map + col_map


def sortig_by_farthest(code: str) -> int:
    '''
    function builds number by code replacing B and R with 1 and F and L with 0
    FFFBBFFLLR - > 0001100001
    BFBFBFBLRL - > 1010101010
    '''
    return int(
        code.replace('B', '1') \
        .replace('F', '0') \
        .replace('R', '1') \
        .replace('L', '0')
    )


def get_seat_id(row: int, col: int):
    return row * 8 + col
