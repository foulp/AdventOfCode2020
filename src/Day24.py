from pathlib import Path

N_DAYS = 100
DIRECTIONS = ('ne', 'e', 'se', 'sw', 'w', 'nw')
MOVEMENTS = [
    lambda x, y: (x-1, y+1),
    lambda x, y: (x, y+2),
    lambda x, y: (x+1, y+1),
    lambda x, y: (x+1, y-1),
    lambda x, y: (x, y-2),
    lambda x, y: (x-1, y-1)
]
ADJACENTS = dict(zip(DIRECTIONS, MOVEMENTS))

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        paths = f.read().split('\n')

    flipped = []
    for path in paths:
        tile = (0, 0)
        path = list(path)
        while path:
            direction = path.pop(0)
            if direction in 'ns':
                direction += path.pop(0)

            tile = ADJACENTS[direction](tile[0], tile[1])

        flipped.append(tuple(tile))

    print(f"The result of first star is {2 * len(set(flipped)) - len(flipped)}.")

    flipped = set([tile for tile in flipped if flipped.count(tile) == 1])
    for i in range(N_DAYS):
        print(f'DAY {i} : {len(flipped)}')
        neighbors = {}
        for tile in flipped:
            for adj in ADJACENTS:
                n = ADJACENTS[adj](tile[0], tile[1])
                neighbors[n] = neighbors.get(n, 0) + 1
        blacks = set([tile for tile in set(neighbors.keys()) - flipped if neighbors[tile] == 2])
        blacks.update(tile for tile in flipped if neighbors.get(tile, 0) in (1, 2))
        flipped = set(blacks)

    print(f"The result of second star is {len(flipped)}.")
