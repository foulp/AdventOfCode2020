from pathlib import Path

N = 2020


class Memory:
    def __init__(self, numbers):
        self.spoken = {n: i+1 for i, n in enumerate(numbers[:-1])}
        self.last = numbers[-1]
        self.count = len(numbers)

    def turn(self):
        if self.last in self.spoken:
            spoken_number = self.count - self.spoken[self.last]
        else:
            spoken_number = 0
        self.spoken[self.last] = self.count
        self.last = spoken_number
        self.count += 1

    def run(self, n_turn):
        while self.count < n_turn:
            self.turn()
        return self.last


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        starting_numbers = list(map(int, f.read().split(',')))

    memory = Memory(starting_numbers)
    print(f"The result of first star is {memory.run(2020)}.")
    print(f"The result of second star is {memory.run(30000000)}.")
