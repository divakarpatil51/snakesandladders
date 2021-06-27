from enum import Enum


class TileType(Enum):
    NORMAL = "normal"
    SNAKE = "snake"

    def validate_params(self, start_pos, end_pos):
        if self == TileType.SNAKE:
            assert start_pos > end_pos, "Start position must be greater than end position for a Snake"

        if self == TileType.NORMAL:
            assert start_pos == end_pos, "Start position must be equal to end position for a Normal Tile"
