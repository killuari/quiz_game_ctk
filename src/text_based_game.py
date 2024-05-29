from player import Player
from question import Question
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory

class TextBasedGame():
    def __init__(self):
        self.__questions_from_file = QuestionsFromJsonFileFactory("assets/questions.json")
        self.__questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")

        # Connect to Server
        self.__connected_to_server = True
        try:
            num = self.__questions_from_server.get_total_number_of_questions()
        except Exception:
            self.__connected_to_server = False
        else:
            if num == 0:
                self.__connected_to_server = False

        print(self.__connected_to_server)
        
        name = input("Please, enter your name: ")
        self.__player = Player(name)
        print(f"Welcome {self.__player.name()}!")
    
    def run(self):
        current_question_idx = 0

        while not self.__player.lives().is_game_over():
            current_question = self.__get_question(current_question_idx)
            print(current_question)

            player_answer = ""
            while player_answer not in ['a', 'b', 'c', 'd']:
                player_answer = input("Please, choose either ['a', 'b', 'c', 'd']: ")

            if current_question.get_answers()["abcd".find(player_answer)].is_correct():
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

        print(f"{self.__player.name()}, you have achieved {self.__player.score().get()} points")


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