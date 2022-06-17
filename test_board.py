"""Tests the Board"""

from copy import deepcopy
import pytest
from board import Board


@pytest.fixture
def create_board():
    """Creates Board"""
    board = Board()
    board.clear()
    return board


def test_clear(create_board):
    """Tests the function clear"""
    board = create_board
    test_board = deepcopy(board.get_board())
    new_board = {"a1": 0}
    board.set_board(new_board)
    board.clear()
    assert board.get_board() == test_board


def test_show_board(create_board):
    """Tests the function show_board"""
    board = create_board
    com_output = board.show_board()
    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': ['X', 0],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    output = board.show_board()
    assert output != com_output


def test_is_winning():
    """Tests the function is_winning"""
    board = Board()
    board.clear()

    new_board = {
        'a1': ['X', 0],
        'b1': ['X', 0],
        'c1': ['X', 0],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    assert board.is_winning() == '0'

    board.clear()

    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': ['X', 0],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    assert board.is_winning() == '0'

    board.clear()

    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': ['X', 0]
    }
    board.set_board(new_board)
    assert board.is_winning() == '0'

    board.clear()

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': ['X', 0],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    assert board.is_winning() == '0'

    board.clear()
    new_board = {
        'a1': ['X', 0],
        'b1': ['O', 1],
        'c1': ['X', 0],
        'a2': ['O', 1],
        'b2': ['O', 1],
        'c2': ['X', 0],
        'a3': ['X', 0],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    assert board.is_winning() == -1

    board.clear()

    assert board.is_winning() is False
