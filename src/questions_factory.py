from abc import ABC, abstractmethod
from question import Question

class QuestionsFactory(ABC):
    @abstractmethod
    def get_total_number_of_questions() -> int:
        pass

    @abstractmethod
    def get_question(index: int) -> Question:
        pass

    