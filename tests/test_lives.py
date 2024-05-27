from lives import Lives
import pytest

@pytest.fixture
def lives():
    return Lives()

def test_static_initial_lives_equals_to_three():
    assert Lives._Lives__INITIAL_LIVES == 3, f"Expected INITIAL_LIVES to equal 3, but got {Lives._Lives__INITIAL_LIVES}"

def test_number_of_lives_is_three(lives):
    expected = 3
    returned = lives.get()
    assert returned == expected, f"Number of initial lives expected {expected}, but got {returned}"

def test_get_returns_number_of_remaining_lives(lives):
    expected = 1
    lives._Lives__lives = 1
    returned = lives.get()
    assert returned == expected, f"Number of lives expected {expected}, but got {returned}"

def test_reset_lives(lives):
    expected = 3

    lives._Lives__lives = 0
    lives.reset()
    returned = lives.get()
    assert returned == expected, f"Number of lives expected {expected}, but got {returned}"

def test_loose_a_life(lives):
    expected_values = [2, 1, 0, 0, 0, 0, 0, 0]
    for expected in expected_values:
        lives.loose_a_life()
        returned = lives.get()
        assert returned == expected, f"Number of lives expected {expected}, but got {returned}"


def test_is_game_over(lives):
    expected_values = [False, False, True, True, True, True]
    for expected in expected_values:
        lives.loose_a_life()
        returned = lives.is_game_over()
        assert returned == expected, f"Expected {expected}, but got {returned}"

def test_is_not_game_over_after_reset(lives):
    expected = False
    for i in range(5):
        lives.loose_a_life()
    
    lives.reset()
    returned = lives.is_game_over()
    assert returned == False, f"Expected {expected}, but got {returned}"