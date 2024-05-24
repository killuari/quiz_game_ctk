from name import Name
import pytest

player_name = "Hugo"

@pytest.fixture
def name():
    return Name(player_name)

def test_str_returns_correct_name(name):
    returned_name_string = str(name)
    assert returned_name_string == player_name, f"Expected {player_name}, but got {returned_name_string}"
