import pytest
from main import App
from board import Board
from player import Player
from ai import Ai
import os


@pytest.fixture
def create_game():
    return App()
