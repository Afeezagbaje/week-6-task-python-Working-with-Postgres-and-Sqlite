import unittest
from models.user import User


class TestBook(unittest.TestCase):
    def setUp(self):
        self.exec = User()
        self.id = 1

    def test_all(self):
        self.assertIsNotNone(self.exec.all())
        self.assertIsInstance(self.exec.all(), list)

    def test_get(self):
        self.assertIsNotNone(self.exec.get(self.id))
        self.assertIsInstance(self.exec.get(self.id), list)

    def test_create(self):
        before_new_user = len(self.exec.all())
        self.exec.create('fenti', 'Rihanna', 'Fenti')
        after_new_user = len(self.exec.all())
        self.assertNotEqual(before_new_user,after_new_user)

    def test_update(self):
        before_update = len(self.exec.all())
        self.exec.create(4, 'scrim', 'Skunk', 'Skuki')
        after_update = len(self.exec.all())
        self.assertEqual(before_update, after_update)

    def test_destroy(self):
        before_destroy = len(self.exec.all())
        self.exec.destroy(4)
        after_destroy = len(self.exec.all())
        self.assertNotEqual(before_destroy, after_destroy)

    def tearDown(self):
        self.exec.cursor.close()
        self.exec.connection.close()


if __name__ == '__main__':
    unittest.main()
