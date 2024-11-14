import brain_games.cli
from brain_games.games.communication_with_users import user_answer, check_user_ansver_and_print_res
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 10


def calc():
    user_name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    i = 0
    flag = True
    while i < 3 and flag:
        number_1, number_2 = (random.randint(LOWER_LIMIT, UPPER_LIMIT),
                              random.randint(LOWER_LIMIT, UPPER_LIMIT))
        sign = random.choice(['+', '-', '*'])
        match sign:
            case '+':
                result = number_1 + number_2
            case '-':
                result = number_1 - number_2
            case '*':
                result = number_1 * number_2
        result = str(result)
        answer = user_answer(f'Question: {number_1} {sign} {number_2}')
        flag = check_user_ansver_and_print_res(user_name, result, answer)
        i += 1

