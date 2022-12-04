import re
import sys
from pathlib import Path
from typing import Tuple

split_rule_regex = re.compile(
    r'(?:([a-z]+ [a-z]+){1} bags contain )(.*)', re.IGNORECASE,
)
contained_bags_regex = re.compile(
    r'((?: ?(?P<num>\d+) (?P<bag>[a-z]+ [a-z]+) bag)(?:s)?(?:,|\.))', re.IGNORECASE,
)


def expand_rule(rule: str) -> Tuple:
    main_bag, contained_bags = split_rule_regex.match(rule).groups()
    return main_bag, {bag[2]: int(bag[1]) for bag in contained_bags_regex.findall(contained_bags)}


def count_bag_children(tree: dict, bag: str) -> int:
    count = 0
    bag_children = tree.get(bag) or {}
    for child, child_number in bag_children.items():
        count += child_number * (count_bag_children(tree, child) + 1)
    return count


def count() -> int:
    tree = {}
    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            main_bag, contained_bags = expand_rule(line)
            tree[main_bag] = contained_bags

    return count_bag_children(tree, 'shiny gold')


if __name__ == '__main__':
    result = count()
    sys.stdout.write(f'Result: {result}\n')
