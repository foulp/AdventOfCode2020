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


def filling_seats_view(arr):
    empty_seats = (arr == 'L').nonzero()
    occupied_seats = (arr == '#').nonzero()
    changes = {}
    views_occ = {(i, j): 0 for i in range(arr.shape[0]) for j in range(arr.shape[1])}

    for x, y in zip(*occupied_seats):
        k = next((j for j in range(1, arr.shape[1]-y) if arr[x, y+j] in 'L#'), 0)
        if k:
            views_occ[(x, y+k)] += 1
        k = next((j for j in range(1, y+1) if arr[x, y-j] in 'L#'), 0)
        if k:
            views_occ[(x, y-k)] += 1
        k = next((i for i in range(1, arr.shape[0]-x) if arr[x+i, y] in 'L#'), 0)
        if k:
            views_occ[(x+k, y)] += 1
        k = next((i for i in range(1, x+1) if arr[x-i, y] in 'L#'), 0)
        if k:
            views_occ[(x-k, y)] += 1
        k = next((k for k in range(1, min(arr.shape[0]-x, arr.shape[1]-y)) if arr[x+k, y+k] in 'L#'), 0)
        if k:
            views_occ[(x+k, y+k)] += 1
        k = next((k for k in range(1, min(x+1, y+1)) if arr[x-k, y-k] in 'L#'), 0)
        if k:
            views_occ[(x-k, y-k)] += 1
        k = next((k for k in range(1, min(arr.shape[0]-x, y+1)) if arr[x+k, y-k] in 'L#'), 0)
        if k:
            views_occ[(x+k, y-k)] += 1
        k = next((k for k in range(1, min(x+1, arr.shape[1]-y)) if arr[x-k, y+k] in 'L#'), 0)
        if k:
            views_occ[(x-k, y+k)] += 1

    for x, y in zip(*occupied_seats):
        if views_occ[(x, y)] >= 5:
            changes[(x, y)] = 'L'
    for x, y in zip(*empty_seats):
        if views_occ[(x, y)] == 0:
            changes[(x, y)] = '#'

    if len(changes) == 0:
        return False

    for x, y in changes:
        arr[x, y] = changes[(x, y)]
    return True


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        seats = np.array([list(line) for line in f.read().split('\n')])
        seats_view = np.array(seats)

    loops = 0
    while filling_seats(seats):
        loops += 1

    print(f"The result of first star is {(seats == '#').sum()} ({loops}).")

    loops = 0
    while filling_seats_view(seats_view):
        loops += 1

    print(f"The result of second star is {(seats_view == '#').sum()} ({loops})")
