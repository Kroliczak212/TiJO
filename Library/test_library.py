
import unittest
from unittest.mock import Mock
from library import Library

class TestLibraryWithMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = Mock()
        self.library = Library(self.mock_repo)

    def test_borrow_existing_book(self):
        # Konfiguracja mocka
        self.mock_repo.remove_book.return_value = True

        result = self.library.borrow_book("Wiedźmin")

        self.assertTrue(result)
        self.mock_repo.remove_book.assert_called_once_with("Wiedźmin")

    def test_borrow_non_existing_book(self):
        self.mock_repo.remove_book.return_value = False

        result = self.library.borrow_book("Harry Potter")

        self.assertFalse(result)
        self.mock_repo.remove_book.assert_called_once_with("Harry Potter")

    def test_return_book(self):
        self.library.return_book("Lalka", "Bolesław Prus", 1890)

        self.mock_repo.add_book.assert_called_once_with(
            "Lalka", "Bolesław Prus", 1890
        )

    def test_list_books(self):
        test_data = [
            {"title": "Pan Tadeusz", "author": "Mickiewicz", "year": 1834},
            {"title": "Dziady", "author": "Mickiewicz", "year": 1823}
        ]
        self.mock_repo.get_all_books.return_value = test_data

        result = self.library.list_books()

        self.assertEqual(result, test_data)
        self.mock_repo.get_all_books.assert_called_once()

if __name__ == '__main__':
    unittest.main()
