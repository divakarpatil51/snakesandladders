from snakesandladders.dice_factory import DiceFactory
from snakesandladders.abstract_dice import AbstractDice


def test_dice_is_instance_of_abstract_dice():
    dice = DiceFactory.get_dice()

    assert isinstance(dice, AbstractDice.__class__)
