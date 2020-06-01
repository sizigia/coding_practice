import unittest
from sentence_smash import smash

class SentenceSmashTest(unittest.TestCase):
    def test_one_word_smash(self):
        self.assertEqual(smash(["hello"]), "hello")

    def test_two_words_smash(self):
        self.assertEqual(smash(["hello", "world"]), "hello world")


if __name__ == "__main__":
    unittest.main()