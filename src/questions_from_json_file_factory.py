import json
import random
from question import Question
from questions_factory import QuestionsFactory

class QuestionsFromJsonFileFactory(QuestionsFactory):
    def __init__(self, path_to_file: str):
        self.__path_to_file = path_to_file

    def __load_questions(self, difficulty: int) -> list[Question]:
        questions : list[Question] = []

        try:
            with open(self.__path_to_file) as file:
                questions_data = json.load(file)
                for data in questions_data:
                    question = self._json_to_question(data)
                    if question.get_difficulty() == difficulty:
                        questions.append(question)
        except FileNotFoundError as e:
            print("File not found!")

        return questions
    
    def get_total_number_of_questions(self) -> int:
        return len(self.__questions)
    
    def get_question(self, index: int, difficulty: int) -> Question:
        if index >= 0 and index < self.get_total_number_of_questions():
            questions = self.__load_questions(difficulty)
            random.shuffle(questions)
            return questions[index]
        else:
            return None