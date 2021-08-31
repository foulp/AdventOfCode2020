import numpy as np
from pathlib import Path


def filling_seats(arr):
    empty_seats = (arr == 'L').nonzero()
    occupied_seats = (arr == '#').nonzero()
    changes = {}
    for x, y in zip(*empty_seats):
        if (arr[max(0, x-1): min(arr.shape[0], x+2), max(0, y-1): min(arr.shape[1], y+2)] != '#').all():
            changes[(x, y)] = '#'
    for x, y in zip(*occupied_seats):
        if (arr[max(0, x-1): min(arr.shape[0], x+2), max(0, y-1): min(arr.shape[1], y+2)] == '#').sum() >= 5:
            changes[(x, y)] = 'L'

    if len(changes) == 0:
        return False

    for x, y in changes:
        arr[x, y] = changes[(x, y)]
    return True


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        seats = np.array([list(line) for line in f.read().split('\n')])

    loops = 0
    while filling_seats(seats):
        loops += 1

    print(f"The result of first star is {(seats == '#').sum()} ({loops}).")

    print(f"The result of second star is {0}")
