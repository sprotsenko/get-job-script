import unittest
from url_utils import read_urls_from_file

class TestUrlUtils(unittest.TestCase):
    def test_read_urls_from_file(self):
        # Simulate a file with URLs
        with open('test_urls.txt', 'w') as f:
            f.write('https://example.com\nhttps://example.org\n')

        urls = read_urls_from_file('test_urls.txt')
        self.assertEqual(urls, ['https://example.com', 'https://example.org'])

if __name__ == '__main__':
    unittest.main()