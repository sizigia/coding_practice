import unittest
from sum_of_intervals import sum_of_intervals


class TestSumIntervals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (4, 10)]), 9)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
        self.assertEqual(sum_of_intervals([(-11, 353), (465, 475), (197, 389), (-386, 64), (85, 291), (-315, 127), (27, 381),
                                           (-115, 69), (261, 473), (-441, 220), (-182, -138), (488, 493), (-235, 341), (293, 338), (454, 486)]), 932)
        self.assertEqual(sum_of_intervals([(-228, 314), (-121, 400), (-159, -66), (-323, 358), (433, 483),
                                           (-28, 55), (-443, -26), (221, 332), (419, 424), (2, 161), (477, 496), (-140, 172)]), 911)


if __name__ == "__main__":
    unittest.main()
