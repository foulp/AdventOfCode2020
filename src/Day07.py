from pathlib import Path
import re

TARGET = 'shiny gold'


def n_bags(color, bagrules):
    if color[1] not in bagrules:
        return int(color[0])
    else:
        return int(color[0]) * (1 + sum(n_bags(bags, bagrules) for bags in bagrules[color[1]]))


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        rules = f.read().split('\n')

    bag_rules = {}
    bag_rules_inv = {}
    for r in rules:
        upper_bag, contained_bags = r.split('contain')
        upper_bag = re.search(r'(\w+ \w+) bags', upper_bag).group(1)
        contained_bags = re.findall(r'(\d+) (\w+ \w+) bags?', contained_bags)
        if len(contained_bags):
            bag_rules[upper_bag] = contained_bags
            for n, bag in contained_bags:
                if bag in bag_rules_inv:
                    bag_rules_inv[bag].add(upper_bag)
                else:
                    bag_rules_inv[bag] = {upper_bag}

    to_visit = set(bag_rules_inv[TARGET])
    visited = []
    value = set(to_visit)
    while to_visit:
        bag = to_visit.pop()
        if bag in visited:
            continue
        visited.append(bag)
        to_visit.update(bag_rules_inv.get(bag, []))
        value.update(bag_rules_inv.get(bag, []))
    print(f"The result of first star is {len(value)}")

    print(f"The result of second star is {n_bags((1, TARGET), bag_rules) - 1}")
