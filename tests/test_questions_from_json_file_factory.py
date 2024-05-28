import pytest
from unittest.mock import patch, mock_open
import json
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from question import Question

# Assuming these classes are imported from the module
# from your_module import Question, QuestionsFromJsonFileFactory

# Sample JSON data for testing
sample_json_data = json.dumps([
    {
        "question": "What is the capital of France?",
        "choices": [
            "Paris",
            "London",
            "Berlin",
            "Madrid"
        ],
        "correct": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "choices": [
            "4",
            "3",
            "5",
            "6"
        ],
        "correct": "4"
    }
])

# Tests

# Patch random.shuffle to be a no-op
def no_op_shuffle(lst):
    pass

@patch('random.shuffle', no_op_shuffle)
def test_initiaization_creates_array_of_questions():
    with patch('builtins.open', mock_open(read_data=sample_json_data)):
        factory = QuestionsFromJsonFileFactory('path/to/file')
        assert factory is not None
        assert len(factory._QuestionsFromJsonFileFactory__questions) == 2  # Since we have 2 questions in the sample data
        for question in factory._QuestionsFromJsonFileFactory__questions:
            assert type(question) == Question, f"Wrong type in list of questions. Got {type(question)}, but expected Question"

@patch('random.shuffle', no_op_shuffle)
def test_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        factory = QuestionsFromJsonFileFactory('path/to/nonexistent/file')
        assert factory is not None
        assert len(factory._QuestionsFromJsonFileFactory__questions) == 0

@patch('random.shuffle', no_op_shuffle)
def test_get_total_number_of_questions():
    with patch('builtins.open', mock_open(read_data=sample_json_data)):
        factory = QuestionsFromJsonFileFactory('path/to/file')
        assert factory.get_total_number_of_questions() == 2

    with patch('builtins.open', side_effect=FileNotFoundError):
        factory = QuestionsFromJsonFileFactory('path/to/nonexistent/file')
        assert factory.get_total_number_of_questions() == 0

@patch('random.shuffle', no_op_shuffle)
def test_get_question_if_loading_file_fails():
    with patch('builtins.open', side_effect=FileNotFoundError):
        factory = QuestionsFromJsonFileFactory('path/to/nonexistent/file')
        assert factory.get_question(0) is None

@patch('random.shuffle', no_op_shuffle)
def test_get_total_number_of_questions_if_loading_file_fails():
    with patch('builtins.open', side_effect=FileNotFoundError):
        factory = QuestionsFromJsonFileFactory('path/to/nonexistent/file')
        assert factory.get_total_number_of_questions() == 0

@patch('random.shuffle', no_op_shuffle)
def test_get_question_if_index_is_in_bounds():
    with patch('builtins.open', mock_open(read_data=sample_json_data)):
        factory = QuestionsFromJsonFileFactory('path/to/file')
        question = factory.get_question(0)
        assert question is not None
        assert question.get_question_text() == "What is the capital of France?"

        question = factory.get_question(1)
        assert question is not None
        assert question.get_question_text() == "What is 2 + 2?"

@patch('random.shuffle', no_op_shuffle)
def test_get_question_if_index_is_out_of_bounds():
    with patch('builtins.open', mock_open(read_data=sample_json_data)):
        factory = QuestionsFromJsonFileFactory('path/to/file')
        assert factory.get_question(2) is None
        assert factory.get_question(-1) is None
