from abstract_dice import AbstractDice
import random


class Dice(AbstractDice):

    @staticmethod
    def roll():
        return random.randint(1, 6)
