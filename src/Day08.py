from pathlib import Path


class HandheldGameConsole:
    def __init__(self, instructions, starting_acc=0):
        self.instructions = [i.split() for i in instructions]
        self.pointer = 0
        self.accumulator = starting_acc

    def acc(self, n):
        self.accumulator += n
        self.pointer += 1

    def jmp(self, offset):
        self.pointer += offset

    def nop(self, value):
        self.pointer += 1

    def clean(self):
        self.pointer = 0
        self.accumulator = 0

    def run(self):
        visited = set()
        while self.pointer not in visited:
            visited.add(self.pointer)
            operation, value = self.instructions[self.pointer]
            method = getattr(self, operation)
            method(int(value))

            if self.pointer >= len(self.instructions):
                return True, self.accumulator

        return False, self.accumulator

    def decorrupt(self):
        for i, (op, v) in enumerate(self.instructions):
            if op in ('jmp', 'op'):
                if op == 'jmp':
                    self.instructions[i][0] = 'nop'
                else:
                    self.instructions[i][0] = 'jmp'
                is_finite, acc = self.run()
                self.instructions[i][0] = op
                if is_finite:
                    return acc
                self.clean()


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        rules = f.read().split('\n')

    hgc = HandheldGameConsole(rules)
    print(f"The result of first star is {hgc.run()[1]}")

    print(f"The result of second star is {hgc.decorrupt()}")
