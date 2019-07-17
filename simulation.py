import sys

import random


class Game:
    """
    Contains the set of existing doors, revealed doors, the correct door.

    Available methods:
    reveal_doors mimics the behavior of the game assistant when he reveals doors to the player
    check_victory reveals if the player chose the correct door
    """

    def __init__(self, number_of_doors=3):
        self.number_of_doors = number_of_doors
        self.door_set = {integer for integer in range(self.number_of_doors)}
        self.correct_door = random.choice(tuple(self.door_set))
        self.revealed_doors = set()

    def reveal_doors(self, chosen_door_player):
        """Reveals all doors except 2 to the player. 
        Such doors have to be incorrect doors (goats), and cannot be the one door that the player chose.
        
        Parameters
        ----------
        chosen_door_player : int
            this argument should be the door number that the player chose
        
        Returns
        -------
        Updates self.revealed_doors
        Returns Nothing
        """

        #Changes self.revealed_doors and doesn't return anything

        available_doors = self.door_set - self.revealed_doors \
            - {chosen_door_player} - {self.correct_door}
        # we don't want to open a door with the car or the door chosen by the player

        if chosen_door_player != self.correct_door:
            # then there is no choice in the doors to reveal - we have to reveal every door except the correct one and the one
            # chosen by the player
            self.revealed_doors = self.revealed_doors | available_doors
        else:
            unrevealed_door = random.choice(tuple(available_doors))
            # we want to have 2 remaining closed doors at the end of this process

            self.revealed_doors = self.revealed_doors | available_doors - {unrevealed_door}
            # self.revealed_doors = available_doors - {unrevealed_door}

    def check_victory(self, player_chosen_door):
        """Returns True if the player won
        Victory is defined by "The player chose the correct door",
        so if game.correct_door == player.chosen_door
        
        Parameters
        ----------
        player_chosen_door : int
            this argument should be the door number that the player chose
        
        Returns
        -------
        Bool
            True if the player won
        """
        if self.correct_door == player_chosen_door:
            return True
        else:
            return False


class Player:
    """
    Defines player behavior and contains the player's chosen door

    Available methods:
    choose_door will randomly choose a door when first called, then act according to strategy
    """
    def __init__(self, switch_strategy=True):
        self.chosen_door = None
        self.switch_strategy = switch_strategy

    def choose_door(self, door_set, revealed_doors):
        """First time called: Randomly selects a door and updates self.chosen_door
        Called later: Will act according to the defined strategy
        
        Parameters
        ----------
        door_set : set
            Set of existing doors
        revealed_doors : set
            Set of doors revealed to the player
        """
        if self.chosen_door is None:  # if we don't have a previous choice, we make our initial choice
            self.chosen_door = random.choice(tuple(door_set - revealed_doors))
        else:
            if self.switch_strategy:  # we only switch if that's our strategy
                self.chosen_door = random.choice(tuple(door_set - revealed_doors - {self.chosen_door}))


def play_games(number_of_games, switch_strategy=True, number_of_doors=3):
    """Plays a number of games, then returns the percentage of victory
    
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

    for _ in range(number_of_games):
        game = Game(number_of_doors=number_of_doors)
        player = Player(switch_strategy=switch_strategy)
        player.choose_door(door_set=game.door_set, revealed_doors=game.revealed_doors)

        game.reveal_doors(player.chosen_door)
        player.choose_door(door_set=game.door_set, revealed_doors=game.revealed_doors)

        if game.check_victory(player_chosen_door=player.chosen_door):
            times_won += 1

    victory_percentage = times_won / number_of_games

    return victory_percentage


if __name__ == '__main__':
    if sys.argv[2] == "True":
        SWITCH_STRATEGY = True
    else:
        SWITCH_STRATEGY = False

    print(play_games(number_of_games=int(sys.argv[1]),
                     switch_strategy=SWITCH_STRATEGY, number_of_doors=int(sys.argv[3])))
