# board.py
# handles the board

# board class
class Board:

    # define gameBoard
    # a dictionary which contains all moves of the players
    def __init__(self):
        self.gameBoard = {}

    # set the game-board to default
    def clear(self):
        letters = ["a", "b", "c"]

        # game-board must contain a1, b1 c1, a2, b2, c2, a3, b3, c3
        for i in range(3):
            for a in letters:
                self.gameBoard[a + str(i + 1)] = [" ", None]

    # returns the board
    def get_board(self):
        return self.gameBoard

    # sets the board
    def set_board(self, board):
        self.gameBoard = board

    # shows the game-board
    def show_board(self):

        # prints on every position the related symbol in self.gameBoard
        # either X or O if a Player moved to this position
        # of " " if none of the players have moved to this
        print(" \n"
              "  {}  |  {}  |  {}     3\n"
              "-----|-----|-----\n"
              "  {}  |  {}  |  {}     2\n"
              "-----|-----|-----\n"
              "  {}  |  {}  |  {}     1\n\n"
              "  a     b     c".format(self.gameBoard["a3"][0], self.gameBoard["b3"][0], self.gameBoard["c3"][0],
                                       self.gameBoard["a2"][0], self.gameBoard["b2"][0], self.gameBoard["c2"][0],
                                       self.gameBoard["a1"][0], self.gameBoard["b1"][0], self.gameBoard["c1"][0]))

    # check if a player wins
    def is_winning(self):

        letters = ["a", "b", "c"]
        RED = '\033[91m'
        END = '\033[0m'

        # for horizontal lines
        for i in range(1, 4):
            # if the field xi (for example a1, b1, c1) contains X or O
            # and if the related fields are filled with X or O (depends on the player)
            if self.gameBoard["a" + str(i)][1] is not None and self.gameBoard["a" + str(i)][1] == \
                    self.gameBoard["b" + str(i)][1] and \
                    self.gameBoard["b" + str(i)][1] == self.gameBoard["c" + str(i)][1]:
                # returns the player number

                self.gameBoard["a" + str(i)][0] = RED + self.gameBoard["a" + str(i)][0] + END
                self.gameBoard["b" + str(i)][0] = RED + self.gameBoard["b" + str(i)][0] + END
                self.gameBoard["c" + str(i)][0] = RED + self.gameBoard["c" + str(i)][0] + END

                return str(self.gameBoard["a" + str(i)][1])

        # for Vertical lines
        for i in letters:
            # if the field ix (for example a1, a2, a3) contains X or O
            # and if the related fields are filled with X or O (depends on the player)
            if self.gameBoard[i + str(1)][1] is not None and self.gameBoard[i + str(1)][1] == \
                    self.gameBoard[i + str(2)][1] and self.gameBoard[i + str(2)][1] == self.gameBoard[i + str(3)][1]:
                # returns the player number

                self.gameBoard[i + str(1)][0] = RED + self.gameBoard[i + str(1)][0] + END
                self.gameBoard[i + str(2)][0] = RED + self.gameBoard[i + str(2)][0] + END
                self.gameBoard[i + str(3)][0] = RED + self.gameBoard[i + str(3)][0] + END

                return str(self.gameBoard[i + str(1)][1])

        # for diagonal lines
        # if the fields a1, b2, c3 got the same symbol (X or O)
        if self.gameBoard["a1"][1] is not None and self.gameBoard["a1"][1] == self.gameBoard["b2"][1] and \
                self.gameBoard["b2"][1] == self.gameBoard["c3"][1]:
            # returns the player number

            self.gameBoard["a1"][0] = RED + self.gameBoard["a1"][0] + END
            self.gameBoard["b2"][0] = RED + self.gameBoard["b2"][0] + END
            self.gameBoard["c3"][0] = RED + self.gameBoard["c3"][0] + END

            return str(self.gameBoard["a1"][1])

        # if the fields c1, b2, a3 got the same symbol (X or O)
        if self.gameBoard["c1"][1] is not None and self.gameBoard["c1"][1] == self.gameBoard["b2"][1] and \
                self.gameBoard["b2"][1] == self.gameBoard["a3"][1]:
            # returns the player number

            self.gameBoard["c1"][0] = RED + self.gameBoard["c1"][0] + END
            self.gameBoard["b2"][0] = RED + self.gameBoard["b2"][0] + END
            self.gameBoard["a3"][0] = RED + self.gameBoard["a3"][0] + END

            return str(self.gameBoard["c1"][1])

        # check if the game board is full
        full = True
        # for all positions in the game board
        for i in letters:
            for a in range(1, 4):
                # if there's a field which is free, set full to False
                if self.gameBoard[i + str(a)][0] == " ":
                    full = False

        # if the game board is full, return -1
        if full:
            return -1

        # if none of the players won, return False
        return False
