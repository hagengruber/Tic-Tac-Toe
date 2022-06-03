"""Creates Player"""


# player.py
# handles players

# player class
class Player:
    """Creates Player"""

    # define player
    # self.num has the number of the player (0 or 1)
    # self.symbol has the symbol of the player (at default X or O)
    def __init__(self, num, symbol, is_ai, name):
        self.num = num
        self.symbol = symbol
        self.name = name
        self.is_ai = is_ai

    def check_valid_move(self, board, position):
        """Check Valid move"""
        # if the move is valid
        if position in board:
            # if the position is validated
            if board[position][0] == " ":
                # the position of the dictionary contains a list
                # set the symbol self.symbol at [0]
                # set the number of the player self.num at [1]
                board[position][0] = self.symbol
                board[position][1] = self.num
                return True
            return False
        return False

    def move(self, game_board, position):
        """the player moved to a field"""
        # b contains the gameBoard - a dictionary (see board.py -> get_board() for more details)
        board = game_board.get_board()

        accept = self.check_valid_move(board, position)

        if accept:
            # if the position is set,
            # set the game-board with set_board
            game_board.set_board(board)

            # if the position is set
            # return true
            return True
        return False
