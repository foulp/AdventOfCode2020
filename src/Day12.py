from pathlib import Path


def ship_mvmts(instructions, waypoint=False):
    pos_x, pos_y, direction = 0, 0, 90
    w_x, w_y = 10, 1
    movements = {
        'N': lambda x, y, d, v: (x, y+v, d),
        'S': lambda x, y, d, v: (x, y-v, d),
        'E': lambda x, y, d, v: (x+v, y, d),
        'W': lambda x, y, d, v: (x-v, y, d),
        'L': lambda x, y, d, v: (x, y, (d-v) % 360) if not waypoint else (-y, x, d) if v == 90 else (-x, -y, d) if v == 180 else (y, -x, d),
        'R': lambda x, y, d, v: (x, y, (d+v) % 360) if not waypoint else (y, -x, d) if v == 90 else (-x, -y, d) if v == 180 else (-y, x, d),
        'F': lambda x, y, d, v:
            movements['N'](x, y, d, v) if d == 0
            else movements['E'](x, y, d, v) if d == 90
            else movements['S'](x, y, d, v) if d == 180
            else movements['W'](x, y, d, v)
    }
    for i in instructions:
        m = i[0]
        value = int(i[1:])
        if not waypoint:
            pos_x, pos_y, direction = movements[m](pos_x, pos_y, direction, value)
        else:
            if m != 'F':
                w_x, w_y, _ = movements[m](w_x, w_y, 0, value)
            else:
                pos_x += (value * w_x)
                pos_y += (value * w_y)
    return pos_x, pos_y, direction


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        commands = f.read().split('\n')

    end_x, end_y, _ = ship_mvmts(commands)
    print(f"The result of first star is {abs(end_x) + abs(end_y)}.")

    end_x, end_y, _ = ship_mvmts(commands, waypoint=True)
    print(f"The result of second star is {abs(end_x) + abs(end_y)}.")
