# https://adventofcode.com/2022/day/7
import os
import sys
import time
from pathlib import Path
from typing import Iterator

from anytree import ChildResolverError, Node, Resolver

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

ROOT_NODE = Node('', size=0)
CURRENT_NODE = ROOT_NODE
TOTAL_SYSTEM_SPACE = 70000000
NEEDED_SPACE = 30000000


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


def find_node_to_delete(min_to_free: int) -> int:
    to_test = set(ROOT_NODE.leaves)
    smallest_node = walk_tree(min_to_free, to_test)

    return smallest_node.size


def walk_tree(min_size: int, to_test: set = None) -> Node:
    smallest_node = None

    while to_test:
        node = to_test.pop()
        if node.size < min_size:
            if node.depth > 1:
                to_test.add(node.parent)
        else:
            if smallest_node is None:
                smallest_node = node

            if node.size < smallest_node.size:
                if smallest_node.parent in to_test:
                    to_test.remove(smallest_node.parent)
                smallest_node = node

    return smallest_node


def main() -> None:
    start = time.time()

    read_commands()

    result = 0
    free_space = TOTAL_SYSTEM_SPACE - ROOT_NODE.size
    if free_space < NEEDED_SPACE:
        result = find_node_to_delete(NEEDED_SPACE-free_space)

    end = time.time()

    sys.stdout.write(f'result = {result}\ntime: {(end - start)*1000.0:.3f}ms\n')


if __name__ == '__main__':
    main()
