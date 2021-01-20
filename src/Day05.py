from pathlib import Path


def seat_id(boarding):
    row = boarding[:7]
    column = boarding[-3:]
    return int(row, 2) * 8 + int(column, 2)


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        passes = f.read()

    replace = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}
    for key in replace:
        passes = passes.replace(key, replace[key])
    passes = passes.split('\n')

    seat_ids = list(map(seat_id, passes))
    print(f"The result of first star is {max(seat_ids)}")

    m = max(seat_ids)
    n = min(seat_ids)
    theoric_sum = m*(m+1)/2 - n*(n-1)/2
    print(f"The result of second star is {theoric_sum - sum(seat_ids)}")
