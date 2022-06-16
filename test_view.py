import pytest
from view import View


@pytest.fixture
def create_view():
    return View()


def test_get_input(mocker, create_view):
    view = create_view

    mocker.patch('builtins.input', return_value="Test")

    assert view.get_input("Test") == "Test"


def test_print_to_ui(mocker, create_view, monkeypatch):
    view = create_view
    mocker_print = mocker.patch('builtins.print')

    view.print_to_ui("Test")
    # assert [call('Test')] in mocker_print.mock_calls


def test_clear(create_view):
    view = create_view
    view.clear()
