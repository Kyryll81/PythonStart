from string import ascii_lowercase, ascii_uppercase


def shift_words(text: str, shift: int) -> str:
    if not isinstance(shift, int):
        raise TypeError("Wrong usage of shift.")
    
    if isinstance(text, dict) or isinstance(text, list):
        raise TypeError("Text can't be list or dict.")
    
    output_text: str = ""
    letter_shift = lambda l, alphabet: alphabet[(alphabet.find(l) + shift) % len(alphabet)]

    for letter in text:
        if letter.isalpha():
            alphabet: str = ascii_lowercase if letter.islower() else ascii_uppercase
            output_text += letter_shift(letter, alphabet)
        else:
            output_text += letter
    return output_text


if __name__ == '__main__':
    test_string = "abcd efgh"
    shifted_text = shift_words(test_string, 2)
    print(f"Оригінал: '{test_string}'")
    print(f"Результат: '{shifted_text}'")