from score import Score
import pytest

@pytest.fixture
def score():
    return Score()

def test_score_initialized_to_zero(score):
    returned_score = score.get()
    assert returned_score == 0, f"Expected {0}, but got {returned_score}"

def test_add_adds_value_to_score(score):
    score.add(300)
    returned_score = score.get()
    assert returned_score == 300, f"Expected {300}, but got {returned_score}"
    score.add(200)
    returned_score = score.get()
    assert returned_score == 500, f"Expected {500}, but got {returned_score}"

def test_reset_resets_score_to_zero(score):
    score.add(300)
    score.reset()
    returned_score = score.get()
    assert returned_score == 0, f"Expected {0}, but got {returned_score}"
