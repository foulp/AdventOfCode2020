from pathlib import Path

ALPHA = 'azertyuiopqsdfghjklmwxcvbn'

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        groups = f.read().split('\n\n')

    value = sum(len(set(g)) - ('\n' in g) for g in groups)
    print(f"The result of first star is {value}")

    value = sum(sum(1 for char in ALPHA if g.count(char) == g.count('\n')+1)for g in groups)
    print(f"The result of second star is {value}")
