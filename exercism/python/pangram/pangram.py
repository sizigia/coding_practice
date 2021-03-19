from string import ascii_lowercase


def is_pangram(sentence):
    sentence = set(sentence.lower())
    abecedary = set(ascii_lowercase)

    return abecedary.issubset(sentence)
