from domain.domain import Board
import random

class Service:
    def __init__(self, board):
        self.__board = board
        self.generate_snake()
        self.generate_random_apples()

    def generate_snake(self):
        size = self.__board.get_size()
        self.__board.set_square(size // 2 , size // 2, "+")
        self.__board.set_square(size // 2 - 1, size // 2, "*")
        self.__board.set_square(size // 2 + 1, size // 2, "+")
    def generate_random_apples(self):
        apples = self.__board.get_apples()
        size = self.__board.get_size()
        while apples > 0:
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            if (self.__board.get_square(i, j) == "" and self.__board.get_square(i + 1, j) != "a" and self.__board.get_square(i, j + 1) != "a"
                and self.__board.get_square(i, j - 1) != "a" and self.__board.get_square(i - 1, j) != "a"):
                self.__board.set_square(i, j, "a")
                apples -= 1

    def move(self, steps):
        for i in range(steps):
            size = self.__board.get_size()
            self.__board.set_square(size // 2, size // 2, "+")
            self.__board.set_square(size // 2 - 1, size // 2, "*")
            self.__board.set_square(size // 2 + 1, size // 2, "+")
