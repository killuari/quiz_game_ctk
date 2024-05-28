import requests

class QuestionsFromServerFactory():
    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def get_total_number_of_questions(self) -> int:
        for i in range(3):
            response = requests.get(f"{self.__base_url}/{self.__api_key}/question_count")
            if response.status_code == 200:
                return response.json()['count']
            elif response.status_code == 403:
                return 0
        return 0
    