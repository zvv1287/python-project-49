#!/usr/bin/env python3
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    return cli.welcome_user()


def brain_even():
    from brain_games.games.brain_even import main as even_main
    even_main()


def brain_calc():
    from brain_games.games.brain_calc import main as calc_main
    calc_main()


if __name__ == '__main__':
    main()
    brain_even()
    brain_calc()
    
