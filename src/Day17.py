from collections import defaultdict
import itertools
from pathlib import Path

N_CYCLES = 6


def simulate_grid(grid, n_cycles, n_dims):
    grid = {
        (int(i), int(j)) + (0,)*(n_dims-2)
        for i, line in enumerate(grid) for j, cell in enumerate(line)
        if cell == '1'}

    for n in range(n_cycles):
        new_grid = set()
        neighbors = defaultdict(lambda: 0)
        for active_cube in grid:
            current_neighbors = -1
            for delta in itertools.product(range(-1, 2), repeat=n_dims):
                coord = tuple(map(sum, zip(active_cube, delta)))
                neighbors[coord] += 1
                if coord in grid:
                    current_neighbors += 1
            neighbors[active_cube] -= 1
            if current_neighbors in (2, 3):
                new_grid.add(active_cube)

        for neighbor in neighbors:
            if neighbors[neighbor] == 3:
                new_grid.add(neighbor)
        grid = set(new_grid)
    return grid


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        layer = f.read()
        layer = layer.replace('.', '0').replace('#', '1').split('\n')

    print(f"The result of first star is {len(simulate_grid(layer, N_CYCLES, 3))}.")
    print(f"The result of second star is {len(simulate_grid(layer, N_CYCLES, 4))}.")
