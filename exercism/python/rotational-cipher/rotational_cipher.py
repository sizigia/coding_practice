from string import ascii_lowercase

def check_uppercase(original_text, translated) -> str:
    """Compare and match cases between characters from two strings of equal length.

    :param original_text: str - original string used to match cases
    :param translate: str - original text that has been translated
    """
    to_upper = lambda idx, char: char.upper() if original_text[idx].isupper() else char
    return ''.join([to_upper(idx, char) for idx, char in enumerate(translated)])


def rotate(text, key) -> str:
    """Translate text with given key using a rotational cipher (Caesar cipher).

    :param text: str - text to translate using a rotational cipher with given key
    :param key: int - number to rotate the Latin alphabet
    :return: str - translated text using rotational cipher
    """
    alphabet = ascii_lowercase
    rot_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = text.maketrans(alphabet, rot_alphabet)

    preliminary_txt = text.lower().translate(translation_table)
    proofread = check_uppercase(text, preliminary_txt)

    return proofread
