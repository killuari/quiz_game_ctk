import random
from answer import Answer

class Question():
    def __init__(self, question_text: str, answer_texts: list[str], correct_answer_text: str):
        self.__question_text : str = question_text
        self.__answers: list[Answer] = []

        for answer_text in answer_texts:
            self.__answers.append(Answer(answer_text, answer_text == correct_answer_text))
        self.shuffle_answers()

    def shuffle_answers(self):
        random.shuffle(self.__answers)

    def get_question_text(self) -> str:
        return self.__question_text
    
    def get_answers(self) -> list[Answer]:
        return self.__answers
    
    def get_options(self) -> list[str]:
        return [chr(ord('a') + idx) for idx in range(len(self.get_answers()))]
    
    def __str__(self) -> str:
        question_print = f"{self.get_question_text()}\n"
        for idx, answer in enumerate(self.get_answers()):
            question_print += f"{self.get_options()[idx]}) {answer}\n"

        return question_print

