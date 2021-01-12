import unittest
from reverse_sequence import reverse_seq


class ReverseSequenceTest(unittest.TestCase):
    def test_reverse_5(self):
        self.assertEqual(reverse_seq(5), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
