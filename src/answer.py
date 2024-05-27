class Answer():
    def __init__(self, answer_text: str, is_correct_answer: bool):
        self.__answer_text = answer_text
        self.__is_correct_answer = is_correct_answer

    def is_correct(self):
        return self.__is_correct_answer
    
    def __str__(self):
        return self.__answer_text