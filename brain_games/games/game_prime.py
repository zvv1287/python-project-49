import brain_games.cli
import random
from brain_games.games.communication_with_users import user_answer, check_user_ansver_and_print_res

LOWER_LIMIT = 2
UPPER_LIMIT = 10


def prime():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    flag = True
    while i < 3 and flag:
        number = (random.randint(LOWER_LIMIT, UPPER_LIMIT))
        result = 'yes'
        for n in range(2, number // 2 + 1):
            if number % n == 0:
                result = 'no'
                break

        answer = user_answer(f'Question: {number}')
        flag = check_user_ansver_and_print_res(user_name, result, answer)
        i += 1
