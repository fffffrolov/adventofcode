import re
import sys
from pathlib import Path
from typing import List, Optional


def test_password(password: str, letter: str, min_v: str, max_v: str) -> bool:
    regex = re.compile(f'^(?!(.*{letter}){{{int(max_v) + 1}}})(.*{letter}){{{min_v}}}.*$')
    return True if regex.match(password) else False


def count() -> int:
    total = 0
    with Path('./input.txt').open() as input_file:
        for line in input_file.read().splitlines():
            data = re.match(r'(?P<min_v>\d+)-(?P<max_v>\d+) (?P<letter>\w{1}): (?P<password>\w+)', line) 
            total += test_password(**data.groupdict())
    return total
        
    
def main():
    total = count()
    sys.stdout.write(f'Total: {total}\n')


if __name__ == '__main__':
    main()
