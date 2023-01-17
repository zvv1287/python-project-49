import random
from brain_games.games.game import main as games_main


def logic_of_game():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    print(f'Question: {number_1} {number_2}')

    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    return str(number_1 + number_2)


message = 'Find the greatest common divisor of given numbers.'


def main():
    games_main(message=message, logic_of_game=logic_of_game)


if __name__ == '__main__':
    main()
