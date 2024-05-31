import json
from score import Score

class Highscore():
    def __init__(self, path_to_file: str):
        self.__highscore_data : list[int] = []
        self.__path_to_file : str = path_to_file
        self.__new_highscore_idx : int = -1
        try:
            with open(self.__path_to_file) as f:
                self.__highscore_data = json.load(f)['highscore_data']
        except FileNotFoundError:
            print("No Highscores found, creating new file!")

    def update(self, score: Score):
        if len(self.__highscore_data) < 10:
            self.__highscore_data.append(score.get())
        elif score.get() > min(self.__highscore_data):
            self.__highscore_data.pop()
            self.__highscore_data.append(score.get()) 
        self.__highscore_data.sort(reverse=True)

        try:
            self.__new_highscore_idx = self.__highscore_data.index(score.get())
        except ValueError:
            print("No new entry in highscores.")
        else:
            print("New highscore entry!")

        with open(self.__path_to_file, 'w+') as f:
            json.dump({"highscore_data" : self.__highscore_data}, f)

    def reset(self):
        with open(self.__path_to_file, 'w+') as f:
            json.dump({"highscore_data" : []}, f)
        self.__highscore_data = []

    def __str__(self):
        if len(self.__highscore_data) == 0:
            line = "No Highscores yet!"
        else:
            line = ""
            for idx, highscore in enumerate(self.__highscore_data):
                line += f"\n#{idx+1}: {highscore}"
        return line
