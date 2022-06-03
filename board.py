"""Handles the board"""


# board.py

class Board:
    """Handles the board"""

    # define gameBoard
    # a dictionary which contains all moves of the players
    def __init__(self):
        self.game_board = {}

    def clear(self):
        """set the game-board to default"""
        letters = ["a", "b", "c"]

        # game-board must contain a1, b1 c1, a2, b2, c2, a3, b3, c3
        for i in range(3):
            for letter in letters:
                self.game_board[letter + str(i + 1)] = [" ", None]

    def get_board(self):
        """returns the board"""
        return self.game_board

    def set_board(self, board):
        """sets the board"""
        self.game_board = board

    def show_board(self):
        """shows the game-board"""

        # prints on every position the related symbol in self.gameBoard
        # either X or O if a Player moved to this position
        # of " " if none of the players have moved to this
        print(" \n"
              "  {}  |  {}  |  {}     3\n"
              "-----|-----|-----\n"
              "  {}  |  {}  |  {}     2\n"
              "-----|-----|-----\n"
              "  {}  |  {}  |  {}     1\n\n"
              "  a     b     c".format(self.game_board["a3"][0],
                                       self.game_board["b3"][0],
                                       self.game_board["c3"][0],
                                       self.game_board["a2"][0],
                                       self.game_board["b2"][0],
                                       self.game_board["c2"][0],
                                       self.game_board["a1"][0],
                                       self.game_board["b1"][0],
                                       self.game_board["c1"][0]))

    def is_winning(self):
        """check if a player wins"""

        letters = ["a", "b", "c"]
        red = '\033[91m'
        end = '\033[0m'

        # for horizontal lines
        for letter in range(1, 4):
            # if the field xi (for example a1, b1, c1) contains X or O
            # and if the related fields are filled with X or O (depends on the player)
            if self.game_board["a" + str(letter)][1] is not None \
                    and self.game_board["a" + str(letter)][1] == \
                    self.game_board["b" + str(letter)][1] and \
                    self.game_board["b" + str(letter)][1] == self.game_board["c" + str(letter)][1]:
                # returns the player number

                self.game_board["a" + str(letter)][0] = \
                    red + self.game_board["a" + str(letter)][0] + end
                self.game_board["b" + str(letter)][0] = \
                    red + self.game_board["b" + str(letter)][0] + end
                self.game_board["c" + str(letter)][0] = \
                    red + self.game_board["c" + str(letter)][0] + end

                return str(self.game_board["a" + str(letter)][1])

        # for Vertical lines
        for letter in letters:
            # if the field ix (for example a1, a2, a3) contains X or O
            # and if the related fields are filled with X or O (depends on the player)
            if self.game_board[letter + str(1)][1] is not None \
                    and self.game_board[letter + str(1)][1] == \
                    self.game_board[letter + str(2)][1] and \
                    self.game_board[letter + str(2)][1] == self.game_board[letter + str(3)][1]:
                # returns the player number

                self.game_board[letter + str(1)][0] = \
                    red + self.game_board[letter + str(1)][0] + end
                self.game_board[letter + str(2)][0] = \
                    red + self.game_board[letter + str(2)][0] + end
                self.game_board[letter + str(3)][0] = \
                    red + self.game_board[letter + str(3)][0] + end

                return str(self.game_board[letter + str(1)][1])

        # for diagonal lines
        # if the fields a1, b2, c3 got the same symbol (X or O)
        if self.game_board["a1"][1] is not None \
                and self.game_board["a1"][1] == self.game_board["b2"][1] and \
                self.game_board["b2"][1] == self.game_board["c3"][1]:
            # returns the player number

            self.game_board["a1"][0] = red + self.game_board["a1"][0] + end
            self.game_board["b2"][0] = red + self.game_board["b2"][0] + end
            self.game_board["c3"][0] = red + self.game_board["c3"][0] + end

            return str(self.game_board["a1"][1])

        # if the fields c1, b2, a3 got the same symbol (X or O)
        if self.game_board["c1"][1] is not None \
                and self.game_board["c1"][1] == self.game_board["b2"][1] and \
                self.game_board["b2"][1] == self.game_board["a3"][1]:
            # returns the player number

            self.game_board["c1"][0] = red + self.game_board["c1"][0] + end
            self.game_board["b2"][0] = red + self.game_board["b2"][0] + end
            self.game_board["a3"][0] = red + self.game_board["a3"][0] + end

            return str(self.game_board["c1"][1])

        # check if the game board is full
        full = True
        # for all positions in the game board
        for letter in letters:
            for integer in range(1, 4):
                # if there's a field which is free, set full to False
                if self.game_board[letter + str(integer)][0] == " ":
                    full = False

        # if the game board is full, return -1
        if full:
            return -1

        # if none of the players won, return False
        return False
