"""Checks Input from User and handles simple actions"""

from os.path import exists


class Controller:
    """Checks Input from User and handles simple actions"""

    def __init__(self, view):
        self.view = view

    def show_menu(self):
        """shows the menu and selects the number of players"""

        self.view.print_to_ui("Willkommen zu Tic-Tac-Toe")

        # if there's a save file
        if exists("saves.dat"):

            # user input will be saved in save_game
            save_game = str(0)
            # while user doesn't write y or n
            while save_game not in 'y' and save_game not in 'n':
                # save user input in save_game
                save_game = self.view.get_input("Soll gespeichertes Spiel "
                                                "geladen werden (y/n)? ").lower()

            # if the user would like to continue the saved game
            return save_game == 'y'

        return False

    def get_number_player(self):
        """Returns the number of Players"""

        number_player = 0
        accept_player = [1, 2]

        # while the player doesn't write 1 or 2 due the number of players
        while number_player not in accept_player:

            # try - because the input could be a string
            try:

                # select number of players
                # 1 Player: play with KI
                # 2 Player: doesn't need the KI
                number_player = int(self.view.get_input("Wie viele Spieler (1-2)? "))

                # if the player doesn't write a valuable number - show error
                if number_player not in accept_player:
                    self.view.print_to_ui("Ungültige Eingabe")

            # when the input is not an integer
            except ValueError:
                self.view.print_to_ui("Ungültige Eingabe")

        return number_player

    def get_level_ai(self):
        """Returns the Level of the AI"""

        # while the user input is not valid -> 1, 2, 3
        while True:

            # try, because the input have to be an integer
            # but the user could enter a string
            try:

                # level contains the level of difficulty of the AI
                level = int(self.view.get_input("Geben Sie die Schwierigkeitsstufe "
                                                "für die KI ein (1-Leicht, "
                                                "2-Mittel, 3-Schwer): "))

                # if the user entered a valid input
                if 1 <= level <= 3:
                    # breaks the loop
                    break

                # print error and continues the endless loop
                self.view.print_to_ui("Ungültige Eingabe")
            # if the user entered a string
            except ValueError:
                # print error and continues the endless loop
                self.view.print_to_ui("Ungültige Eingabe")

        return level

    def get_user_info(self, i, default_symbols, symbols):
        """Returns Name and Symbol from the User"""

        # Saves the Name of the Player in name
        name = ""

        # while the Player doesn't a name
        while name == "":
            # player should enter a name
            name = self.view.get_input("Geben Sie den Namen für Spieler " + str(i + 1) + " ein: ")
            # if the player clicked enter without entered a name
            if name == "":
                # print hint
                self.view.print_to_ui("Bitte gib einen Namen ein")

        # Player writes a single character for the symbol
        symbol = self.view.get_input("Geben Sie ein Symbol "
                                     "für " + name + " ein (standard "
                                                     "ist " + default_symbols[i] + "): ")

        # while the symbol is already used or if the user input is more than one character
        while (symbol in symbols and symbol != "") or len(symbol) > 1 or symbol == " ":

            # prints warning
            if symbol in symbols:
                self.view.print_to_ui("Zeichen wurde schon benutzt")

            # prints warning
            elif len(symbol) > 1:
                self.view.print_to_ui("Symbol darf nicht mehr als ein Zeichen enthalten")

            # prints warning
            else:
                self.view.print_to_ui("Symbol darf kein Leerzeichen sein")

            # ask the user again for the symbol
            symbol = self.view.get_input("Geben Sie ein Symbol "
                                         "für " + name + " ein (standard "
                                                         "ist " + default_symbols[i] + "): ")

        # if the user clicked enter without an entry
        if symbol == "":
            # use the default symbol
            symbol = default_symbols[i]

        return name, symbol

    def get_first_player(self, player):
        """Returns the ID of the first Player"""

        # the ID of the player which begins will be saved in self.first_player
        first_player = 0
        accept_player = [1, 2]

        # while the variable isn't 1 or 2
        while first_player not in accept_player:

            # try because the user could enter a string
            try:

                # Player input
                first_player = int(self.view.get_input("Welcher Spieler"
                                                       " soll anfangen (1: " + player[0].name +
                                                       ", 2: " + player[1].name + ")? "))

            # if the Player input wasn't an int
            except ValueError:
                # pass
                pass

        # the Player selected 1 or 2
        # but the Player IDs are 0 or 1
        return first_player - 1

    def get_input(self, text):
        """Returns User Input"""
        return self.view.get_input(text)
