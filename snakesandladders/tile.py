from tile_type import TileType


class Tile:

    def __init__(self, start_pos=0, end_pos=0, tile_type=TileType.NORMAL):
        self._start_pos = start_pos
        self._end_pos = end_pos
        self.tile_type = tile_type
        self.tile_type.validate_params(start_pos, end_pos)

    @property
    def start_pos(self):
        return self._start_pos

    @start_pos.setter
    def start_pos(self, val):
        self._start_pos = val

    @property
    def end_pos(self):
        return self._end_pos

    @end_pos.setter
    def end_pos(self, value):
        self._end_pos = value
