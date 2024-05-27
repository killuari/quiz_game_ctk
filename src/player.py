from name import Name
from score import Score
from lives import Lives

class Player():
    def __init__(self, name: Name):
        self.__name = name
        self.__score = Score()
        self.__lives = Lives()