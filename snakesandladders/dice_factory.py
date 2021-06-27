from dice import Dice
from abstract_dice import AbstractDice
from crooked_dice import CrookedDice
import random


class DiceFactory:

    @staticmethod
    def get_dice() -> AbstractDice:
        return random.choice([Dice, CrookedDice])
