import unittest
from unittest.mock import patch, MagicMock
from fetch_jobs import fetch_jobs



class TestFetchJobs(unittest.TestCase):

    @patch('fetch_jobs.requests.get')
    def test_fetch_jobs_success(self, mock_get):
        # Мокаємо успішну відповідь
        mock_html = '''
        <html>
        <body>
            <a href="/job/123">Technical Writer</a>
            <a href="/job/124">Software Engineer</a>
        </body>
        </html>
        '''
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_html

        result = fetch_jobs('https://example.com/careers', ['technical writer'])
        expected = ['- Technical Writer | https://example.com/careers/job/123']

        self.assertEqual(result, expected)


class TestFetchJobs(unittest.TestCase):

    @patch('fetch_jobs.requests.get')
    def test_fetch_jobs_no_matches(self, mock_get):
        # Мокаємо успішну відповідь без збігу з ключовими словами
        mock_html = '''
        <html>
        <body>
            <a href="/job/125">Marketing Manager</a>
            <a href="/job/126">Sales Executive</a>
        </body>
        </html>
        '''
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_html

        result = fetch_jobs('https://example.com/careers', ['technical writer'])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()