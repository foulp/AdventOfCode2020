from collections import deque
from pathlib import Path


class CrabCups:
    def __init__(self, cups):
        self.cups = deque(cups)
        self.current = cups[0]

    def _round(self):
        self.cups.rotate(-self.cups.index(self.current) - 1)
        picked_up = [self.cups.popleft() for _ in range(3)]
        destination = self._find_destination()
        for i, value in enumerate(picked_up):
            self.cups.insert(destination + i + 1, value)
        self.current = self.cups[(self.cups.index(self.current) + 1) % len(self.cups)]

    def ending_labels(self, n, level=1):
        for i in range(n):
            self._round()
        self.cups.rotate(-self.cups.index(1))
        self.cups.popleft()
        if level == 1:
            return ''.join(map(str, self.cups))
        else:
            return self.cups[0] * self.cups[1]

    def _find_destination(self):
        label = next((i for i in range(self.current-1, 0, -1) if i in self.cups), max(self.cups))
        return self.cups.index(label)


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        cups = list(map(int, f.read()))

    print(f"The result of first star is {CrabCups(list(cups)).ending_labels(100)}.")

    cups.extend(range(max(cups) + 1, 1000001))
    print(f"The result of second star is {CrabCups(list(cups)).ending_labels(10000000)}.")
