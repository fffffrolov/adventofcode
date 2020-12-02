import sys
from pathlib import Path
from typing import List, Optional



def get_input_data() -> List[str]:
    with Path('./input.txt').open() as input_file:
        return input_file.read().splitlines()


def calculate(lines) -> Optional[int]:
    data = {}
    for line in lines:
        el = int(line)
        if data.get(el):
            return data[el] * el
        data[2020 - int(el)] = el


def main():
    data = get_input_data()
    result = calculate(data)
    if result is None:
        sys.stdout.write('Oh now! There is no result!\n')
    sys.stdout.write(f'resilt is \n{result}\n')


if __name__ == '__main__':
    main()
