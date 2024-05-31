from question import Question
import pytest
from unittest.mock import patch

question_string = "Welcher Buchstabe gefällt Ihnen am besten?"
answer_strings = ["a", "b", "c", "d"]
correct_answer = "a"

@pytest.fixture
def question():
    return Question(question_string, answer_strings, correct_answer)

def test_get_question_text(question):
    assert question.get_question_text() == question_string, f"Expected {question_string}, but got {question.get_question_text()}"

def test_get_answers_returns_all_answers(question):
    answers = question.get_answers()
    answer_strings_returned = [str(answer) for answer in answers]

    for answer_string in answer_strings:
        assert answer_string in answer_strings_returned, f"Answer string {answer_string} is missing in returned answers"

def test_correct_answer_is_set_correct(question):
    answers = question.get_answers()

    for answer in answers:
        if str(answer) == correct_answer:
            assert answer.is_correct() == True, f"Expected \n{True}, but got \n{answer.is_correct()}."

def test_not_correct_answers_are_not_correct(question):
    answers = question.get_answers()

    for answer in answers:
        if str(answer) != correct_answer:
            assert answer.is_correct() == False, f"Expected \n{False}, but got \n{answer.is_correct()}."

@patch("random.shuffle")
def test_question_init_shuffles_answers(mock_shuffle):
    question = Question(question_string, answer_strings, correct_answer)
    mock_shuffle.assert_called_with(question._Question__answers)

# def test_str_question(question):
#     expected = f"Question: {question_string}\n"
#     for idx, answer in enumerate(question.get_answers()):
#         expected += f"{chr(ord('a') + idx)}) {str(answer)}\n"

#     question_str = str(question)
#     assert question_str == expected, f"Expected \n{expected}, but got \n{question_str}."

