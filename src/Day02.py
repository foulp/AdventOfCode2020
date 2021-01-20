from pathlib import Path


def extract_pwd(string):
    regex, pwd = string.split(": ")
    nb, letter = regex.split()
    i, j = map(int, nb.split("-"))
    return i, j, letter, pwd


def is_pwd_valid(string, star):
    i, j, letter, pwd = string
    if star == 'first':
        return i <= pwd.count(letter) <= j
    else:
        return (pwd[i-1] == letter) + (pwd[j-1] == letter) == 1


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        passwords = f.read().split('\n')

    passwords = [extract_pwd(pw) for pw in passwords]

    print(f"The result of first star is {sum(map(lambda x: is_pwd_valid(x, 'first'), passwords))}")
    print(f"The result of second star is {sum(map(lambda x: is_pwd_valid(x, 'second'), passwords))}")
