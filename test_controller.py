"""Tests the Controller"""

import pytest

from controller import Controller
from view import View
from player import Player


@pytest.fixture
def create_controller():
    """Creates Controller"""
    view = View()
    return Controller(view)


@pytest.fixture
def create_player():
    """Creates Player"""
    return Player(0, "X", False, "Player")


def test_show_menu(mocker, create_controller):
    """Tests the function show_menu"""

    controller = create_controller
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('view.View.get_input', return_value='n')
    assert controller.show_menu() is False

    mocker.patch('os.path.exists', return_value=False)
    assert controller.show_menu() is False


def test_get_number_player(mocker, create_controller):
    """Tests the function get_number_player"""

    controller = create_controller
    mocker.patch('view.View.get_input', return_value=2)
    assert controller.get_number_player() == 2

    mocker.patch('view.View.get_input', side_effect=['a', '3', '1'])
    assert controller.get_number_player() == 1


def test_get_level_ai(mocker, create_controller):
    """Tests the function get_level_ai"""

    controller = create_controller
    mocker.patch('view.View.get_input', return_value=3)
    assert controller.get_level_ai() == 3

    mocker.patch('view.View.get_input', side_effect=['a', '4', '1'])
    assert controller.get_level_ai() == 1


def test_get_user_info(mocker, create_controller):
    """Tests the function get_user_info"""

    controller = create_controller
    mocker.patch('view.View.get_input', return_value="1")
    name, symbol = controller.get_user_info(0, ["X", "O"], [])
    assert name == '1' and symbol == "1"

    mocker.patch('view.View.get_input', side_effect=['', 'X', 'X', 'XX', ' ', ''])
    name, symbol = controller.get_user_info(1, ["X", "O"], ["X"])
    assert name == 'X' and symbol == 'O'


def test_get_fist_player(mocker, create_controller, create_player):
    """Tests the function get_first_player"""

    controller = create_controller
    mocker.patch('view.View.get_input', side_effect=['a', '1'])
    assert controller.get_first_player([create_player, create_player]) == 0


def test_get_input(mocker, create_controller):
    """Tests the function get_input"""

    controller = create_controller
    mocker.patch('view.View.get_input', return_value="Test")
    assert controller.get_input("Test") == "Test"
