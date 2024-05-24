from player import Player
from lives import Lives
from score import Score
from name import Name
import pytest

player_name = "Hugo"

@pytest.fixture
def player():
    return Player(player_name)

def test_name_is_initalized(player):
    returned = str(player.name())
    assert str(player.name()) == player_name, f"Expected {player_name}, but got {returned}."

def test_lives_returns_type_lives(player):
    expected_type = Lives
    returned_type = type(player.lives())
    assert returned_type == expected_type, f"Expected return type {expected_type}, but got {returned_type}."

def test_lives_returns_member_object(player):
    expected_object = player._PLAYER__lives
    returned_object = player.lives()
    assert returned_object == expected_object, f"Function lives() is not returning the member object `lives`"

def test_score_returns_type_score(player):
    expected_type = Score
    returned_type = type(player.score())
    assert returned_type == expected_type, f"Expected return type {expected_type}, but got {returned_type}."

def test_score_returns_member_object(player):
    expected_object = player._PLAYER__score
    returned_object = player.score()
    assert returned_object == expected_object, f"Function score() is not returning the member object `score`"

def test_name_returns_type_name(player):
    expected_type = Name
    returned_type = type(player.name())
    assert returned_type == expected_type, f"Expected return type {expected_type}, but got {returned_type}."

def test_name_returns_member_object(player):
    expected_object = player._PLAYER__name
    returned_object = player.name()
    assert returned_object == expected_object, f"Function name() is not returning the member object `name`"

def test_reset_resets_lives_and_score(player):
    player.lives().loose_a_life()
    player.score().add(150)
    player.reset()
    lives_after_reset = player.lives().get()
    assert lives_after_reset == player.lives()._Lives__INITIAL_LIVES, f"Player's lives have not been reset. Expected {player.lives()._Lives__INITIAL_LIVES}, but got {lives_after_reset}"
    score_after_reset = player.score().get()
    assert player.score().get() == 0, f"Player score has not been reset. Expected 0, but got {score_after_reset}."
