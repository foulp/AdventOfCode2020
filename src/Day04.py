from pathlib import Path
import re

REQUIRED = {'byr': r'19[2-9]\d|200[0-2]',
            'iyr': r'201\d|2020',
            'eyr': r'202\d|2030',
            'hgt': r'1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in',
            'hcl': r'#[\da-f]{6}',
            'ecl': r'amb|blu|brn|gry|grn|hzl|oth',
            'pid': r'\d{9}'}

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        passports = f.read().split('\n\n')

    passports = [{field.split(':')[0]: field.split(':')[1] for field in p.split()} for p in passports]

    print(f"The result of first star is {sum(1 for p in passports if all(field in p for field in REQUIRED))}")

    print(f"The result of second star is {sum(1 for p in passports if all(field in p and re.fullmatch(REQUIRED[field], p[field]) for field in REQUIRED))}")
