from services.service import *

class UI:
    def __init__(self):
        self.__board = Board()
        self.__service = Service(self.__board)


    def run_ui(self):
        print(self.__board)