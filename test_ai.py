"""Tests the AI"""

import copy
import pytest
from ai import Ai
from player import Player
from board import Board


@pytest.fixture
def create_board():
    """Creates Board"""
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
    """Creates Player"""
    return Player(1, 'O', True, 'KI')


def test_is_winning(mocker, create_player, create_board):
    """Tests the function is_winning"""
    mocker.patch('time.sleep')
    board = create_board
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')
    assert ai.is_winning('X', 0)

    board.clear()
    ai = Ai(board, player_ai, 3, 'X')
    assert ai.is_winning('X', 0) is False


def test_move_weak(mocker, create_player, create_board):
    """Tests the function move_weak"""
    mocker.patch('time.sleep')
    board = create_board
    t1_board = copy.deepcopy(board.get_board())

    player_ai = create_player
    ai = Ai(board, player_ai, 1, 'X')
    ai.move()
    t2_board = copy.deepcopy(board.get_board())
    assert t1_board != t2_board


def test_move_middle(mocker, create_player, create_board):
    """Tests the function move_middle"""
    board = create_board

    mocker.patch('time.sleep')
    player_ai = create_player
    ai = Ai(board, player_ai, 2, 'X')
    ai.move()

    mocker.patch('ai.Ai.is_winning', side_effect=[True, False, False])
    mocker.patch('player.Player.move')
    mocker.patch('ai.Ai.move_weak')
    ai.move()

    ai.move()

    assert board.get_board()["c1"][1] is not None


def test_move_hard_defense(mocker, create_player, create_board):
    """Tests the function move_hard in defense mode"""
    board = create_board

    mocker.patch('time.sleep')

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
    mocker.patch('ai.Ai.move_middle')
    mocker.patch('ai.Ai.count_moves', return_value=3)
    ai.move()

    assert board.get_board()["b2"][1] is not None


def test_defense_two(mocker, create_player, create_board):
    """Tests the function move_hard in defense mode on Path 2"""
    board = create_board
    mocker.patch('time.sleep')
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    # Defense 2
    ai.path = 0
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

    mocker.patch('ai.Ai.count_moves', return_value=3)
    mocker.patch('player.Player.move')
    ai.move()

    assert board.get_board()["c3"][1] is not None or board.get_board()["c1"][1] is not None or \
           board.get_board()["a1"][1] is not None or board.get_board()["a3"][1] is not None


def test_defense_three(mocker, create_player, create_board):
    """Tests the function move_hard in defense mode on Path 3"""

    mocker.patch('time.sleep')
    board = create_board
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    # Path 3
    ai.path = 0
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

    new_board = {
        'a1': ['O', 1],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': ['X', 0],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()

    assert board.get_board()["c1"][1] is not None

    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': ['X', 0],
        'b2': ['O', 1],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()

    assert board.get_board()["a3"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['O', 1],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': ['X', 0],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()

    assert board.get_board()["c3"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': ['X', 0],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()

    assert board.get_board()["c3"][1] is not None

    # Path 1

    mocker.patch('ai.Ai.count_moves', return_value=1)

    ai.move()

    assert board.get_board()["b2"][1] is not None

    # Path 5
    mocker.patch('ai.Ai.count_moves', return_value=5)
    board.clear()
    ai.move()

    assert board.get_board()["a3"][1] is not None

    board.clear()
    mocker.patch('ai.Ai.is_winning', side_effect=["a3", False, False, "a3", "a3", False,
                                                  "a3", False, False])
    ai.move()

    assert board.get_board()["a3"][1] is not None

    board.clear()
    ai.move()

    assert board.get_board()["a3"][1] is not None

    # Path 6
    mocker.patch('ai.Ai.count_moves', return_value=7)

    ai.path = 0
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
    assert board.get_board()["a3"][1] is not None

    ai.move()
    assert board.get_board()["a3"][1] is not None

    mocker.patch('ai.Ai.move_weak')
    ai.move()


def test_move_hard_attack(mocker, create_player, create_board):
    """Tests the function move_hard in attack mode on Path 1"""
    board = create_board
    mocker.patch('time.sleep')
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    # Attack first Move
    ai.path = 0
    new_board = {
        'a1': [' ', None],
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
    ai.move()
    assert board.get_board()["a1"][1] is not None or board.get_board()["a2"][1] is not None or \
           board.get_board()["a3"][1] is not None or board.get_board()["c1"][1] is not None or \
           board.get_board()["c2"][1] is not None or board.get_board()["c3"][1] is not None

    # Attack 1
    ai.path = 0
    new_board = {
        'a1': [' ', None],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a3"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["b2"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    mocker.patch('ai.Ai.is_winning', return_value="a2")
    ai.move()
    assert board.get_board()["a2"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    mocker.patch('ai.Ai.is_winning', return_value=False)
    ai.move()
    assert board.get_board()["b2"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': ['X', 0],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)

    test = mocker
    test.patch('ai.Ai.is_winning', return_value="a2")
    test.patch('ai.Ai.count_moves', return_value=6)

    ai.move()
    assert board.get_board()["a2"][1] is not None


def test_move_hard_attack_path_two(mocker, create_player, create_board):
    """Tests the function move_hard in attack mode on Path 2"""

    mocker.patch('time.sleep')
    board = create_board
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    # Path 2

    ai.path = 0
    new_board = {
        'a1': ['O', 1],
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
    assert board.get_board()["c3"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c1"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a3"][1] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a1"][1] is not None

    # Path 4

    new_board = {
        'a1': ['O', 1],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': ['X', 0],
        'c2': ['X', 0],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a2"][1] is not None

    ai.sub_path = 0
    new_board = {
        'a1': [' ', None],
        'b1': ['O', 1],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': ['X', 0],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a1"][1] is not None

    ai.sub_path = 0
    new_board = {
        'a1': ['O', 1],
        'b1': [' ', None],
        'c1': ['X', 0],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': ['X', 0],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["a3"][1] is not None

    ai.sub_path = 0
    new_board = {
        'a1': ['O', 1],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': ['X', 0],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c1"][1] is not None

    ai.sub_path = 0
    new_board = {
        'a1': ['O', 1],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': ['X', 0],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c3"][1] is not None

    ai.sub_path = 0
    new_board = {
        'a1': ['O', 1],
        'b1': ['X', 0],
        'c1': ['O', 1],
        'a2': ['X', 0],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['X', 0],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["b2"][1] is not None


def test_move_hard_attack_path_three(mocker, create_player, create_board):
    """Tests the function move_hard in attack mode on Path 3"""

    mocker.patch('time.sleep')
    board = create_board
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    # Path 2

    ai.path = 0
    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["c3"][1] is not None

    # Path 4
    ai.path = 0
    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['X', 0],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.move()
    assert board.get_board()["b2"][1] is not None

    ai.path = 0
    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': ['X', 0],
        'a3': ['O', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    mocker.patch('ai.Ai.is_winning', return_value=False)
    ai.move()
    assert board.get_board()["c3"][1] is not None

    # Path 6
    ai.path = 0
    new_board = {
        'a1': ['X', 0],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': ['X', 0],
        'a3': ['O', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    mocker.patch('ai.Ai.count_moves', return_value=6)
    mocker.patch('ai.Ai.is_winning', return_value="c3")
    ai.move()
    assert board.get_board()["c3"][1] is not None


def test_set_move_corner(mocker, create_player):
    """Tests the function set_move_corner"""
    board = Board()
    board.clear()
    mocker.patch('time.sleep')
    player_ai = create_player
    ai = Ai(board, player_ai, 3, 'X')

    new_board = {
        'a1': ['O', 1],
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
    ai.set_move_corner()
    assert board.get_board()["c1"] is not None

    new_board = {
        'a1': ['O', 1],
        'b1': ['O', 1],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["a3"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["c3"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': ['O', 1],
        'b3': ['O', 1],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["a1"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["a1"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': ['O', 1],
        'c1': ['O', 1],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': [' ', None]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["c3"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': [' ', None],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["a3"] is not None

    new_board = {
        'a1': [' ', None],
        'b1': [' ', None],
        'c1': [' ', None],
        'a2': [' ', None],
        'b2': [' ', None],
        'c2': [' ', None],
        'a3': [' ', None],
        'b3': ['O', 1],
        'c3': ['O', 1]
    }
    board.set_board(new_board)
    ai.set_move_corner()
    assert board.get_board()["c1"] is not None
