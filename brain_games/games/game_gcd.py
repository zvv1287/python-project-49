import brain_games.cli
import random
from brain_games.games.communication_with_users import user_answer, check_user_ansver_and_print_res

LOWER_LIMIT = 2
UPPER_LIMIT = 10


def gsd():
    user_name = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    flag = True
    while i < 3 and flag:
        number_1, number_2 = (random.randint(LOWER_LIMIT, UPPER_LIMIT),
                              random.randint(LOWER_LIMIT, UPPER_LIMIT))
        min_number = min(number_1, number_2)
        result = 'no'
        for n in range(2, min_number + 1):
            if number_1 % n == 0 and number_2 % n == 0:
                result = n

        answer = user_answer(f'Question: {number_1} {number_2}')
        flag = check_user_ansver_and_print_res(user_name, result, answer)
        i += 1
