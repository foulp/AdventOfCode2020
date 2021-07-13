from pathlib import Path

PREAMBLE_SIZE = 25


class XMAS:
    def __init__(self, n, series):
        self.length = n
        self.numbers = series

    def is_correct_sum(self, i):
        preamble = sorted(self.numbers[i-self.length: i])
        start = 0
        end = int(self.length) - 1
        while preamble[start] + preamble[end] != self.numbers[i]:
            if preamble[start] + preamble[end] > self.numbers[i]:
                end -= 1
            else:
                start += 1
            if start == end:
                return False
        return True

    def find_first_outlier(self):
        i = int(self.length)
        while self.is_correct_sum(i):
            i += 1
        return self.numbers[i]

    def find_encryption_weakness(self, invalid):
        start = 0
        end = 2
        tmp_sum = sum(self.numbers[start: end])
        while tmp_sum != invalid:
            if tmp_sum < invalid:
                end += 1
            else:
                start += 1
            tmp_sum = sum(self.numbers[start: end])
        return min(self.numbers[start: end]) + max(self.numbers[start: end])


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        numbers = list(map(int, f.read().split('\n')))

    xmas = XMAS(PREAMBLE_SIZE, numbers)
    invalid_number = xmas.find_first_outlier()
    print(f"The result of first star is {invalid_number}")

    print(f"The result of second star is {xmas.find_encryption_weakness(invalid_number)}")
