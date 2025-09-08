import pytest
from unittest.mock import patch

from my_module import find_first_unique_char
import my_module


@pytest.mark.parametrize("text,result", [
    ("abbbccdf", "a"),
    ("aabbcdeeff", "c"),
    ("aabbcc", None),
    ("@@@!!! 2342342", " ")
    
])
def test_find_first_unique_char(text, result):
    assert find_first_unique_char(text) == result


@pytest.mark.parametrize("wrong_text", [
    None,
    1,
    1.3,
    [],
    {"e": "error"},
    ("tuple", ),
    {1, 2, 3},
    True,
])
def test_find_first_unique_char_with_wrong_input(wrong_text):
    with pytest.raises(TypeError):
        find_first_unique_char(wrong_text)
