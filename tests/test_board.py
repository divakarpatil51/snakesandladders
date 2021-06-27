from unittest.mock import patch, Mock

import pytest

from snakesandladders.board import Board


@pytest.fixture(scope="class")
def board():
    b = Board()
    yield b


@patch.object(target=Board, attribute="__validate_tile_pos__")
def test_validate_pos_user_win(_validate_tile_mock, board):
    _validate_tile_mock.return_value = (False, 100)
    result = board.validate_pos(100)

    assert result == (True, 100)


@patch.object(target=Board, attribute="__validate_tile_pos__")
def test_validate_pos_normal_flow(_validate_tile_mock, board):
    _validate_tile_mock.return_value = (False, 1)
    result = board.validate_pos(1)

    assert result == (False, 1)


@patch.object(target=Board, attribute="__validate_tile_pos__")
def test_validate_pos_snake(_validate_tile_mock, board):
    _validate_tile_mock.return_value = (False, 7)
    result = board.validate_pos(14)

    assert result == (False, 7)


@patch.object(target=Board, attribute="__create_snakes__")
def test_initialize(snake_mock, board):
    board.initialize()

    snake_mock.assert_called_once()


@patch("snakesandladders.board.Tile")
def test_create_snakes(tile_mock, board):
    _mock = Mock()
    tile_mock.return_value = _mock
    board.__create_snakes__()

    assert len(board.tiles) == 1
    assert board.tiles[0] == _mock


def test_validate_normal_tile_pos(board):
    valid, pos = board.__validate_tile_pos__(10)

    assert (valid, pos) == (False, 10)


def test_validate_snake_tile_pos(board):
    snake_tile_mock = Mock()
    snake_tile_mock.start_pos = 14
    snake_tile_mock.end_pos = 7
    board.tiles.append(snake_tile_mock)

    valid, pos = board.__validate_tile_pos__(14)

    assert (valid, pos) == (False, 7)
