import brain_games.cli
import random
from brain_games.games.communication_with_users import user_answer, check_user_ansver_and_print_res


def even():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    flag = True
    while i < 3 and flag:
        number = random.randint(1, 1000)
        result = 'yes' if number % 2 == 0 else 'no'

        answer = user_answer(f'Question: {number}')
        flag = check_user_ansver_and_print_res(user_name, result, answer)
        i += 1
