from snakesandladders.board import Board


def test_validate_pos_user_win():
    b = Board()
    result = b.validate_pos(100)

    assert result


def test_validate_pos_normal_flow():
    b = Board()
    result = b.validate_pos(1)

    assert not result
