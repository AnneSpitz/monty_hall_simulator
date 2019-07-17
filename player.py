import random


class Player:
    """
    Defines player behavior and contains the player's chosen door

    Available methods:
    choose_door will randomly choose a door when first called, then act according to strategy
    """
    def __init__(self, switch_strategy=True):
        self.__chosen_door = None
        self.__switch_strategy = switch_strategy

    @property
    def chosen_door(self):
        return self.__chosen_door

    def choose_door(self, door_set, revealed_doors):
        """
        First time called: Randomly selects a door and updates self.__chosen_door
        Called later: Will act according to the defined strategy

        Parameters
        ----------
        door_set : set
            Set of existing doors
        revealed_doors : set
            Set of doors revealed to the player

        returns
        -------
        Updates self.__chosen_door
        Returns nothing
        """
        if self.__chosen_door is None:  # if we don't have a previous choice, we make our initial choice
            self.__chosen_door = random.choice(tuple(door_set - revealed_doors))
        else:
            if self.__switch_strategy:  # we only switch if that's our strategy
                self.__chosen_door = random.choice(tuple(door_set - revealed_doors - {self.__chosen_door}))

        return None
