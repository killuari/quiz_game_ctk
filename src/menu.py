from text_based_game import TextBasedGame
from player import Player
from highscore import Highscore

class Menu():
    def __init__(self):
        self.__options = ["Play", "View highscore", "Exit game"]
        self.__highscore = Highscore("assets/highscore.json")

        name = input("Please, enter your name: ")
        self.__player = Player(name)
        print(f"Welcome {self.__player.name()}!")

        self.__game = TextBasedGame(self.__player, self.__highscore)

    def __str__(self) -> str:
        line = "------Quizking------"
        for idx, option in enumerate(self.__options):
            line += f"\n{chr(ord('a') + idx)}) {option}"
        return line

    def __play(self):
        self.__game.run()
        self.__player.reset()

    def __view_highscore(self):
        print(self.__highscore)

    def __exit_game(self):
        quit()

    def __get_input(self):
        choice = ""
        while choice not in ['a', 'b', 'c']:
            choice = input("Please, choose either ['a', 'b', 'c']: ")
        print()
        match choice:
            case 'a': self.__play()
            case 'b': self.__view_highscore()
            case 'c': self.__exit_game()

    def run(self):
        while True:
            print(self)
            self.__get_input()