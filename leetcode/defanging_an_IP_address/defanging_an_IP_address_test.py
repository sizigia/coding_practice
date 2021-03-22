import unittest

from defanging_an_IP_address import Solution


class DefangingIPTest(unittest.TestCase):

    def test_simple_IP_address(self):
        address = "1.1.1.1"

        self.assertEqual(Solution().defangIPaddr(address),
                         "1[.]1[.]1[.]1")

    def test_complex_IP_address(self):
        address = "255.100.50.0"

        self.assertEqual(Solution().defangIPaddr(address),
                         "255[.]100[.]50[.]0")


if __name__ == '__main__':
    unittest.main()
