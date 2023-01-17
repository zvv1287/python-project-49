import random
from brain_games.games.game import main as games_main


def logic_of_game():
    number = random.randint(0, 1000)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    games_main(message=message, logic_of_game=logic_of_game)


message = 'Answer "yes" if the number is even, otherwise answer "no".'

if __name__ == '__main__':
    main()
