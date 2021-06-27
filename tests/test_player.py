from snakesandladders.player import  Player


def test_move_to():
    p = Player("test")
    p.move_to(10)

    assert p.get_current_pos() == 10
    assert p.name == "test"
