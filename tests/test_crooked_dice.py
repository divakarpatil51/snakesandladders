from snakesandladders.crooked_dice import CrookedDice


def test_crooked_dice():
    resp = CrookedDice.roll()

    assert resp in [2, 4, 6]
