class Score():
    def __init__(self):
        self.__score = 0

    def reset(self):
        self.__score = 0

    def add(self, score: int) -> int:
        self.__score += score
        return self.__score
    
    def get(self) -> int:
        return self.__score