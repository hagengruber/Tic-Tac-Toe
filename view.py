import os


class View:

    def __int__(self):
        pass

    @staticmethod
    def print_to_ui(text):
        print(text)

    @staticmethod
    def get_input(text=""):
        return input(text)

    @staticmethod
    def clear():
        # depending on the system
        # execute cls (for windows) or clear (for unix/macOS)
        os.system('cls' if os.name == 'nt' else 'clear')
