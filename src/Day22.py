from pathlib import Path


class Combat:
    def __init__(self, deck1, deck2, recursive=False):
        self.d1 = deck1
        self.d2 = deck2
        self.recursive = recursive
        if recursive:
            self.hd1 = set()
            self.hd2 = set()

    def _draw_cards(self):
        c1 = self.d1.pop(0)
        c2 = self.d2.pop(0)
        return c1, c2

    def _round_winner(self, c1, c2):
        if self.recursive:
            if len(self.d1) >= c1 and len(self.d2) >= c2:
                return Combat(list(self.d1[:c1]), list(self.d2[:c2]), recursive=True)._game_winner()

        return (c2 > c1) + 1

    def _game_winner(self):
        while len(self.d1) * len(self.d2):
            if self.recursive:
                str_d1 = ''.join(map(str, self.d1))
                str_d2 = ''.join(map(str, self.d2))
                if str_d1 in self.hd1 or str_d2 in self.hd2:
                    return 1
                self.hd1.add(str_d1)
                self.hd2.add(str_d2)

            c1, c2 = self._draw_cards()
            round_winner = self._round_winner(c1, c2)
            if round_winner == 1:
                self.d1.extend((c1, c2))
            else:
                self.d2.extend((c2, c1))

        return 1 if len(self.d1) else 2

    def run(self):
        winner = self._game_winner()
        return self._winning_score(self.d1 if winner == 1 else self.d2)

    @staticmethod
    def _deck_score(deck):
        return sum(c * (i + 1) for i, c in enumerate(deck[::-1]))

    def _winning_score(self, deck):
        return self._deck_score(deck)


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        d1, d2 = f.read().split('\n\n')

    d1 = list(map(int, d1.split('\n')[1:]))
    d2 = list(map(int, d2.split('\n')[1:]))
    print(f"The result of first star is {Combat(list(d1), list(d2)).run()}.")

    print(f"The result of second star is {Combat(list(d1), list(d2), recursive=True).run()}.")
