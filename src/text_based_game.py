from player import Player
from question import Question
from highscore import Highscore
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory

class TextBasedGame():
    def __init__(self):
        self.__questions_from_file = QuestionsFromJsonFileFactory("assets/questions_with_variying_answers.json")
        self.__questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")
        self.__highscore = Highscore("assets/highscore.json")

        # Connect to Server
        self.__connected_to_server = True
        try:
            num = self.__questions_from_server.get_total_number_of_questions()
        except Exception:
            self.__connected_to_server = False
        else:
            if num == 0:
                self.__connected_to_server = False

        print(f"Connected to Server: {self.__connected_to_server}\n")
        
        name = input("Please, enter your name: ")
        self.__player = Player(name)
        print(f"Welcome {self.__player.name()}!")
    
    def run(self):
        current_question_idx = 0

        while not self.__player.lives().is_game_over():
            current_question = self.__get_question(current_question_idx)
            print(current_question)

            player_answer = ""
            while player_answer not in current_question.get_options():
                player_answer = input(f"Please, choose either {current_question.get_options()}: ")

            if current_question.get_answers()[current_question.get_options().index(player_answer)].is_correct():
                print("\nCorrect!")
                self.__player.score().add(100)
                print(f"Your score is {self.__player.score().get()}\n")
                current_question_idx += 1
            else:
                print("\nIncorrect!")
                self.__player.lives().loose_a_life()
                print(f"Remaining lives: {self.__player.lives().get()}\n")

            if current_question_idx >= self.__get_total_number_of_questions():
                current_question_idx = 0

        print(f"{self.__player.name()}, you have achieved {self.__player.score().get()} points!")

        self.__highscore.update(self.__player.score())
        print(f"\n{self.__highscore}")


    def __get_question(self, index: int) -> Question:
        if self.__connected_to_server:
            question_from_server = self.__questions_from_server.get_question(index)
            if not question_from_server is None:
                return question_from_server
        return self.__questions_from_file.get_question(index)

    def __get_total_number_of_questions(self) -> int:
        if self.__connected_to_server:
            if self.__questions_from_server.get_total_number_of_questions() != 0:
                return self.__questions_from_server.get_total_number_of_questions()
        return self.__questions_from_file.get_total_number_of_questions()