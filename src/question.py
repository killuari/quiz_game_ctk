import random
from answer import Answer
from PIL import Image

class Question():
    def __init__(self, id: int, question_text: str, answer_texts: list[str], correct_answer_text: str, difficulty: int, image: str):
        self.__id = id
        self.__question_text : str = question_text
        self.__difficulty = difficulty
        self.__answers: list[Answer] = []
        self.__image: str = image

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
    
    def get_difficulty(self) -> int:
        return self.__difficulty
    
    def get_id(self) -> int:
        return self.__id
    
    def get_image(self) -> Image:
        image = None
        if self.__image != "":
            try:
                image = Image.open(self.__image)
            except Exception:
                print(f"Could not open Image from path {self.__image}")
        return image
    
    def __str__(self) -> str:
        question_print = ""
        for idx, answer in enumerate(self.get_answers()):
            question_print += f"{self.get_options()[idx]}) {answer}\n"

        return question_print

