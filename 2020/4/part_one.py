import sys
from pathlib import Path


def scanners() -> int:
    def count_valid():
        nonlocal valid_passports
        is_valid = len(current_passport_keys) == len(required_keys)
        if is_valid:
            valid_passports += 1

    valid_passports = 0
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid', 'ecl')
    current_passport_keys = set()

    with Path('./input.txt').open() as input_file:
        for line in input_file.readlines():
            
            for key in required_keys: 
                if f'{key}:' in line: 
                    current_passport_keys.add(key)
            
            if line == '\n':
                count_valid()
                current_passport_keys = set()
        
        # check last passport
        count_valid()

    return valid_passports


if __name__ == '__main__':
    result = scanners()
    sys.stdout.write(f'Valid: {result}\n')
