import pytest
from main import App
from board import Board
from player import Player
from ai import Ai
import os


@pytest.fixture
def create_game():
    return App()


@pytest.fixture
def create_board():
    board = Board()
    board.clear()
    return board


def test_create_board(create_game, mocker):
    app = create_game
    mocker.patch('controller.Controller.get_number_player', return_value=1)
    app.create_board()
    assert app.board is not None and app.number_players == 1


def test_create_ai(create_game, mocker):
    app = create_game
    mocker.patch('controller.Controller.get_level_ai', return_value=3)
    app.symbols[0] = "X"
    app.default_symbols[1] = "X"
    app.create_ai()
    assert len(app.player) == 1 and app.artificial_intelligence is not None

    del app
    app = App()
    app.symbols[0] = "X"
    app.default_symbols[1] = "O"
    app.create_ai()
    assert len(app.player) == 1 and app.artificial_intelligence is not None


def test_create_player(create_game, mocker):
    app = create_game
    app.number_players = 1
    app.default_symbols = ["X", "O"]
    app.symbols = ["X", "O"]
    mocker.patch('view.View.get_input', return_value="1")

    app.create_player()
    assert len(app.player) == 2 and app.player[1].is_ai


def test_start_game(create_game, create_board, mocker):
    app = create_game
    app.board = create_board
    app.first_player = 0
    app.player = [Player(0, "X", True, "Player"), Player(0, "X", False, "Player")]
    app.artificial_intelligence = Ai(app.board, app.player[1], 3, "X")

    mocker.patch('view.View.print_to_ui', return_value="")
    mocker.patch('view.View.clear', return_value="")
    mocker.patch('board.Board.is_winning', return_value=1)
    mocker.patch('board.Board.show_board', return_value="")
    mocker.patch('controller.Controller.get_input', return_value="n")
    app.start_game()

    assert app.finish_game() == "n"

    mocker.patch('board.Board.is_winning', return_value=-1)
    app.start_game()

    mocker.patch('board.Board.is_winning', return_value=False)
    mocker.patch('controller.Controller.get_input', side_effect=['1', 'a1', 's'])
    mocker.patch('ai.Ai.move', return_value="")
    mocker.patch('main.App.save_score', return_value="")
    app.error = "Test"
    app.start_game()


def test_finish_game(create_game, create_board, mocker):
    app = create_game
    board = create_board
    app.player = [Player(0, "X", True, "Player1"), Player(1, "O", True, "Player2")]
    app.artificial_intelligence = app.player[0]
    app.board = board

    mocker.patch('board.Board.is_winning', return_value=-1)
    mocker.patch('controller.Controller.get_input', return_value='n')

    app.finish_game()

    assert app.artificial_intelligence.path is None and app.artificial_intelligence.sub_path is None

    mocker.patch('board.Board.is_winning', return_value=1)
    app.finish_game()

    assert app.artificial_intelligence.path is None and app.artificial_intelligence.sub_path is None


def test_select_player(mocker, create_game):
    app = create_game

    mocker.patch('controller.Controller.get_first_player', return_value=0)

    app.select_player()

    assert app.first_player == 0


def test_save_score(mocker, create_game, create_board):

    if os.path.exists("saves.dat"):
        os.remove("saves.dat")

    app = create_game
    board = create_board

    app.player = [Player(0, "X", True, "Player1"), Player(1, "O", False, "Player2")]
    app.board = board
    app.current_player = 0
    app.first_player = 0
    app.symbols = ["X", "O"]
    app.artificial_intelligence = Ai(board, app.player[0], 3, "O")
    app.artificial_intelligence.path = 1
    app.artificial_intelligence.sub_path = 1

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.remove', return_value=True)

    app.save_score()

    assert os.path.exists("saves.dat")


def test_load_score(mocker, create_game, create_board):
    test_save_score(mocker, create_game, create_board)

    app = App()

    app.load_score()

    assert app.board is not None and len(app.player) == 2 and len(app.symbols) == 2 and app.current_player == 0 \
           and app.artificial_intelligence is not None


def test_run(mocker, create_game):
    app = create_game
    app.current_player = None

    mocker.patch('controller.Controller.show_menu', return_value=True)
    mocker.patch('main.App.load_score', return_value="")
    mocker.patch('main.App.create_board', return_value="")
    mocker.patch('main.App.create_player', return_value="")
    mocker.patch('main.App.select_player', return_value="")
    mocker.patch('main.App.start_game', return_value="")
