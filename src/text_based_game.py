from player import Player
from question import Question
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory

class TextBasedGame():
    def __init__(self):
        self.__questions_from_file = QuestionsFromJsonFileFactory("assets/questions.json")
        self.__questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")

    def run(self):
        name = input("Please, enter your name: ")
        player = Player(name)
        print(f"Welcome {player.name()}!")
        current_question_idx = 0

        while not player.lives().is_game_over():
            current_question = self.get_question(current_question_idx)
            print(current_question)
            player_answer = input("Please, choose either ['a', 'b', 'c', 'd']: ")

            if current_question.get_answers()["abcd".find(player_answer)].is_correct():
                print("\nCorrect!")
                player.score().add(100)
                print(f"Your score is {player.score().get()}\n")
                current_question_idx += 1
            else:
                print("\nIncorrect!")
                player.lives().loose_a_life()
                print(f"Remaining lives: {player.lives().get()}\n")

            if current_question_idx >= self.get_total_number_of_questions():
                current_question_idx = 0

        print(f"{player.name()}, you have achieved {player.score().get()} points")


    def get_question(self, index: int) -> Question:
        question_from_server = self.__questions_from_server.get_question(index)
        if not question_from_server is None:
            return question_from_server
        else:
            return self.__questions_from_file.get_question(index)

    def get_total_number_of_questions(self) -> int:
        if self.__questions_from_server.get_total_number_of_questions() != 0:
            return self.__questions_from_server.get_total_number_of_questions()
        else:
            return self.__questions_from_file.get_total_number_of_questions()