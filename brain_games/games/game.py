import prompt
from brain_games.scripts import brain_games


def main(message, logic_of_game):
    user_name = brain_games.main()
    print(message)
    for _ in range(3):
        true_answer = logic_of_game()
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;\
(. Correct answer was '{true_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    print('da')
    main('', print('dsf'))
