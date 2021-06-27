from functools import lru_cache

from tile import Tile
from tile_type import TileType


class Board:

    def __init__(self):
        self.size = 100
        self.tiles = []

    def initialize(self):
        self.__create_snakes__()

    def __create_snakes__(self):
        snake = Tile(start_pos=14, end_pos=7, tile_type=TileType.SNAKE)
        self.tiles.append(snake)

    def validate_pos(self, next_pos):
        valid, next_pos = self.__validate_tile_pos__(next_pos)

        if next_pos >= self.size:
            print("You won!!")
            return True, next_pos

        return valid, next_pos

    @lru_cache(50)
    def __validate_tile_pos__(self, next_pos):
        for tile in self.tiles:
            if next_pos == tile.start_pos:
                print(f"You have step onto a {tile.tile_type.name}! "
                      f"Moving from position {tile.start_pos} to {tile.end_pos}.")
                return False, tile.end_pos
        return False, next_pos

