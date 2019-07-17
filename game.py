import random


class Game:
    """
    Contains the set of existing doors, revealed doors, the correct door.

    Available methods:
    reveal_doors mimics the behavior of the game assistant when he reveals doors to the player
    check_victory reveals if the player chose the correct door
    """

    def __init__(self, number_of_doors=3):
        self.__number_of_doors = number_of_doors
        self.__door_set = set(range(self.__number_of_doors))
        self.__correct_door = random.choice(tuple(self.__door_set))
        self.__revealed_doors = set()

    @property
    def door_set(self):
        return self.__door_set

    @property
    def revealed_doors(self):
        return self.__revealed_doors

    def reveal_doors(self, chosen_door_player):
        """
        Reveals all doors except 2 to the player.
        Such doors have to be incorrect doors (goats), and cannot be the one door that the player chose.

        Parameters
        ----------
        chosen_door_player : int
            this argument should be the door number that the player chose

        Returns
        -------
        Updates self.__revealed_doors
        Returns Nothing
        """

        #Changes self.__revealed_doors and doesn't return anything

        available_doors = self.__door_set - self.__revealed_doors \
            - {chosen_door_player} - {self.__correct_door}
        # we don't want to open a door with the car or the door chosen by the player

        if chosen_door_player != self.__correct_door:
            # then there is no choice in the doors to reveal - we have to reveal every door except the correct one and the one
            # chosen by the player
            self.__revealed_doors = self.__revealed_doors | available_doors
        else:
            unrevealed_door = random.choice(tuple(available_doors))
            # we want to have 2 remaining closed doors at the end of this process

            self.__revealed_doors = self.__revealed_doors | available_doors - {unrevealed_door}
            # self.__revealed_doors = available_doors - {unrevealed_door}

        return None

    def check_victory(self, chosen_door_player):
        """
        Returns True if the player won
        Victory is defined by "The player chose the correct door",
        so if game.correct_door == player.chosen_door

        Parameters
        ----------
        chosen_door_player : int
            this argument should be the door number that the player chose

        Returns
        -------
        Bool
            True if the player won
        """
        if self.__correct_door == chosen_door_player:
            return True
        else:
            return False

    def reset_state(self):
        """
        Resets the state of the game
        Sets a new correct_door and cleans self.__revealed_doors
        """
        self.__correct_door = random.choice(tuple(self.__door_set))
        self.__revealed_doors = set()
