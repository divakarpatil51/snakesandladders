from dice import Dice
import random


class CrookedDice(Dice):

    @staticmethod
    def roll():
        return random.choice([2, 4, 6])
