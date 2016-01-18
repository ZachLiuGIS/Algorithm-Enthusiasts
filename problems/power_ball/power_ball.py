import random


WHITE_BALLS = {4, 8, 19, 27, 34}
RED_BALL = 10


def generate_winning_numbers():
    white_numbers = set(random.sample(range(1, 70), 5))
    red_number = random.choice(range(1, 27))
    if white_numbers == WHITE_BALLS and red_number == RED_BALL:
        return True
    return False


def play():
    count = 0
    while not generate_winning_numbers():
        count += 1
    count += 1
    print("after {} numbers of tickets, you win the Powerball!".format(count))

if __name__ == '__main__':
    play()
