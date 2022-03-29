from time import sleep
from random import randint


class ai:

    def __init__(self, board, player, level):
        self.board = board
        self.player = player
        self.level = int(level)

    def move_weak(self):

        characters = ["a", "b", "c"]

        while not self.player.move(self.board, characters[randint(0, 2)] + str(randint(1, 3))):
            pass

    def move(self):

        print("KI überlegt...")

        if self.level == 1:
            self.move_weak()
        if self.level == 2:
            pass
        if self.level == 3:
            pass

        sleep(2)
