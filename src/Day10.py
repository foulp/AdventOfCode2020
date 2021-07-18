from pathlib import Path


def count_distr(values):
    c = 0
    for binary in range(2 ** len(values)):
        fine = True
        prev = values[0] - 1
        binary = bin(binary)[2:]
        binary = '0' * (len(values) - len(binary)) + binary
        for k, j in enumerate(binary):
            if j == '1':
                if values[k] - prev > 3:
                    fine = False
                    break
                prev = values[k]
        if fine and (values[-1] + 1 - prev) <= 3:
            c += 1
    return c


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        jolts = sorted(list(map(int, f.read().split('\n'))))

    c1 = 1 if jolts[0] == 1 else 0
    c2 = 1 if jolts[0] == 2 else 0
    c3 = 2 if jolts[0] == 3 else 1
    for i, v in enumerate(jolts[:-1]):
        if jolts[i+1] - v == 3:
            c3 += 1
        elif jolts[i+1] - v == 1:
            c1 += 1
    print(f"The result of first star is {c1 * c3}. FYI (c1, c2, c3) = {c1,c2,c3}")

    jolts = [0] + jolts + [jolts[-1] + 3]
    count = 1
    combo = {0: 1, 1: 1}
    series = 0
    i = 1
    while i < len(jolts):
        while jolts[i] - jolts[i-1] == 1:
            series += 1
            i += 1
        if series not in combo:
            combo[series] = count_distr(jolts[i-series:i-1])
        count *= combo[series]
        series = 0
        i += 1
    print(f"The result of second star is {count}")
