import unittest
from unittest.mock import patch, mock_open, MagicMock
import word2xwiki

class TestWordToXWikiConverter(unittest.TestCase):
    @patch('word2xwiki.requests.put')
    @patch('word2xwiki.subprocess.run')
    @patch('word2xwiki.glob.glob')
    @patch('word2xwiki.yaml.safe_load')
    def test_process_files(self, mock_safe_load, mock_glob, mock_run, mock_put):
        # Mock configuration
        mock_safe_load.return_value = {
            'directory': 'test_directory',
            'xwiki_url': 'http://test-xwiki-instance',
            'space': 'TestSpace',
            'username': 'test-username',
            'password': 'test-password'
        }
        # Mock files
        mock_glob.return_value = ['test_directory/test.docx']
        # Mock pandoc conversion
        mock_run.return_value = MagicMock(returncode=0, stdout='Converted content')
        # Mock XWiki API response
        mock_put.return_value = MagicMock(status_code=200, text='Success')

        converter = word2xwiki.WordToXWikiConverter('config.yaml')
        converter.process_files()

        mock_run.assert_called_once_with(['pandoc', 'test_directory/test.docx', '-t', 'xwiki'], capture_output=True, text=True)
        mock_put.assert_called_once()

if __name__ == '__main__':
    unittest.main()
