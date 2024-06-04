from abc import ABC, abstractmethod
from question import Question

class QuestionsFactory(ABC):
    @abstractmethod
    def get_total_number_of_questions(self) -> int:
        pass

    @abstractmethod
    def get_question(self, index: int, difficulty: int) -> Question:
        pass

    @abstractmethod
    def reload_questions(self) -> None:
        pass

    def _json_to_question(self, json: dict) -> Question:
        return Question(json['id'], json['question'], json['choices'], json['correct'], json['difficulty'], json['image'])