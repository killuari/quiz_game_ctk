import responses
import requests_mock
from questions_from_server_factory import QuestionsFromServerFactory
import pytest
from question import Question

api_key = "this_is_the_correct_api_key"


def questions_equal(question1, question2):
    if not isinstance(question2, Question):
        return False
    if question1.get_question_text() != question2.get_question_text():
        return False
    if len(question1.get_answers()) != len(question2.get_answers()):
        return False

    # Sort answers by their text and compare
    question1_sorted_answers = sorted(question1.get_answers(), key=lambda ans: str(ans))
    question2_sorted_answers = sorted(question2.get_answers(), key=lambda ans: str(ans))
    for self_ans, other_ans in zip(question1_sorted_answers, question2_sorted_answers):
        if str(self_ans) != str(other_ans) and self_ans.is_correct() != other_ans.is_correct():
            return False
    return True

@pytest.fixture
def question_factory():
    base_url = "http://127.0.0.1:5000"
    return QuestionsFromServerFactory(base_url, api_key)

def test_question_factory_stores_base_url_in_private_member():
    base_url = "http://test123test:1234"
    question_factory = QuestionsFromServerFactory(base_url, api_key)
    assert hasattr(question_factory, '_QuestionsFromServerFactory__base_url') is True, "There is no private member variable named base_url"
    assert question_factory._QuestionsFromServerFactory__base_url == base_url, "Base URL is not stored correctly in the private member variable base_url"

@responses.activate
def test_question_count_is_returned_correctly(question_factory):
    expected = 111
    mock_response = {"count": expected}

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json=mock_response,
        status=200
    )

    returned = question_factory.get_total_number_of_questions()
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 1, f"Expected only one request, but {responses.calls} were made."

# @responses.activate
# def test_question_is_returned_correctly(question_factory):
#     mock_response = {
#         "question": "What is the largest planet in our Solar System?",
#         "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
#         "correct": "Jupiter"
#     }

#     question = Question(mock_response["question"], mock_response["choices"], mock_response["correct"])

#     # Mock the API endpoint
#     responses.add(
#         responses.GET,
#         f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question?index=0",
#         json=mock_response,
#         status=200
#     )

#     returned = question_factory.get_question(0)

#     assert questions_equal(returned, question), f"Question is not correct. Expected {question}, but got {returned}."
#     assert len(responses.calls) == 1, f"Expected only one request, but {responses.calls} were made."

@responses.activate
def test_count_is_zero_if_request_fails(question_factory):
    expected = 0

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={},
        status=404
    )
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={},
        status=404
    )
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={},
        status=404
    )
    returned = question_factory.get_total_number_of_questions()
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 3, f"Expected three requests, but {responses.calls} were made."

@responses.activate
def test_question_is_none_if_request_fails(question_factory):
    expected = None

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question",
        json={},
        status=404
    )
    returned = question_factory.get_question(0)
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 3, f"Expected three requests, but {responses.calls} were made."

@responses.activate
def test_count_is_returned_correctly_it_third_request_is_successful(question_factory):
    expected = 111
    mock_response = {"count": expected}

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={},
        status=404
    )
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={},
        status=404
    )
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json=mock_response,
        status=200
    )

    returned = question_factory.get_total_number_of_questions()
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 3, f"Expected three requests, but {responses.calls} were made."

@responses.activate
def test_count_is_returned_zero_directly_if_api_key__reported_to_be_wrong(question_factory):
    expected = 0

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question_count",
        json={"error": "Unauthorized"},
        status=403
    )

    returned = question_factory.get_total_number_of_questions()
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 1, f"Expected only one request, but {responses.calls} were made."

@responses.activate
def test_count_is_returned_none_directly_if_api_key_wrong(question_factory):
    expected = None

    # Mock the API endpoint
    responses.add(
        responses.GET,
        f"{question_factory._QuestionsFromServerFactory__base_url}/{api_key}/question",
        json={"error": "Unauthorized"},
        status=403
    )

    returned = question_factory.get_question(0)
    assert expected == returned, f"Expected {expected}, but got {returned}."
    assert len(responses.calls) == 1, f"Expected only one request, but {responses.calls} were made."
