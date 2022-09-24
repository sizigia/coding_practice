from collections import Counter
import re

def is_isogram(string):
    """Determine if a given string constitutes an isogram
    a word or phrase without a repeating letter. However, spaces and hyphens
    are allowed to appear multiples.

    :param string: str - word or phrase to determine if it's an isogram
    :return: bool - True is the given string is an isogram, False if it's not.
    """
    if not len(string):
        return not len(string)
    else:
        string = re.sub('[^a-zA-Z]+', '', string).lower()
        letters_frequency = Counter(string)

        return set(letters_frequency.values()) == {1}