# main.py
# main file

from board import board
from player import player
from ai import ai
import os
from time import sleep


# app Class
# start the whole program
class app:

    # constructor
    def __init__(self):
        # board reference to the board Object - it handles the board
        self.board = None
        # numbers of players in the game
        self.numberPlayers = None
        # contains player objects
        self.player = []
        # every player gets different symbols
        self.symbols = [None, None]
        self.default_symbols = ["X", "O"]
        self.ai = None

    # create the game-board and clears it
    def create_board(self):
        self.board = board()
        self.board.clear()

    # shows the menu and selects the number of players
    def showMenu(self):

        print("Willkommen zu Tic-Tac-Toe")

        # while the player doesnt write 1 or 2 due the number of players
        while self.numberPlayers != 1 and self.numberPlayers != 2:

            # try - because the input could be a string
            try:

                # select number of players
                # 1 Player: play with KI
                # 2 Player: doesnt need the KI
                self.numberPlayers = int(input("Wie viele Spieler (1-2)? "))

                # if the player doesnt write a valueabled number - show error
                if self.numberPlayers != 1 and self.numberPlayers != 2:
                    print("Ungültige Eingabe...")

            # when the input is not an integer
            except ValueError:
                print("Ungültige Eingabe...")

    # an AI will be created
    def create_ai(self):

        # in userInput will be saved the difficult level
        level = None

        # while the user input is not valid
        # valid -> 1, 2, 3
        while True:

            # try, because the input have to be an integer
            # but the user could enter a stirng
            try:

                # level contains the level of difficulty of the AI
                level = int(input("Geben Sie die Schwierigkeitsstufe für die KI ein (1-Leicht, 2-Mittel, 3-Schwer): "))
                # if the user entered a valid input
                if 1 <= level <= 3:
                    # breaks the loop
                    break
                else:
                    # print error and continues the endless loop
                    print("Ungültige Eingabe...")
            # if the user entered a string
            except ValueError:
                # print error and continues the endless loop
                print("Ungültige Eingabe...")

        if self.symbols[0] == self.default_symbols[1]:
            self.symbols[1] = "X"
        else:
            self.symbols[1] = "O"

        # creates an new entry in the list self.player
        # saves in that entry a new player object
        self.player.append(player(1, self.symbols[1], True, "KI"))
        self.ai = ai(self.board, self.player[-1], level)

    # create as much player as in the self.numberPlayers and saves it in a list
    def create_player(self):

        for i in range(self.numberPlayers):

            # Saves the Name of the Player in name
            name = ""

            # while the Player doesn't a name
            while name == "":
                # player should enter a name
                name = input("Geben Sie den Namen für Spieler " + str(i+1) + " ein: ")
                # if the player clicked enter without enterd a name
                if name == "":
                    # print hint
                    print("Bitte gib einen Namen ein")


            # ToDo: Kommentieren
            symbol = input("Geben Sie ein Symbol für " + name + " ein (standart ist " + self.default_symbols[i] + "): ")

            while symbol in self.symbols or len(symbol) > 1 or symbol == " ":
                if symbol in self.symbols:
                    print("Zeichen wurde schon benutzt")
                elif len(symbol) > 1:
                    print("Symbol darf nicht mehr als ein Zeichen enthalten")
                else:
                    print("Symbol darf kein Leerzeichen sein")

                symbol = input("Geben Sie ein Symbol für " + name + " ein (standart ist " + self.default_symbols[i] + "): ")

            if symbol == "":
                symbol = self.default_symbols[i]

            self.symbols[i] = symbol

            # creates an new entry in the list self.player
            # saves in that entry a new player object
            self.player.append(player(i, symbol, False, name))

        # if the player selected the single player mode
        if self.numberPlayers == 1:
            # an AI will be created
            self.create_ai()

    # clears the command line
    def clear(self):
        # depending on the system
        # execute cls (for windows) or clear (for unix/mac OS)
        os.system('cls' if os.name == 'nt' else 'clear')

    # start game
    def start_game(self):

        # current player
        player = self.first_player
        # if an error occures it will be saved as an string in error
        error = None

        # run the game in an infiniti loop
        while True:

            # clears the command line
            self.clear()

            # shows the game-board
            self.board.show_board()

            # check if one of the user winns
            # if the function returns -1, the game-board is full
            # then break the loop too
            if self.board.is_winning() or self.board.is_winning() == -1:
                # if a user won then break the loop
                break

            # ToDo: Wenn ein Spieler gewonnen hat, markier die Siegesfelder farbig
            # Hierzu:   CRED = '\033[91m'
            #           CEND = '\033[0m'
            #           print(CRED + "Error, does not compute!" + CEND)
            # ToDo: Zähle, wie viele Spiele die einzelnen Spieler schon gewonnen haben

            # Info for the Player
            print("\nSpieler {} ist am Zug".format(self.player[player].name))

            # if an error occure
            if error is not None:
                # print the error
                # this has to be made due the clear
                print(error)
                # set error = None so the error disappear in the next round
                error = None

            # ToDo: Kommentare
            if self.player[player].is_ai:

                self.ai.move()

            else:

                # current Player writes the move
                position = input("Zug eingeben (z.B. a1): ")

                # calls the move function of the player
                # returns False if the move was invalid
                if not self.player[player].move(self.board, position):
                    # shows in the next round an error
                    error = "Ungültiger Zug..."
                    # don't continue the current instance of the loop
                    continue

            # Next Player
            player += 1
            # if theres no more Player, reset player = 0
            if player == len(self.player):
                player = 0

        # winning_player contains either the number of the player who wons
        # or -1 -> means the game-board is full
        winning_player = self.board.is_winning()

        # if the game-baord is full
        if winning_player == -1:
            #print error
            print("Keine freien Züge mehr... das Spiel ist unentschieden! Aber´s Schatzü ist trotzdem toll! Love you!")
        else:
            # print congrats
            print("Spieler {} hat gewonnen!!!".format(self.player[int(winning_player)].name))

    def select_player(self):

        self.first_player = 0

        while self.first_player != 1 and self.first_player != 2:

            try:

                self.first_player = int(input("Welcher Spieler soll anfagen (1: " + self.player[0].name + ", 2: " + self.player[1].name + ")? "))

            except ValueError:
                pass

        self.first_player -= 1

    # run-function
    # start the program
    def run(self):

        # shows the menu and selects the number of players
        self.showMenu()

        # creates the game-board
        self.create_board()

        # creates players
        self.create_player()

        # what player moves first
        self.select_player()

        # run the game
        self.start_game()


if __name__ == "__main__":
    # start the program
    app = app()
    app.run()
