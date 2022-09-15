import re

def word_beginning(word):
    p = re.compile(r"(?P<vowels>(^[aeiou]|^[xr|yt]{2}))|(^[y]|^[bcdfghjklmnprstvwxz]{,1}qu|^[bcdfghjklmnpqrstvwxz]{,3})")

    for m in p.finditer(word):
        if m.groupdict()['vowels']:
            return word + 'ay'
        else:
            return word[m.end():] + m.group() + 'ay'


def translate(text):
    """Translate a text from English to Pig Latin.

    Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
    Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster (e.g. "chair" -> "airchay").
    Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
    Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").

    :param text: string - text in English to be translated to Pig Latin
    :return: string - text translated to Pig Latin
    """

    return ' '.join(list(map(word_beginning, text.split(' '))))


if __name__ == '__main__':
    print(translate("rhythm"))