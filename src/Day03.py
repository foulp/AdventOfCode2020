from pathlib import Path

STEEP_FIRST = (3, 1)
STEEPS_SECOND = [(1, 1), (5, 1), (7, 1), (1, 2)]


def trees_encountered(right, down):
    x = 0
    y = 0
    counter = 0
    while x < len(grid):
        counter += grid[x][y % len(grid[0])] == '#'
        x += down
        y += right
    return counter


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        grid = f.read().split('\n')

    trees = trees_encountered(*STEEP_FIRST)
    print(f"The result of first star is {trees}")

    for steep in STEEPS_SECOND:
        trees *= trees_encountered(*steep)
    print(f"The result of second star is {trees}")
