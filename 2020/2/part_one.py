import re
import sys
from pathlib import Path


def test_password(password: str, letter: str, min_v: str, max_v: str) -> bool:
    max_v = int(max_v) + 1
    regex = re.compile(
        f'^(?!(.*{letter}){{{max_v}}})(.*{letter}){{{min_v}}}.*$',
    )
    return bool(regex.match(password))


def count() -> int:
    total = 0
    template = r'(?P<min_v>\d+)-(?P<max_v>\d+) (?P<letter>\w{1}): (?P<password>\w+)'
    with Path('./input.txt').open() as input_file:
        for line in input_file.read().splitlines():
            password = re.match(template, line)
            total += test_password(**password.groupdict())
    return total


if __name__ == '__main__':
    total = count()
    sys.stdout.write(f'Total: {total}\n')
