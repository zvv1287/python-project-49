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


def brain_gsd():
    from brain_games.games.brain_gsd import main as gsd_main
    gsd_main()


def brain_progression():
    from brain_games.games.brain_progression import main as progression_main
    progression_main()


if __name__ == '__main__':
    main()
    brain_even()
    brain_calc()
    brain_gsd()
    brain_progression()
