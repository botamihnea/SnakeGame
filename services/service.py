from domain.domain import Board
import random

class Service:
    def __init__(self, board):
        self.__board = board
        self.generate_snake()
        self.generate_random_apples()

    def generate_snake(self):
        size = self.__board.get_size()
        self.__board.set_square(size // 2 + 1, size // 2 + 1, "+")
        self.__board.set_square(size // 2, size // 2 + 1, "*")
        self.__board.set_square(size // 2 + 2, size // 2 + 1, "+")
    def generate_random_apples(self):
        apples = self.__board.get_apples()
        size = self.__board.get_size()
        while apples:
            i = random.randint(0, size)
            j = random.randint(0, size)
            if (self.__board.get_square(i, j) == "" and self.__board.get_square(i + 1, j) != "a" and self.__board.get_square(i, j + 1) != "a"
                and self.__board.get_square(i, j - 1) != "a" and self.__board.get_square(i - 1, j) != "a"):
                self.__board.set_square(i, j, "a")
                apples -= 1
