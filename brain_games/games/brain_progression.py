import random
from brain_games.games.game import main as games_main


def logic_of_game():
    a = random.randint(0, 100)
    d = random.randint(0, 10)
    quantity = random.randint(5, 10)
    res_list = []
    for i in range(quantity):
        res_list.append(a + i * d)
    number_index = random.randint(0, quantity - 1)
    true_answer = str(res_list[number_index])
    res_list[number_index] = '..'
    print(f'Question: {" ".join(map(str, res_list))}')
    return true_answer


message = 'What number is missing in the progression?'


def main():
    games_main(message=message, logic_of_game=logic_of_game)


if __name__ == '__main__':
    main()
