import itertools
import numpy as np
from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        timestamp, bus_lines = f.read().split('\n')

    bus_lines_filtered = filter(lambda b: b != 'x', bus_lines.split(','))
    departure, bus = min((int(line) - int(timestamp) % int(line), int(line)) for line in bus_lines_filtered)
    print(f"The result of first star is {departure * bus}.")

    bus_lines_ts = sorted([(int(line), (-i) % int(line)) for i, line in enumerate(bus_lines.split(',')) if line != 'x'], reverse=True)

    x = bus_lines_ts[0][1]
    n = bus_lines_ts[0][0]
    for bus, a in bus_lines_ts[1:]:
        while x % bus != a:
            x += n
        n *= bus

    print(f"The result of second star is {x}.")
