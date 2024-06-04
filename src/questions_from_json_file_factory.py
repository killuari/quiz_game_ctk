import json
import random
from question import Question
from questions_factory import QuestionsFactory

class QuestionsFromJsonFileFactory(QuestionsFactory):
    def __init__(self, path_to_file: str):
        self.__path_to_file = path_to_file
        self.__all_questions = self.__load_questions()
        self.__questions = [None, None, None]

    def __load_questions(self, difficulty: int = None) -> list[Question]:
        questions : list[Question] = []
        try:
            with open(self.__path_to_file) as file:
                questions_data = json.load(file)
                for idx, data in enumerate(questions_data):
                    question = self._json_to_question(data, idx)
                    if difficulty is None:
                        questions.append(question)
                    elif question.get_difficulty() == difficulty:
                        questions.append(question)
        except FileNotFoundError as e:
            print("File not found!")

        return questions
    
    def reload_questions(self):
        for idx, questions in enumerate(self.__questions):
            if not questions is None:
                random.shuffle(self.__questions[idx])
    
    def get_total_number_of_questions(self) -> int:
        return len(self.__all_questions)
    
    def get_question(self, index: int, difficulty: int) -> Question:
        if index >= 0 and index < self.get_total_number_of_questions():
            if self.__questions[difficulty-1] is None:
                questions = self.__load_questions(difficulty)
                random.shuffle(questions)
                self.__questions[difficulty-1] = questions
            else:
                if index < len(self.__questions[difficulty-1]):
                    questions = self.__questions[difficulty-1]
                else:
                    return None
            return questions[index]
        else:
            return None