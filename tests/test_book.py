import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.exec = Book()
        self.id = 1

    def test_all(self):
        self.assertIsNotNone(self.exec.all(self.id))
        self.assertIsInstance(self.exec.all(self.id), list)

    def test_get_all_books(self):
        self.assertIsNotNone(self.exec.get_all_books())
        self.assertIsInstance(self.exec.get_all_books(), list)

    def test_get(self):
        self.assertIsNotNone(self.exec.get(self.id))
        self.assertIsInstance(self.exec.get(self.id), tuple)

    def test_create(self):
        user_books = len(self.exec.all(self.id))
        add_book_to_user = self.exec.create(self.id, 'Book of Life', 10000)
        self.assertIsNotNone(add_book_to_user)
        self.assertIsInstance(add_book_to_user, list)
        self.assertNotEqual(add_book_to_user, user_books)

    def test_destroy(self):
        self.assertIsNotNone(self.exec.destroy(4))
        self.assertIsInstance(self.exec.destroy(4), list)

    def tearDown(self):
        self.exec.cursor.close()
        self.exec.connection.close()


if __name__ == '__main__':
    unittest.main()
