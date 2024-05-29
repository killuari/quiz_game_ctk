import json
from score import Score

class Highscore():
    def __init__(self, path_to_file: str):
        self.__highscore_data : list = []
        self.__path_to_file : str = path_to_file
        try:
            with open(self.__path_to_file) as f:
                self.__highscore_data = json.load(f)['highscore_data']
        except FileNotFoundError:
            print("No Highscores found, creating new file!")
            with open(self.__path_to_file, 'w+') as f:
                json.dump({"highscore_data" : []}, f)

    def update(self, score: Score):
        if len(self.__highscore_data) < 10:
            self.__highscore_data.append(score.get())
        elif score.get() > min(self.__highscore_data):
            print(self.__highscore_data.pop(0))
            self.__highscore_data.append(score.get()) 
        self.__highscore_data.sort()

        with open(self.__path_to_file, 'w+') as f:
            json.dump({"highscore_data" : self.__highscore_data}, f)