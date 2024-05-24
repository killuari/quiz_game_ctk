from answer import Answer
import string
import random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def test_constructor_sets_answer_text_to_string():
    expected = "Bla blub"
    answer = Answer(expected, False)
    resulted = answer._Answer__answer_text
    assert resulted == expected, f"answer_text is not set correctly. Expected {expected}, but got {resulted}"

def test_constructor_sets_is_correct_answer_to_passed_value():
    expected = True
    answer1 = Answer("bla blub", expected)
    resulted = answer1._Answer__is_correct_answer
    assert resulted == expected, f"is_correct_answer is not set correctly. Expected {expected}, but got {resulted}"

    expected = False
    answer2 = Answer("bla blub", expected)
    resulted = answer2._Answer__is_correct_answer
    assert resulted == expected, f"is_correct_answer is not set correctly. Expected {expected}, but got {resulted}"

def test_answer_to_string():
    random_string = generate_random_string(16)
    answer = Answer(random_string, False)
    assert random_string == str(answer), f"Expected {random_string}, but got {str(answer)}."

def test_answer_is_correct_is():
    random_string = generate_random_string(16)

    answer1 = Answer(random_string, False)
    assert answer1.is_correct() == False, f"Expected {False}, but got {answer1.is_correct()}."

    answer2 = Answer(random_string, True)
    assert answer2.is_correct() == True, f"Expected {True}, but got {answer1.is_correct()}."
