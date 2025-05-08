import unittest
from library_repository import InMemoryRepository

class TestInMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()

    def test_add_and_get_books(self):
        self.repo.add_book("Solaris", "Lem", 1961)
        books = self.repo.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Solaris")
        self.assertEqual(books[0]['author'], "Lem")

    def test_remove_existing_book(self):
        self.repo.add_book("Kordian", "Słowacki", 1834)
        result = self.repo.remove_book("Kordian")

        self.assertTrue(result)
        self.assertEqual(len(self.repo.get_all_books()), 0)

    def test_remove_non_existing_book(self):
        result = self.repo.remove_book("Nieistniejąca")

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
