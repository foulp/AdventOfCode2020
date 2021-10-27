import re
from collections import defaultdict
import numpy as np
from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        tiles = f.read().replace('#', '1').replace('.', '0').split('\n\n')

    grid_shape = int(len(tiles) ** 0.5)
    tiles_shape = (tiles[0].count('\n') - 2, tiles[0][::-1].index('\n') - 2)

    tiles = {
        int(tile.split('\n')[0][5:-1]):
            np.array([list(map(int, line)) for line in tile.split('\n')[1:]])
        for tile in tiles
    }

    neighbors = defaultdict(lambda: {})
    to_update = set(list(tiles.keys())[:1])
    updated = set()
    corners = 1
    while to_update:
        n = to_update.pop()
        if len(neighbors[n]) == 4:
            updated.add(n)
            continue

        tile = tiles[n]
        for m, tile_bis in tiles.items():
            if m == n:
                continue

            if np.array_equal(tile[0], tile_bis[0]):
                tiles[m] = np.flipud(tiles[m])
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[-1]):
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[:, 0]):
                tiles[m] = np.rot90(tiles[m], k=1)
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[:, -1]):
                tiles[m] = np.rot90(np.fliplr(tiles[m]), k=1)
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[0][::-1]):
                tiles[m] = np.rot90(tiles[m], k=2)
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[-1][::-1]):
                tiles[m] = np.fliplr(tiles[m])
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[:, 0][::-1]):
                tiles[m] = np.fliplr(np.rot90(tiles[m], k=1))
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[0], tile_bis[:, -1][::-1]):
                tiles[m] = np.rot90(tiles[m], k=-1)
                neighbors[n]['over'] = m
                neighbors[m]['under'] = n
            elif np.array_equal(tile[-1], tile_bis[0]):
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[-1]):
                tiles[m] = np.flipud(tiles[m])
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[:, 0]):
                tiles[m] = np.rot90(np.flipud(tiles[m]), k=-1)
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[:, -1]):
                tiles[m] = np.rot90(tiles[m], k=1)
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[0][::-1]):
                tiles[m] = np.fliplr(tiles[m])
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[-1][::-1]):
                tiles[m] = np.rot90(tiles[m], k=2)
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[:, 0][::-1]):
                tiles[m] = np.rot90(tiles[m], k=-1)
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[-1], tile_bis[:, -1][::-1]):
                tiles[m] = np.rot90(np.fliplr(tiles[m]), k=-1)
                neighbors[n]['under'] = m
                neighbors[m]['over'] = n
            elif np.array_equal(tile[:, 0], tile_bis[0]):
                tiles[m] = np.rot90(tiles[m], k=-1)
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[-1]):
                tiles[m] = np.rot90(np.flipud(tiles[m]), k=-1)
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[:, 0]):
                tiles[m] = np.fliplr(tiles[m])
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[:, -1]):
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[0][::-1]):
                tiles[m] = np.rot90(np.fliplr(tiles[m]), k=-1)
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[-1][::-1]):
                tiles[m] = np.rot90(tiles[m], k=1)
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[:, 0][::-1]):
                tiles[m] = np.rot90(tiles[m], k=2)
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, 0], tile_bis[:, -1][::-1]):
                tiles[m] = np.flipud(tiles[m])
                neighbors[n]['left'] = m
                neighbors[m]['right'] = n
            elif np.array_equal(tile[:, -1], tile_bis[0]):
                tiles[m] = np.rot90(np.flipud(tiles[m]), k=-1)
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[-1]):
                tiles[m] = np.rot90(tiles[m], k=-1)
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[:, 0]):
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[:, -1]):
                tiles[m] = np.fliplr(tiles[m])
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[0][::-1]):
                tiles[m] = np.rot90(tiles[m], k=1)
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[-1][::-1]):
                tiles[m] = np.flipud(np.rot90(tiles[m], k=-1))
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[:, 0][::-1]):
                tiles[m] = np.flipud(tiles[m])
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            elif np.array_equal(tile[:, -1], tile_bis[:, -1][::-1]):
                tiles[m] = np.rot90(tiles[m], k=2)
                neighbors[n]['right'] = m
                neighbors[m]['left'] = n
            else:
                continue

            if m not in updated:
                to_update.add(m)
            if len(neighbors[n]) == 4:
                updated.add(n)
                break
        updated.add(n)
        if len(neighbors[n]) == 2:
            corners *= n
    print(f"The result of first star is {corners}.")

    grid = np.zeros((grid_shape * tiles_shape[0], grid_shape * tiles_shape[1]), dtype=int)
    start = next(n for n in neighbors if len(neighbors[n]) == 2 and 'under' in neighbors[n] and 'right' in neighbors[n])
    for i in range(grid_shape):
        current = start
        for j in range(grid_shape):
            grid[tiles_shape[0]*j:tiles_shape[0]*(j+1), tiles_shape[1]*i:tiles_shape[1]*(i+1)] = tiles[current][1:-1, 1:-1]
            if j < grid_shape - 1:
                current = neighbors[current]['under']
        if i < grid_shape - 1:
            start = neighbors[start]['right']

    regex = [r'[01]{18}1[01]', r'(?:1[01]{4}1){3}1{2}', r'[01](?:1[01]{2}){6}[01]']
    regex = fr'[0\n1]{"{"}{grid_shape * tiles_shape[1] + 1 - 20}{"}"}'.join(regex)
    regex_length = 2 * (grid_shape * tiles_shape[1] + 1 - 20) + 60

    for _ in range(4):
        for _ in range(2):
            string_grid = '\n'.join(''.join(line.astype(str)) for line in grid)
            match = [re.match(regex, string_grid[i: i+regex_length]) is not None for i in range(len(string_grid) - regex_length + 1)]
            if sum(match):
                print(f"The result of second star is {np.count_nonzero(grid==1) - sum(match) * 15}.")
                break
            grid = np.rot90(grid)
        grid = np.fliplr(grid)
