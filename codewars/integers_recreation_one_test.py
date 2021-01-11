import unittest
from integers_recreation_one import list_squared


class ListSquaredTest(unittest.TestCase):
    def test_(self):
        self.assertEqual(list_squared(1, 250), [
            [1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])


if __name__ == '__main__':
    unittest.main()
