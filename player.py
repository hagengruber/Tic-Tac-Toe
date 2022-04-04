# player.py
# handles players

# player class
class player:

    # define player
    # self.num has the number of the player (0 or 1)
    # self.symbol has the symbol of the player (at default X or O)
    def __init__(self, num, symbol, is_ai, name):
        self.num = num
        self.symbol = symbol
        self.name = name
        self.is_ai = is_ai

    # the player moved to a field
    def move(self, gameBoard, position):
        # b contains the gameBoard - a dictionary (see board.py -> get_board() for more details)
        b = gameBoard.get_board()

        # if the move is valid
        if position in b:
            # if the position is validated
            if b[position][0] == " ":
                # the position of the dictionary contains a list
                # set the symbol self.symbol at [0]
                # set the number of the player self.num at [1]
                b[position][0] = self.symbol
                b[position][1] = self.num
            # if the position of the field was not validate
            # return False
            else:
                return False
        # if the position of the field was not valid
        # return False
        else:
            return False

        # if the position is set
        # set the game-board with set_board
        gameBoard.set_board(b)

        # if the position is set
        # return true
        return True
