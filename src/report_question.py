from question import Question
import requests

class ReportQuestion():
    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key
        self.__reported : list[int] = []

    def on_question_report(self, question: Question):
        if question.get_id() not in self.__reported:
            try:
                response = requests.post(f"{self.__base_url}/{self.__api_key}/report_question", json={"id": question.get_id()})
                self.__reported.append(question.get_id())
                print(response.json())
            except Exception as e:
                print("Server POST Request Error")