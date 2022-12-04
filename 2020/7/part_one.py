import re
import sys
from pathlib import Path
from typing import Tuple

split_rule_regex = re.compile(
    r'(?:([a-z]+ [a-z]+){1} bags contain )(.*)', re.IGNORECASE)
contained_bags_regex = re.compile(
    r'(?:(?: ?\d ([a-z]+ [a-z]+) bag)(?:s)?(?:,|\.))', re.IGNORECASE)


def expand_rule(rule: str) -> Tuple:
    main_bag, contained_bags = split_rule_regex.match(rule).groups()
    return main_bag, contained_bags_regex.findall(contained_bags)


def build_parrents_set(tree: dict, bag: str) -> set:
    parents = tree.get(bag) or set()
    for parent in parents.copy():
        parents |= build_parrents_set(tree, parent)
    return parents


def count() -> int:
    tree = {}
    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            main_bag, contained_bags = expand_rule(line)
            for bag in contained_bags:
                if tree.get(bag) is None:
                    tree[bag] = set()
                tree[bag].add(main_bag)

    parents = build_parrents_set(tree, 'shiny gold')
    return len(parents)


if __name__ == '__main__':
    result = count()
    sys.stdout.write(f'Result: {result}\n')
