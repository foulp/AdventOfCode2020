import math
from pathlib import Path

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        rules, ticket, nearby_tickets = f.read().split('\n\n')

    rules = map(lambda x: x.split(': '), rules.split('\n'))
    rules = {name: [list(map(int, rng.split('-'))) for rng in values.split(' or ')] for name, values in rules}

    ticket = list(map(int, ticket.split('\n')[1].split(',')))

    nearby_tickets = [list(map(int, t.split(','))) for t in nearby_tickets.split('\n')[1:]]

    valid_fields = {name: list(range(len(ticket))) for name in rules}
    error_rate = 0
    for t in nearby_tickets:
        kept = True
        for value in t:
            if all(all(value not in range(a, b + 1) for a, b in rule_ranges) for rule_ranges in rules.values()):
                error_rate += value
                kept = False
                break
        if kept:
            for i, value in enumerate(t):
                for name in rules:
                    rule_ranges = rules[name]
                    if all(value not in range(a, b+1) for a, b in rule_ranges):
                        valid_fields[name].remove(i)

    to_remove = [valid_fields[name][0] for name in valid_fields if len(valid_fields[name]) == 1]
    removed = []
    while to_remove:
        field = to_remove.pop()
        removed.append(field)
        for name in valid_fields:
            if field in valid_fields[name] and len(valid_fields[name]) > 1:
                valid_fields[name].remove(field)
            if len(valid_fields[name]) == 1 and valid_fields[name][0] not in removed:
                to_remove.append(valid_fields[name][0])

    print(f"The result of first star is {error_rate}.")
    print(f"The result of second star is {math.prod([ticket[valid_fields[name][0]] for name in valid_fields if name.startswith('departure')])}.")
