import prompt
import random
from brain_games.scripts import brain_games


def main():
    user_name = brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(0, 1000)
        if number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        print(f'Question: {number}')
        answer = prompt.string(f'Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
