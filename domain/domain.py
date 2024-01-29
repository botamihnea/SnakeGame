from texttable import Texttable

class Board:
    def __init__(self):
        size = int(self.get_size())
        self.__board = [["" for _ in range (size)] for _ in range(size)]


    def get_size(self):
        with open("input", "r") as file:
            for line in file:
                line.strip()

                if line == "":
                    continue

                line.split(" ")
                size = line[0]

        return int(size)

    def get_apples(self):
        with open("input", "r") as file:
            for line in file:
                line.strip()

                if line == "":
                    continue

                line.split(" ")
                apples = line[1]

        return int(apples)

    def get_square(self, i, j):
        return self.__board[i][j]

    def set_square(self, i, j, symbol):
        if i < 0 or j < 0 or i > self.get_size() or j > self.get_size():
            raise ValueError("Invalid coordinates!")
        else:
            self.__board[i][j] = symbol


    def __str__(self):
        table = Texttable()
        size = self.get_size()
        print(size)
        for i in range(size):
            added_row = []
            for j in range(size):
                added_row.append(self.__board[i][j])

            table.add_row(added_row)

        return table.draw()

def main():
    board = Board()
    print(board)

main()