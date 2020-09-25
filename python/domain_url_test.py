import unittest
from domain_url import domain_name


class DomainNameFromURL(unittest.TestCase):
    def test_http(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name(
            "http://github.com/carbonfive/raygun"), "github")
        self.assertEqual(domain_name(
            "http://www.zombie-bites.com"), "zombie-bites")

    def test_https(self):
        self.assertEqual(domain_name("https://www.cnet.com"), "cnet")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("https://123.net"), "123")

    def test_www(self):
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")


if __name__ == '__main__':
    unittest.main()
