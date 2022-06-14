import unittest
from unittest.mock import patch
from unittest import TestCase
from main import App

class Test(TestCase):

    @patch('view.View.get_input', return_value=1)
    def test_run(self, input):
        c = App()
        c.create_board()
        c.create_player()
        c.select_player()
        # a = App()
        # a.run()
