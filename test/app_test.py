""" imports """
import unittest
from unittest.mock import patch, MagicMock
from src.models.taxi import Taxis
from src.app import get_taxis as real_get_taxis

mock_db_allTaxis = [
    { 'id': 12500, 'plate': 'ABC-test1' },
    { 'id': 12501, 'plate': 'ABC-test2' },
    { 'id': 12502, 'plate': 'ABC-test3' },
]

class TestGetTaxis(unittest.TestCase):
    """ Test for path '/taxis' """
    def test_get_all_taxis(self):
        """ test for get all taxis """
        mock_get_taxis = MagicMock(return_value = mock_db_allTaxis)
        with patch.object(Taxis, 'get_taxis', mock_get_taxis):
            result = real_get_taxis()
            self.assertEqual(result, mock_db_allTaxis)


if __name__ == '__main__':
    unittest.main()

# End-of-file
