import requests
import random
from question import Question
from questions_factory import QuestionsFactory

class QuestionsFromServerFactory(QuestionsFactory):
    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key
        self.__questions = [None, None, None]

    def get_total_number_of_questions(self) -> int:
        for i in range(3):
            response = requests.get(f"{self.__base_url}/{self.__api_key}/question_count")
            if response.status_code == 200:
                return response.json()['count']
            elif response.status_code == 403:
                return 0
        return 0
    
    def __load_questions(self, difficulty: int) -> list[Question]:
        questions : list[Question] = []
        for idx in range(self.get_total_number_of_questions()):
            question = self.get_question(idx)
            if question.get_difficulty() == difficulty:
                questions.append(question)
        return questions
    
    def reload_questions(self):
        for idx, questions in enumerate(self.__questions):
            if not questions is None:
                random.shuffle(self.__questions[idx])

    def get_question(self, index: int, difficulty: int = None) -> Question:
        if difficulty is None:
            for i in range(3):
                response = requests.get(f"{self.__base_url}/{self.__api_key}/question?index={index}")
                if response.status_code == 200:
                    question_data = response.json()
                    return self._json_to_question(question_data)
                elif response.status_code == 403:
                    return None
            return None
        else:
            if self.__questions[difficulty-1] is None:
                questions = self.__load_questions(difficulty)
                random.shuffle(questions)
                self.__questions[difficulty-1] = questions
            else:
                questions = self.__questions[difficulty-1]

            return questions[index]

