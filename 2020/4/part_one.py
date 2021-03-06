import sys
from pathlib import Path


def is_passport_valid(passport: str) -> bool:
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid', 'ecl')
    for key in required_keys:
        if f'{key}:' not in passport:
            return False
    return True


def scanner() -> int:
    valid_passports = 0
    passport = ''

    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            line = line.strip()
            passport += line + ' '

            if not line:
                if is_passport_valid(passport):
                    valid_passports += 1
                passport = ''

        # check last passport
        if is_passport_valid(passport):
            valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    result = scanner()
    sys.stdout.write(f'Valid: {result}\n')
