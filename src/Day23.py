from pathlib import Path


class CrabCups:
    def __init__(self, cups, n=None):
        self.cups = {c: cups[(i+1) % len(cups)] for i, c in enumerate(cups)}
        self.current = cups[0]
        if n:
            self.cups.update({i: i+1 for i in range(max(cups) + 1, n)})
            self.cups[n] = cups[0]
            self.cups[cups[-1]] = max(cups) + 1
            self.full_len = n
        else:
            self.full_len = len(cups)

    def _round(self):
        b = self.cups[self.current]
        c = self.cups[b]
        d = self.cups[c]
        dest = (self.current - 2) % self.full_len + 1
        while dest in (b, c, d):
            dest = (dest - 2) % self.full_len + 1
        self.cups[self.current] = self.cups[d]
        self.cups[d] = self.cups[dest]
        self.cups[dest] = b
        self.current = self.cups[self.current]

    def run(self, n):
        for i in range(n):
            self._round()
        return self.cups


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        cups_list = list(map(int, f.read()))
    game = CrabCups(list(cups_list)).run(100)
    res = ''
    current = game[1]
    for _ in range(len(game) - 1):
        res += f'{current}'
        current = game[current]
    print(f"The result of first star is {res}.")

    game = CrabCups(list(cups_list), 1000000).run(10000000)
    print(f"The result of second star is {game[1] * game[game[1]]}.")
