"""Handles interaction with User"""

import os


class View:
    """Handles interaction with User"""

    def __int__(self):
        pass

    @staticmethod
    def print_to_ui(text):
        """Prints text to UI"""
        print(text)

    @staticmethod
    def get_input(text=""):
        """Returns User Input"""
        return input(text)

    @staticmethod
    def clear():
        """Clears the Terminal"""
        # depending on the system
        # execute cls (for windows) or clear (for unix/macOS)
        os.system('cls' if os.name == 'nt' else 'clear')
