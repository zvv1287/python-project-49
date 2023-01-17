import random
from brain_games.games.game import main as games_main


def logic_of_game():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    sign = random.choice(['+', '-', '*'])
    if sign == '+':
        true_answer = str(number_1 + number_2)
    elif sign == '-':
        true_answer = str(number_1 - number_2)
    else:
        true_answer = str(number_1 * number_2)
    print(f'Question: {number_1} {sign} {number_2}')
    return true_answer


def main():
    games_main(message=message, logic_of_game=logic_of_game)

message = 'What is the result of the expression?'

if __name__ == '__main__':
    main()
