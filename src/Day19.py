import re
from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        rules, messages = f.read().split('\n\n')
    rules = {int(line.split(':')[0].strip()): [r.strip('" ').split() for r in line.split(':')[1].strip().split('|')] for line in rules.split('\n')}
    messages = messages.split('\n')

    regex = {n: rules[n][0][0] for n in rules if len(rules[n]) == 1 and len(rules[n][0]) == 1 and rules[n][0][0].isalpha()}
    to_update = []
    for n in regex:
        to_update.append(n)
        rules.pop(n)

    while to_update:
        n = to_update.pop()
        tmp = []
        for r in rules:
            for l in rules[r]:
                while str(n) in l:
                    l[l.index(str(n))] = f"({regex[n]})"

            if all(re.match(r'[a-z\|\(\)]+', ll) for l in rules[r] for ll in l):
                step = [f"({''.join(ll for ll in l)})" for l in rules[r]]
                regex[r] = f"{'|'.join(step)}"
                tmp.append(r)
        to_update.extend(tmp)
        for r in tmp:
            rules.pop(r)

    print(f"The result of first star is {sum(re.fullmatch(regex[0], msg) is not None for msg in messages)}.")
    print(f"The result of second star is {0}.")
