def user_answer(question):
    print(question)
    answer = input('Your answer: ')
    return answer


def check_user_ansver_and_print_res(name, result, answer):
    if str(result) == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
