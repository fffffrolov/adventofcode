# https://adventofcode.com/2022/day/6
import os
import sys
import time
from pathlib import Path
from typing import Iterator

from anytree import ChildResolverError, Node, Resolver

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

ROOT_NODE = Node('', size=0)
CURRENT_NODE = ROOT_NODE
MAX_SIZE = 100000


def _read_input() -> Iterator[str]:
    with Path(BASE_PATH, 'input.txt').open() as input_file:
        yield from input_file.readlines()


def is_command(output: str, command: str = '') -> bool:
    return output.startswith(f'$ {command}')


def is_cd(output: str) -> bool:
    return is_command(output, 'cd')


def is_dir(output: str) -> bool:
    return output.startswith('dir')


def get_dir_name(output: str) -> str:
    return output.split('dir ')[1].strip()


def get_cd(output: str) -> str:
    return output.split('$ cd')[1].strip()


def read_commands() -> None:
    global CURRENT_NODE
    resolver = Resolver('name')

    for line in _read_input():

        if not is_command(line):
            process_ls_output(line)

        if is_cd(line):
            cd = get_cd(line)
            if cd == '/':
                continue

            CURRENT_NODE = resolver.get(CURRENT_NODE, cd)


def process_ls_output(output: str) -> None:
    size = 0

    if is_dir(output):
        name = get_dir_name(output)

        try:
            resolver = Resolver('name')
            resolver.get(CURRENT_NODE, name)
        except ChildResolverError:
            Node(name, parent=CURRENT_NODE, size=0)

    else:
        size += int(output.split(' ')[0])

    CURRENT_NODE.size += size
    for ancestor in CURRENT_NODE.ancestors:
        ancestor.size += size


def get_total_size_for_small() -> int:
    return sum(
        [node.size for node in ROOT_NODE.descendants if node.size <= MAX_SIZE],
    )


def main() -> None:
    start = time.time()

    read_commands()
    result = get_total_size_for_small()

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
