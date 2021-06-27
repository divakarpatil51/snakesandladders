from snakesandladders.dice import Dice


def test_roll_dice():
    val = Dice.roll()

    assert type(val) is int
    assert 1 <= val <= 6
