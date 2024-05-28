import requests

class QuestionsFromServerFactory():
    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def get_total_number_of_questions(self) -> int:
        response = requests.get(f"{self.__base_url}/{self.__api_key}/question_count")
        return response.json()['count']