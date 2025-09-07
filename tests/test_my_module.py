import pytest

from my_module import shift_words


@pytest.mark.parametrize("text,shift,out_text", [
    ("abcd", 1, "bcde"),
    ("abcd efgh", 1, "bcde fghi"),
    ("abcd efgh", 2, "cdef ghij"),
    ("ab1cd", 1, "bc1de"),
    ("abcd efg1h", 1, "bcde fgh1i"),
    ("abcd efg1h", -1, "zabc def1g"),
])
def test_shift_words(text, shift, out_text):
    assert shift_words(text, shift) == out_text


@pytest.mark.parametrize("text,shift", [
    ("hello", "2"),
    ("hello", "abc"),
    ("hello", ""),
    (123, 2),
    (None, 2),
    ([], 2),
    ({}, 2),
    (123, "abc"),
    (None, None),
])
def test_shift_words_raises_type_error(text, shift):
    with pytest.raises(TypeError):
        shift_words(text, shift)
