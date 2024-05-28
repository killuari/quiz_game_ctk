from player import Player
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory

class TextBasedGame():
    def __init__(self):
        questions_from_file = QuestionsFromJsonFileFactory("assets/questions.json")
        questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")

    def run(self):
        name = input("Please, enter your name: ")
        player = Player(name)
        print(f"Welcome {player.name()}!")