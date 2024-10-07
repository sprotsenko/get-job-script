import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_utils import log_to_file, clear_file

class TestLogUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_log.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_log_to_file(self):
        log_to_file(self.test_file, 'Test log entry')
        with open(self.test_file, 'r') as f:
            content = f.read().strip()
        self.assertEqual(content, 'Test log entry')

    def test_clear_file(self):
        with open(self.test_file, 'w') as f:
            f.write('Some content')
        clear_file(self.test_file)
        with open(self.test_file, 'r') as f:
            content = f.read().strip()
        self.assertEqual(content, '')

if __name__ == '__main__':
    unittest.main()