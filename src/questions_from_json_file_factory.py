import json
import random
from question import Question

class QuestionsFromJsonFileFactory():
    def __init__(self, path_to_file: str):
        self.__questions : list[Question] = self.__load_questions(path_to_file)
        random.shuffle(self.__questions)

    def __load_questions(self, path_to_file: str) -> list[Question]:
        questions : list[Question] = []

        try:
            with open(path_to_file) as file:
                questions_data = json.load(file)
                for data in questions_data:
                    questions.append(Question(data['question'], data['choices'], data['correct']))
        except FileNotFoundError as e:
            print("File not found!")

        return questions
    
    def get_total_number_of_questions(self) -> int:
        return len(self.__questions)
    
    def get_question(self, index: int) -> Question:
        if index >= 0 and index < self.get_total_number_of_questions():
            return self.__questions[index]
        else:
            return None