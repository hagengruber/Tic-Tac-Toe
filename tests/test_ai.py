import pytest

from ai import Ai
from player import Player
from board import Board
from io import StringIO
import copy


@pytest.fixture
def create_board():
    board = Board()
    new_board = {
        'a1': ['X', 0],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['O', 1],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    return board


@pytest.fixture
def create_player():
    return Player(1, 'O', True, 'KI')


def test_is_winning(monkeypatch, create_player, create_board):
    board = create_board
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')
    is_winning = ai.is_winning('X', 0)
    assert is_winning


def test_move_weak(monkeypatch, create_player, create_board):
    board = create_board
    t1_board = copy.deepcopy(board.get_board())

    player_ai = create_player
    ai = Ai(board, player_ai, 1, 'X')
    ai.move()
    t2_board = copy.deepcopy(board.get_board())
    assert t1_board != t2_board


def test_move_middle(monkeypatch, create_player, create_board):
    board = create_board

    player_ai = create_player
    ai = Ai(board, player_ai, 2, 'X')
    ai.move()
    assert board.get_board()["c1"][1] is not None


def test_move_hard(monkeypatch, create_player, create_board):
    board = create_board

    # Defense 1
    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)

    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')
    ai.move()
    assert board.get_board()["b2"][1] is not None

    # Defense 2
    ai.path = None
    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c3"][1] is not None or board.get_board()["c1"][1] is not None or \
           board.get_board()["a1"][1] is not None or board.get_board()["a3"][1] is not None

    # Defense 3
    ai.path = None
    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': ['X', 0],
        'b2': ['O', 1],
        'c2': ['X', 0],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a1"][1] is not None or board.get_board()["a2"][1] is not None or \
           board.get_board()["a3"][1] is not None or board.get_board()["c1"][1] is not None or \
           board.get_board()["c2"][1] is not None or board.get_board()["c3"][1] is not None

    # Attack
    ai.path = None
    new_board = {
        'a1': ['X', 0],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['O', 1],
        'c2': [' ', None],
        'a3': ['X', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c1"][1] is not None
