import json
from player import Player
from score import Score

class Highscore():
    def __init__(self, path_to_file: str):
        self.__highscore_data : dict = {}
        self.__path_to_file : str = path_to_file
        try:
            with open(self.__path_to_file) as f:
                self.__highscore_data = json.load(f)
        except FileNotFoundError:
            print("No Highscores found, creating new file!")

    def update(self, player: Player):
        if str(player.name()) in self.__highscore_data:
            if player.score().get() > self.__highscore_data[str(player.name())]:
                self.__highscore_data[str(player.name())] = player.score().get()
        else:
            self.__highscore_data[str(player.name())] = player.score().get()

        with open(self.__path_to_file, 'w+') as f:
            json.dump(self.__highscore_data, f)

    def reset(self):
        self.__highscore_data = {}
        with open(self.__path_to_file, 'w+') as f:
            json.dump(self.__highscore_data, f)

    def __get_sorted_highscore_keys(self) -> list[str]:
        sorted_highscore_keys = []
        not_used_highscore_data = self.__highscore_data.copy()
        for i in range(len(self.__highscore_data.keys())):
            idx = list(not_used_highscore_data.values()).index(max(not_used_highscore_data.values()))
            key = list(not_used_highscore_data.keys())[idx]
            not_used_highscore_data.pop(key)
            sorted_highscore_keys.append(key)
        return sorted_highscore_keys

    def __str__(self):
        if len(self.__highscore_data.keys()) == 0:
            line = "No Highscores yet!"
        else:
            line = ""
            idx = 0
            last_score = -1
            for key in self.__get_sorted_highscore_keys():
                score = self.__highscore_data[key]
                if score != last_score:
                    idx += 1
                last_score = score
                line += f"\n#{idx} - {key}: {score}"
        return line
