import argparse
import sys

from game import Game
from player import Player


def play_games(number_of_games, switch_strategy=True, number_of_doors=3):
    """
    Plays a number of games, then returns the percentage of victory

    Parameters
    ----------
    number_of_games : int
        defines the number of games simulated
    switch_strategy : bool, optional
        defines the player's behavior. If True, the player will change doors after doors have been revealed,
        will do nothing otherwise. By default True
    number_of_doors : int, optional
        defines the number of doors each games will have, by default 3 (classic Monty Hall problem)

    Returns
    -------
    Float
        Percentage of victories over the total number of games
    """
    times_won = 0

    game = Game(number_of_doors=number_of_doors)
    for _ in range(number_of_games):
        player = Player(switch_strategy=switch_strategy)
        player.choose_door(door_set=game.door_set, revealed_doors=game.revealed_doors)

        game.reveal_doors(player.chosen_door)
        player.choose_door(door_set=game.door_set, revealed_doors=game.revealed_doors)

        if game.check_victory(chosen_door_player=player.chosen_door):
            times_won += 1

        game.reset_state()

    victory_percentage = times_won / number_of_games

    return victory_percentage

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n_games", "--number_of_games", type=int, default=10000, help="Define the number of games to run.")
    parser.add_argument("-switch", "--switch_strategy", type=str, default="False", help="Define the strategy of the player: if True the player will always switch, else he will never switch.")
    parser.add_argument("-n_doors", "--number_of_doors", type=int, default=3, help="Define the number of doors in the game.")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argument_parser()
    if args.switch_strategy == "True":
        SWITCH_STRATEGY = True
    else:
        SWITCH_STRATEGY = False

    victory_percentage = play_games(number_of_games=args.number_of_games,
                                    switch_strategy=SWITCH_STRATEGY,
                                    number_of_doors=args.number_of_doors)

    print('The percentage of victory is {}.'.format(victory_percentage))
