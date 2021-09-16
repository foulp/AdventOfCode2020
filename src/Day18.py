from pathlib import Path
import re


def solve_short(string):
    values = string.split(' ')
    res = values.pop(0)
    while len(values):
        res = str(eval(res + values.pop(0) + values.pop(0)))
    return res


def solve_short_reverse(string):
    while '+' in string:
        string = re.sub(r'(\d+ \+ \d+)', lambda x: str(eval(x.group(1))), string)
    return str(eval(string))


def solve(expr, reverse=False):
    pattern = r'\(([^\(\)]+)\)'
    while '(' in expr:
        if not reverse:
            expr = re.sub(pattern, lambda x: solve_short(x.group(1)), expr)
        else:
            expr = re.sub(pattern, lambda x: solve_short_reverse(x.group(1)), expr)
    if not reverse:
        return int(solve_short(expr))
    else:
        return int(solve_short_reverse(expr))


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        expressions = f.read().split('\n')

    print(f"The result of first star is {sum(solve(e) for e in expressions)}.")
    print(f"The result of second star is {sum(solve(e, reverse=True) for e in expressions)}.")
