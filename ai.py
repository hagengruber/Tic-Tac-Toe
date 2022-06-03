"""Controls behavior of the AI"""

from time import sleep
from random import randint
import player


# ai class
class Ai:
    """Controls behavior of the AI"""

    # define AI
    def __init__(self, board, play, level, enemy_symbol):
        # the AI needs the board
        self.board = board
        # the player which the AI is controlling
        self.player = play
        # the level (difficulty) of the AI
        self.level = int(level)
        # the symbol of the enemy
        self.enemy_symbol = enemy_symbol
        self.path = None
        self.sub_path = None

    def is_winning(self, symbol, num):
        """
        check if a user (Player or AI, depends on the Symbol and number)
        could win with the next move
        """

        # characters for the for-loop
        characters = ["a", "b", "c"]

        # in current_board the return value of self.board.get_board() will be saved
        current_board = []
        # b is a placeholder for the dictionary from the board
        board = self.board.get_board()

        # saves the dictionary from b as a list in current_board
        # that's because if the program simply was current_board = self.board.get_board(),
        # current_board were just a reference to the dictionary of board
        # the AI changes moves in the current board to predict the best move
        # current_board is therefore a save
        # for the current board and
        # the current board will be set to the state of
        # current_board
        # so current_board = self.board.get_board() will not work, because if the
        # AI changes the board in self.board,
        # current_board will also be changed
        for character in characters:
            for i in range(1, 4):
                # adds an Entry in the current_board list
                # list(...) means that the list is no reference but an actual list
                current_board.append(list(board[character + str(i)]))

        # creates a third Player with either the number and symbol of the Player or the AI
        enemy = player.Player(num, symbol, False, "AI")

        # check every field in the board
        for i in characters:

            # check every field in the board
            for number in range(1, 4):
                pos = i + str(number)
                # if a Player could move in pos
                if enemy.move(self.board, pos):

                    win = self.board.is_winning()

                    # sets the board to the "default" state, which is saved in current_board
                    self.board.set_board(
                        {"a1": list(current_board[0]), "a2": list(current_board[1]),
                         "a3": list(current_board[2]), "b1": list(current_board[3]),
                         "b2": list(current_board[4]), "b3": list(current_board[5]),
                         "c1": list(current_board[6]), "c2": list(current_board[7]),
                         "c3": list(current_board[8])})

                    # if the player would win with this move
                    if win:

                        # returns the position of the winning field
                        return pos

        # if no won could win with the next move, return false
        return False

    def move_weak(self):
        """move to a random field"""

        characters = ["a", "b", "c"]

        # while the current move is invalid
        while not self.player.move(self.board, characters[randint(0, 2)] + str(randint(1, 3))):
            # pass
            pass

    def move_middle(self):
        """
        move the AI
        check if the AI or the user could win with the next move
        """

        # in ai_winning is either the position of the field in which the AI wins
        # or False if the AI cannot win with the next move
        ai_winning = self.is_winning(self.player.symbol, self.player.num)

        # if ai_winning is not False
        if ai_winning:
            # move to the field in ai_winning
            # means that the AI wins
            self.player.move(self.board, ai_winning)
        # if ai_winning is False (AI cannot win with the next move)
        else:
            # in enemy is either the position of the field in which the Player wins
            # or False if the Player cannot win with the next move
            enemy = self.is_winning(self.enemy_symbol, self.player.num - 1)

            # if enemy is not False
            if enemy:
                # move to the field in enemy
                # means that the Player cannot win with this field
                self.player.move(self.board, enemy)
            # if enemy is False (Player also cannot win with the next move)
            else:
                # move to a random field
                self.move_weak()

    def is_first_move(self):
        """check if the AI has the first move"""

        # iterate through the game board
        characters = ["a", "b", "c"]
        field = self.board.get_board()

        for i in characters:
            for number in range(1, 4):
                # if a field is not free, return False
                if field[i + str(number)][1] is not None:
                    return False
        # if there are all field free, return true
        return True

    def count_moves(self):
        """returns the number of moves the Player and AI made"""

        characters = ["a", "b", "c"]
        count = 0
        field = self.board.get_board()

        for i in characters:
            for number in range(1, 4):
                # if the current field is not None, add 1 to count
                if field[i + str(number)][1] is not None:
                    count += 1
        return count

    def set_path_attack(self):
        """set the Path for Attack"""

        field = self.board.get_board()

        if field["b2"][0] != " ":
            self.path = 2
            return

        if field["a1"][0] in self.enemy_symbol or field["a3"][0] in self.enemy_symbol or \
                field["c1"][0] in self.enemy_symbol or field["c3"][0] in self.enemy_symbol:
            self.path = 3
            return

        self.path = 1

    def move_path_one(self):
        """Moves in the Path One Pattern"""

        counts = self.count_moves()

        if counts == 2:
            self.set_move_corner()

        elif counts == 4:
            if self.is_winning(self.player.symbol, self.player.num):
                self.player.move(self.board, self.is_winning(self.player.symbol, self.player.num))
            else:
                self.player.move(self.board, "b2")

        else:
            self.player.move(self.board, self.is_winning(self.player.symbol, self.player.num))

    def set_move_corner(self):
        """Sets Moves in a Corner"""

        field = self.board.get_board()
        if field["a1"][1] == self.player.num:
            if field["b1"][0] == " ":
                self.player.move(self.board, "c1")
            else:
                self.player.move(self.board, "a3")

        elif field["a3"][1] == self.player.num:
            if field["b3"][0] == " ":
                self.player.move(self.board, "c3")
            else:
                self.player.move(self.board, "a1")

        elif field["c1"][1] == self.player.num:
            if field["b1"][0] == " ":
                self.player.move(self.board, "a1")
            else:
                self.player.move(self.board, "c3")

        elif field["c3"][1] == self.player.num:
            if field["b3"][0] == " ":
                self.player.move(self.board, "a3")
            else:
                self.player.move(self.board, "c1")

    def move_path_three(self):
        """Moves in the Path Three Pattern"""

        counts = self.count_moves()

        if counts == 2:
            self.set_move_corner()

        elif counts == 4:
            if self.is_winning(self.player.symbol, self.player.num):
                self.player.move(self.board, self.is_winning(self.player.symbol, self.player.num))
            else:
                if not self.player.move(self.board, "a1"):
                    if not self.player.move(self.board, "a3"):
                        if not self.player.move(self.board, "c1"):
                            self.player.move(self.board, "c3")

        else:
            self.player.move(self.board, self.is_winning(self.player.symbol, self.player.num))

    def move_path_two(self):
        """Moves in the Path Two Pattern"""

        counts = self.count_moves()
        field = self.board.get_board()

        if counts == 2:
            if field["a1"][1] == self.player.num:
                self.player.move(self.board, "c3")

            elif field["a3"][1] == self.player.num:
                self.player.move(self.board, "c1")

            elif field["c1"][1] == self.player.num:
                self.player.move(self.board, "a3")

            elif field["c3"][1] == self.player.num:
                self.player.move(self.board, "a1")

        elif counts == 4:
            if self.sub_path is None:
                if field["a1"][0] in self.enemy_symbol or field["a3"][0] in self.enemy_symbol or \
                        field["c1"][0] in self.enemy_symbol or field["c3"][0] in self.enemy_symbol:
                    self.sub_path = True
                else:
                    self.sub_path = False

            if self.sub_path:
                if field["a1"][0] == " ":
                    self.player.move(self.board, "a1")
                elif field["a3"][0] == " ":
                    self.player.move(self.board, "a3")
                elif field["c1"][0] == " ":
                    self.player.move(self.board, "c1")
                elif field["c3"][0] == " ":
                    self.player.move(self.board, "c3")

        else:
            self.move_middle()

    def attack(self):
        """AI Attacks"""

        if self.is_first_move():
            characters = ["a", "c"]
            digits = [1, 3]
            self.player.move(self.board, characters[randint(0, 1)] + str(digits[randint(0, 1)]))
            return

        if self.path is None:
            self.set_path_attack()

        if self.path == 1:
            self.move_path_one()
        if self.path == 2:
            self.move_path_two()
        if self.path == 3:
            self.move_path_three()

    def set_path_defense(self):
        """Sets Path for defense"""

        field = self.board.get_board()

        if field["a1"][0] in self.enemy_symbol or field["a3"][0] in self.enemy_symbol or \
                field["c1"][0] in self.enemy_symbol or field["c3"][0] in self.enemy_symbol:
            self.path = 1

        elif field["b2"][0] == self.enemy_symbol:
            self.path = 2

        else:
            self.path = 3

    def defense_move_path_one(self):
        """Moves in the Path One Pattern"""

        counts = self.count_moves()

        if counts == 1:
            self.player.move(self.board, "b2")

        else:
            self.move_middle()

    def defense_move_path_two(self):
        """Moves in the Path Two Pattern"""

        counts = self.count_moves()

        if counts == 1:
            digits = [1, 3]
            characters = ["a", "c"]
            self.player.move(self.board, characters[randint(0, 1)] + str(digits[randint(0, 1)]))

        else:
            self.move_middle()

    def defense_move_path_three(self):
        """Moves in the Path Three Pattern"""

        counts = self.count_moves()
        field = self.board.get_board()

        if counts == 1:
            self.player.move(self.board, "b2")

        elif counts == 3:
            if not (field["a2"][0] == self.enemy_symbol and field["c2"][0] == self.enemy_symbol):
                if not (field["b1"][0] == self.enemy_symbol
                        and field["b3"][0] == self.enemy_symbol):

                    if field["b1"][0] == self.enemy_symbol:
                        if not self.player.move(self.board, "a1"):
                            self.player.move(self.board, "c1")

                    elif field["a2"][0] == self.enemy_symbol:
                        if not self.player.move(self.board, "a1"):
                            self.player.move(self.board, "a3")

                    elif field["b3"][0] == self.enemy_symbol:
                        if not self.player.move(self.board, "a3"):
                            self.player.move(self.board, "c3")

                    elif field["c2"][0] == self.enemy_symbol:
                        if not self.player.move(self.board, "c1"):
                            self.player.move(self.board, "c3")

                    return

            digits = [1, 3]
            characters = ["a", "c"]
            self.player.move(self.board, characters[randint(0, 1)] + str(digits[randint(0, 1)]))

        elif counts == 5:

            win = self.is_winning(self.player.symbol, self.player.num)
            enemy = self.is_winning(self.enemy_symbol, self.player.num - 1)
            if win:
                self.player.move(self.board, win)
            elif enemy:
                self.player.move(self.board, enemy)

            else:

                characters = ["a", "c"]
                digits = [1, 3]

                for character in characters:
                    for digit in digits:
                        if field[character + str(digit)][0] == " ":
                            self.player.move(self.board, character + str(digit))
                            break

        else:
            self.move_middle()

    def defense(self):
        """AI goes to defense Mode"""

        if self.path is None:
            self.set_path_defense()

        if self.path == 1:
            self.defense_move_path_one()
        if self.path == 2:
            self.defense_move_path_two()
        if self.path == 3:
            self.defense_move_path_three()

    def move_hard(self):
        """AI on difficult Level"""

        if self.count_moves() % 2 == 0:
            self.attack()

        else:
            self.defense()

    def move(self):
        """move function of AI"""

        print("KI überlegt...")

        # if the level of the AI is 1 -> weak AI
        if self.level == 1:
            self.move_weak()
        # if the level of the AI is 2 -> middle AI
        if self.level == 2:
            self.move_middle()
        # if the level of the AI is 3 -> hard AI
        if self.level == 3:
            self.move_hard()

        # sleep because the Player should see "KI überlegt..."
        sleep(2)
