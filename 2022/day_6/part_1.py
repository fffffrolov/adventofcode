# https://adventofcode.com/2022/day/6
import os
import sys
import time
from pathlib import Path

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

MESSAGE_LENGTH = 4


def _read_input() -> str:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        return input_file.readline()


def find_start_of_packet() -> int:
    line = _read_input()
    for i in range(MESSAGE_LENGTH, len(line)):
        if len(set(line[i-MESSAGE_LENGTH:i])) == MESSAGE_LENGTH:
            return i


def main() -> None:
    start = time.time()

    result = find_start_of_packet()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
