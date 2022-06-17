"""Tests the View"""

import pytest
from view import View


@pytest.fixture
def create_view():
    """Creates view"""
    return View()


def test_get_input(mocker, create_view):
    """Tests the function get_input"""

    view = create_view

    mocker.patch('builtins.input', return_value="Test")

    assert view.get_input("Test") == "Test"


def test_print_to_ui(create_view):
    """Tests the function print_to_ui"""

    view = create_view

    view.print_to_ui("Test")


def test_clear(create_view):
    """Tests the function clear"""

    view = create_view
    view.clear()
