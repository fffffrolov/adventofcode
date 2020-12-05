import re
import sys
from pathlib import Path
from typing import Generator


class Validator:
    regex = None

    def __init__(self, passport: str):
        self.value = re.match(self.regex, passport)

    def __call__(self) -> bool:
        if self.value is None:
            return False
        return self.validate_value()

    def validate_value(self) -> bool:
        raise NotImplementedError()

    @classmethod
    def __all__subclasses__(cls) -> Generator:
        for subclass in cls.__subclasses__():
            yield from subclass.__all__subclasses__()
            yield subclass


class BirthYearValidator(Validator):
    regex = r'.*byr:(\d{4})\b'

    def validate_value(self):
        value = self.value.group(1)
        return 1920 <= int(value) <= 2002


class IssueYearValidator(Validator):
    regex = r'.*iyr:(\d{4})\b'

    def validate_value(self):
        value = self.value.group(1)
        return 2010 <= int(value) <= 2020


class ExpirationYearValidator(Validator):
    regex = r'.*eyr:(\d{4})\b'

    def validate_value(self):
        value = self.value.group(1)
        return 2020 <= int(value) <= 2030


class HeightValidator(Validator):
    regex = r'.*hgt:(\d+)(cm|in)\b'

    def validate_value(self):
        value = self.value.group(1)
        unit = self.value.group(2)
        if unit == 'cm':
            return 150 <= int(value) <= 193
        return 59 <= int(value) <= 76


class HairColorValidator(Validator):
    regex = r'.*hcl:#[a-f0-9]{6}\b'

    def validate_value(self):
        return True


class EyeColorValidator(Validator):
    regex = r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\b'

    def validate_value(self):
        return True


class PassportIDValidator(Validator):
    regex = r'.*pid:(\d{9})\b'

    def validate_value(self):
        return True


def is_passport_valid(passport: str) -> bool:
    for validator_class in Validator.__all__subclasses__():
        validator = validator_class(passport)
        if validator():
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
