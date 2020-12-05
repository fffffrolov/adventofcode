from typing import Tuple


def get_number_by_code(code: str, max_value: int) -> int:
    lower = 0
    upper = max_value - 1

    for step in code:
        result = lower + (upper - lower) // 2
        if step == 'B' or step == 'R':
            result = result + 1
            lower = result
        else:
            upper = result
    return result


def get_seat_by_code(code: str) -> Tuple[int]:
    row = get_number_by_code(code[:7], 128)
    col = get_number_by_code(code[7:], 8)
    return row, col


def sortig_by_farthest(code: str) -> int:
    '''
    function builds number by code replacing B and R with 1 and F and L with 0
    FFFFFFFLLR -> 0000000001 - the lowest possible seat number
    FFFFFFFLRL -> 0000000010
    FFFFFFFLRR -> 0000000011
    FFFFFFFRLL -> 0000000100
    FFFFFFFRLR -> 0000000101
    ...
    BFBBBBBRRR -> 1011111111
    BBBBBBBRRR -> 1111111111 - the greatest possible seat number
    '''
    return int(
        code.replace('B', '1')
        .replace('R', '1')
        .replace('F', '0')
        .replace('L', '0')
    )


def get_seat_id(row: int, col: int):
    return row * 8 + col
