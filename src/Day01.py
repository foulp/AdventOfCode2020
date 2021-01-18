from pathlib import Path

TARGET = 2020

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        numbers = list(map(int, f.read().split('\n')))

    for n in numbers:
        if (TARGET - n) in numbers:
            print(f"The result of first star is {n * (TARGET - n)}")
            break

    found = False
    for i, n in enumerate(numbers):
        for m in numbers[i:]:
            if (TARGET - n - m) in numbers:
                print(f"The result of second star is {n * m * (TARGET - n - m)}")
                found = True
                break
            if found:
                break
