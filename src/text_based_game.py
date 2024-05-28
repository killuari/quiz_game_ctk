from player import Player
from question import Question
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory

class TextBasedGame():
    def __init__(self):
        self.questions_from_file = QuestionsFromJsonFileFactory("assets/questions.json")
        self.questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")

    def run(self):
        name = input("Please, enter your name: ")
        player = Player(name)
        print(f"Welcome {player.name()}!")

        if not player.lives().is_game_over():
            pass

    def get_question(self, index: int) -> Question:
        question_from_server = self.questions_from_server.get_question(index)
        if not question_from_server is None:
            return question_from_server
        else:
            return self.questions_from_file.get_question(index)

    def get_total_number_of_questions(self) -> int:
        if self.questions_from_server.get_total_number_of_questions() != 0:
            return self.questions_from_server.get_total_number_of_questions()
        else:
            return self.questions_from_file.get_total_number_of_questions()