# import pytest
# from questions_factory import QuestionsFactory

# def test_abstract_methods():
#     abstract_methods = QuestionsFactory.__abstractmethods__
#     assert abstract_methods is not None, "No abstract methods found"
#     assert 'get_question' in abstract_methods, "get_question not found in abstract methods"
#     assert 'get_total_number_of_questions' in abstract_methods, "get_total_number_of_questions not found in abstract methods"

# class TestClass(QuestionsFactory):
#     def get_question(self):
#         return None
    
#     def get_total_number_of_questions(self):
#         return 0
    
#     def question_to_json(self, json):
#         return super()._json_to_question(json)

# def test_json_to_question():
#     question_json = {
#         "question": "What is the largest planet in our Solar System?",
#         "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
#         "correct": "Jupiter"
#     }

#     test = TestClass()
#     question = test.question_to_json(question_json)
#     assert question.get_question_text() == question_json["question"]
#     answers = question.get_answers()
#     answer_strings_returned = [str(answer) for answer in answers]

#     for answer_string in question_json["choices"]:
#         assert answer_string in answer_strings_returned, f"Answer string {answer_string} is missing in returned answers"

