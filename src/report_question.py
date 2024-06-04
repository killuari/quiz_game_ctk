from question import Question

class ReportQuestion():
    def __init__(self):
        self.__question = None

    def on_question_report(self):
        pass

    def set_question(self, question: Question):
        self.__question = question