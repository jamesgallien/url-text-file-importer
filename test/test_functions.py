from os.path import join, dirname
import unittest
from unittest.mock import patch, MagicMock

from app.functions import populateDb, printDb, clearDb
from app.models import Link

TEST_FILE = join(dirname(__file__), 'test_files/text_file.txt')

class TestFunctions(unittest.TestCase):
    @patch('app.functions.db')
    def test_populateDb(self, mock_db: MagicMock):
        populateDb(TEST_FILE)
        mock_db.session.add.call_count = 14
        mock_db.session.commit.assert_called()

    @patch('app.functions.Link')
    @patch('app.functions.db')
    def test_clearDb(self, mock_db: MagicMock, mock_Link):
        test_link = Link(
                url = 'www.google.com',
                starred = False,
                read = False,
                dead_link=False,
                header=False,
                space=False,
            )
        mock_Link.query.all.return_value = [test_link]
        clearDb()
        mock_Link.query.all.assert_called()
        mock_db.session.delete.assert_called()

    @patch('app.functions.Link')
    def test_printDb(self, mock_Link: MagicMock):
        printDb()
        mock_Link.query.all.assert_called()

