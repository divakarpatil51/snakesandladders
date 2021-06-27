import pytest
from snakesandladders.abstract_dice import AbstractDice


def test_roll_dice_exception():
    with pytest.raises(NotImplementedError, match="Child class must implement this method."):
        AbstractDice.roll()
