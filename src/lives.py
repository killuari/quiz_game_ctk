class Lives():
    __INITIAL_LIVES = 3
    def __init__(self):
        self.__lives = Lives.__INITIAL_LIVES
    
    def reset(self):
        self.__lives = Lives.__INITIAL_LIVES

    def loose_a_life(self):
        if self.__lives > 0:
            self.__lives -= 1

    def is_game_over(self) -> bool:
        return self.__lives == 0
    
    def get(self) -> int:
        return self.__lives
