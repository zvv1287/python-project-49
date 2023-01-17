import random
from brain_games.games.game import main as games_main


def logic_of_game():
    number = random.randint(0, 100)
    print(f'Question: {number}')
    for i in range(2, number // 2):
        if number % i == 0:
            return 'no'
    return 'yes'


message = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    games_main(message=message, logic_of_game=logic_of_game)


if __name__ == '__main__':
    main()
