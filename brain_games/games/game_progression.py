import brain_games.cli
import random
from brain_games.games.communication_with_users import user_answer, check_user_ansver_and_print_res

LOWER_LIMIT_LENGTH_PROGRESSION = 5
UPPER_LIMIT_LENGTH_PROGRESSION = 10
MAX_START_NUMBER = 10
MAX_STEP = 5


def progression():
    user_name = brain_games.cli.welcome_user()
    print('What number is missing in the progression?')

    i = 0
    flag = True
    while i < 3 and flag:
        length_progression = random.randint(LOWER_LIMIT_LENGTH_PROGRESSION,
                                            UPPER_LIMIT_LENGTH_PROGRESSION)

        start_number = random.randint(0, MAX_START_NUMBER)
        step = random.randint(1, MAX_STEP)
        end_number = start_number + step * (length_progression - 1)

        progression_list = [str(i) for i in range(start_number, end_number + 1, step)]
        hidden_index = random.randint(0, length_progression - 1)
        result = progression_list[hidden_index]
        progression_list[hidden_index] = '..'

        question_str = ' '.join(progression_list)
        answer = user_answer(f'Question: {question_str}')
        flag = check_user_ansver_and_print_res(user_name, result, answer)
        i += 1
