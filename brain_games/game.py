import brain_games.cli
import random

'''
brain-calc

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
'''


def user_answer(question):
    print(question)
    answer = input('Your answer: ')
    return answer


def check_user_ansver(name, result, answer):
    if result == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")


def even():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    flag = True
    while i < 3 and flag:
        number = random.randint(1, 1000)
        result = 'yes' if number % 2 == 0 else 'no'

        answer = user_answer(f'Question: {number}')
        flag = check_user_ansver(user_name, result, answer)
        i += 1


def calc():
    user_name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    i = 0
    flag = True
    while i < 3 and flag:
        number_1, number_2 = random.randint(1, 10), random.randint(1, 10)
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
        flag = check_user_ansver(user_name, result, answer)
        i += 1
