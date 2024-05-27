from name import Name
from score import Score
from lives import Lives

class Player():
    def __init__(self, name: str):
        self.__name = Name(name)
        self.__score = Score()
        self.__lives = Lives()

    def reset(self):
        self.__score.reset()
        self.__lives.reset()

    def lives(self) -> Lives:
        return self.__lives
    
    def score(self) -> Score:
        return self.__score
    
    def name(self) -> Name:
        return self.__name