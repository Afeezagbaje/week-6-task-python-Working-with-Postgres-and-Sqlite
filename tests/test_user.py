import unittest
from models.user import User


class TestBook(unittest.TestCase):
    def setUp(self):
        self.exec = User()

    def test_all(self):
        self.assertIsNotNone(self.exec.all())
        self.assertIsInstance(self.exec.all(), list)

    def test_get(self):
        self.assertIsNotNone(self.exec.get())
        self.assertIsInstance(self.exec.get(), list)

    def test_create(self):
        self.assertIsNotNone(self.exec.create())
        self.assertIsInstance(self.exec.create(), list)

    def test_update(self):
        self.assertIsNotNone(self.exec.update())
        self.assertIsInstance(self.exec.update(), list)

    def test_destroy(self):
        self.assertIsNotNone(self.exec.destroy())
        self.assertIsInstance(self.exec.destroy(), list)

    def tearDown(self):
        self.exec.cursor.close()
        self.exec.connection.close()


if __name__ == '__main__':
    unittest.main()
