# main.py
# main file -> model

#
#   @author: Florian Hagengruber: 22101608
#   enjoy!

from board import Board
from player import Player
from ai import Ai
import os
from os.path import exists
import ast
import view
import controller


# app Class
# start the whole program
class App:

    # constructor
    def __init__(self):
        # board reference to the board Object - it handles the board
        self.board = None
        # numbers of players in the game
        self.numberPlayers = None
        # contains player objects
        self.player = []
        # every player gets different symbols
        self.symbols = ["", ""]
        # there are also default symbols for each Player
        self.default_symbols = ["X", "O"]
        # if the user selects the one-Player mode, in self.ai will be a Player Object for the AI
        self.ai = None
        # contains the Player who currently moves
        self.current_player = None
        self.first_player = None
        self.view = view.View()
        self.controller = controller.Controller(self.view)

    # create the game-board and clears it
    def create_board(self):
        self.board = Board()
        self.board.clear()
        self.numberPlayers = self.controller.getNumberPlayer()

    # an AI will be created
    def create_ai(self):

        level = self.controller.getLevelAI()

        # if the user use the Symbol O
        if self.symbols[0] == self.default_symbols[1]:
            # AI use the Symbol X
            self.symbols[1] = "X"
        else:
            # if the user doesn't use the Symbol O, AI is using O
            self.symbols[1] = "O"

        # creates a new entry in the list self.player
        # saves in that entry a new player object
        self.player.append(Player(1, self.symbols[1], True, "KI"))
        self.ai = Ai(self.board, self.player[-1], level, self.symbols[0])

    # create as much player as in the self.numberPlayers and saves it in a list
    def create_player(self):

        for i in range(self.numberPlayers):

            name, symbol = self.controller.getUserInfo(i, self.default_symbols, self.symbols)

            # saves the used symbol in self.symbols
            self.symbols[i] = symbol

            # creates a new entry in the list self.player
            # saves in that entry a new player object
            self.player.append(Player(i, symbol, False, name))

        # if the player selected the single player mode
        if self.numberPlayers == 1:
            # an AI will be created
            self.create_ai()

    # start game
    def start_game(self):

        if self.current_player is None:
            # current player
            self.current_player = self.first_player

        # if an error occurs it will be saved as a string in error
        error = None

        # run the game in an infinite loop
        while True:

            # clears the command line
            self.view.clear()

            # shows the game-board
            self.board.show_board()

            # check if one of the user wins
            # if the function returns -1, the game-board is full
            if self.board.is_winning() or self.board.is_winning() == -1:
                # the game is finished
                # selects the start player for the next round
                self.current_player = int(self.first_player)

                self.view.clear()
                self.board.show_board()

                # calls self.finish_game()
                # the function prints the winner and asks the player
                # if they would like to continue the game
                if self.finish_game() == 'y':
                    # if the user input was y, the loop will continue
                    continue
                else:
                    # if the user input was n, the loop breaks
                    break

            self.view.print_to_ui("\nFür Speichern und Beenden, 's' eingeben")

            # Info for the Player
            self.view.print_to_ui("\nSpieler {} ist am Zug".format(self.player[int(self.current_player)].name))

            # if an error occur
            if error is not None:
                # print the error
                # this has to be made due the clear
                self.view.print_to_ui(error)
                # set error = None so the error disappear in the next round
                error = None

            # if the current Player is an AI
            if self.player[int(self.current_player)].is_ai:
                # AI should move
                self.ai.move()

            # if the current Player is not an AI
            else:

                # current Player writes the move
                position = self.controller.get_input("Zug eingeben (z.B. a1): ").lower()

                if position == 's':
                    self.save_score()
                    break

                # calls the move function of the player
                # returns False if the move was invalid
                if not self.player[int(self.current_player)].move(self.board, position):
                    # shows in the next round an error
                    error = "Ungültiger Zug..."
                    # don't continue the current instance of the loop
                    continue

            # Next Player
            self.current_player += 1
            # if there's no more Player, reset player = 0
            if self.current_player == len(self.player):
                self.current_player = 0

    # clears the game-board and asks if the player want to continue the game
    def finish_game(self):
        # winning_player contains either the number of the player who won
        # or -1 -> means the game-board is full
        winning_player = self.board.is_winning()

        # if the game-board is full
        if winning_player == -1:
            # print error
            self.view.print_to_ui("Keine freien Züge mehr... das Spiel ist unentschieden!")
        else:
            # print congrats
            self.view.print_to_ui("Spieler {} hat gewonnen!!!".format(self.player[int(winning_player)].name))

        # clears the game-board
        self.board.clear()

        if self.player[0].is_ai or self.player[1].is_ai:
            # Sets the strategy for the AI to None
            self.ai.path = None
            self.ai.sub_path = None

        # the user input is in continue_game
        continue_game = None

        # while the user input isn't valid
        while continue_game != 'y' and continue_game != 'n':
            # saves the user input in continue_game
            continue_game = self.controller.get_input("Neue Runde beginnen (y/n)? ").lower()

        # return the user input
        return continue_game

    # Player decided which Player starts the game
    def select_player(self):

        self.first_player = self.controller.get_first_player(self.player)

    # saves the current score
    def save_score(self):

        # if a save file exists, remove it
        if exists("saves.dat"):
            os.remove("saves.dat")

        # open a new save file, called saves.dat
        f = open("saves.dat", "a")

        # for every entry in the list self.player
        for i in self.player:
            # saves the number, the symbol and the name of every Player and if it's an AI
            f.write("(" + str(i.num))
            f.write("(" + str(i.symbol))
            f.write("(" + str(i.name))
            f.write("(" + str(i.is_ai))

        # saves the game-board
        f.write("(" + str(self.board.get_board()))
        # saves the current Player (0 or 1)
        f.write("(" + str(self.current_player))
        # saves the first player (if the player finish a round and want to play another)
        f.write("(" + str(self.first_player))
        # saves the symbols
        f.write("(" + str(self.symbols))

        # if the player chose to play with an AI
        if self.ai is not None:
            # saves the level of the AI
            f.write("(" + str(self.ai.level))
            f.write("(" + str(self.ai.path))
            f.write("(" + str(self.ai.sub_path))

        # close the file
        f.close()

    # loads the score
    def load_score(self):

        # opens the save file
        f = open("saves.dat", "r")
        # creates a list
        # separates the string by every (
        data = f.read().split('(')

        # create a board
        self.board = Board()
        # set the board
        # the ast.literal_eval creates a dictionary instead of a string
        self.board.set_board(ast.literal_eval(data[9].replace("'", '"')))

        # creates the player
        for i in range(1, 3):
            # append an entry in the self.player list

            self.player.append(Player(int(data[i * 4 - 3]), data[i * 4 - 2], data[i * 4] == 'True', data[i * 4 - 1]))
            # if the player is an AI
            if data[i * 4] == 'True':
                self.view.print_to_ui(data[i * 4 - 2])
                # creates an AI object
                self.ai = Ai(self.board, self.player[-1], int(data[13]), data[(i - 1) * 4 - 2])
                self.ai.path = int(data[14])
                self.ai.sub_path = int(data[14])

        # set the first player (if the player finish a round and want to play another)
        self.first_player = data[11]

        # set the symbols
        # ast.literal_eva creates a list instead of a string
        self.symbols = ast.literal_eval(data[12])

        # set the current player
        self.current_player = int(data[10])

        # close the save file
        f.close()
        # remove the save file
        os.remove("saves.dat")

    # run-function
    # start the program
    def run(self):

        # shows the menu, check if there's a save file and selects the number of players
        continue_game = self.controller.showMenu()

        if continue_game:
            self.load_score()

        # if there's a current Player the Player loaded a game from a save file
        # in that case, the board and the Players are already set
        if self.current_player is None:
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
    app = App()
    app.run()
