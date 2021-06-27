import pytest
from snakesandladders.tile import Tile
from snakesandladders.tile_type import TileType


def test_valid_snake_tile_values():
    tile = Tile(start_pos=10, end_pos=5, tile_type=TileType.SNAKE)

    assert tile.start_pos == 10
    assert tile.end_pos == 5


def test_invalid_snake_tile_values():
    with pytest.raises(AssertionError, match="Start position must be greater than end position for a Snake"):
        Tile(start_pos=10, end_pos=15, tile_type=TileType.SNAKE)


def test_valid_normal_tile_values():
    tile = Tile()

    assert tile.start_pos == 0
    assert tile.end_pos == 0
    assert tile.tile_type.name == TileType.NORMAL.name


def test_invalid_normal_tile_values():
    with pytest.raises(AssertionError, match="Start position must be equal to end position for a Normal Tile"):
        Tile(start_pos=10, end_pos=15)
