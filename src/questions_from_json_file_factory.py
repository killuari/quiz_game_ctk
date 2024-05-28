import json
from question import Question

class QuestionsFromJsonFileFactory():
    def __init__(self, path_to_file: str):
        self.__questions : list[Question] = self.__load_questions(path_to_file)

    def __load_questions(self, path_to_file: str) -> list[Question]:
        questions : list[Question] = []

        with open(path_to_file) as file:
            questions_data = json.load(file)
            for data in questions_data:
                questions.append(Question(data['question'], data['choices'], data['correct']))

        return questions