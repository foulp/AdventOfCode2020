MODULO = 20201227
STARTING_NUMBER = 7

CARD_KEY = 8252394
DOOR_KEY = 6269621


def transform_subject_number(n, loop_size):
    return pow(n, loop_size, MODULO)


if __name__ == '__main__':
    card_loop_size = 1
    while transform_subject_number(STARTING_NUMBER, card_loop_size) != CARD_KEY:
        card_loop_size += 1

    door_loop_size = 1
    while transform_subject_number(STARTING_NUMBER, door_loop_size) != DOOR_KEY:
        door_loop_size += 1

    print(f"The result of first star is {transform_subject_number(CARD_KEY, door_loop_size)}.")
    print(f"The result of second star is {0}.")
