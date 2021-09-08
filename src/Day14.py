import numpy as np
from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        program = f.read().split('\n')

    memories_first = {}
    memories_second = {}
    bitmask = np.array(['X'] * 36)
    for line in program:
        if line.startswith('mask'):
            bitmask = np.array(list(line[-36:]))
            continue

        place, value = map(int, line[4:].split('] = '))

        value_first = np.array(list(f'{value:036b}'))
        value_first = np.where(bitmask == 'X', value_first, bitmask)
        memories_first[place] = int(''.join(value_first), 2)

        place_second = np.array(list(f'{place:036b}'))
        place_second = np.where(bitmask == '0', place_second, bitmask)
        rnd = np.nonzero(place_second == 'X')[0]
        for k in range(2 ** rnd.shape[0]):
            place_second[rnd] = list(f"{k:0{rnd.shape[0]}b}")
            memories_second[int(''.join(place_second), 2)] = value

    print(f"The result of first star is {sum(memories_first[key] for key in memories_first)}.")
    print(f"The result of second star is {sum(memories_second[key] for key in memories_second)}.")
