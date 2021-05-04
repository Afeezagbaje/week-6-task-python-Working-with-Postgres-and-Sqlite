import unittest
from ..csv_to_database import CsvToDatabase


class TestCsvToDatabase(unittest.TestCase):
    def setUp(self):
        self.execute = CsvToDatabase()
        self.execute.create_table()
        self.execute.load_data()

    def test_all_student_result(self):
        self.assertIsNotNone(self.execute.all_student_result())
        self.assertIsInstance(self.execute.all_student_result(), list)

    def test_add_student(self):
        before_adding_student = len(self.execute.all_student_result())
        add_student = self.execute.add_student('Agbaje', 'Afeez', '419-419-419', '100', '90', '80', '85', '85', 'A')
        after_adding_student = len(self.execute.all_student_result())
        self.assertNotEqual(before_adding_student, after_adding_student)
        self.assertIsNotNone(add_student)

    def test_update(self):
        update = self.execute.update('100', '90', '80', '85', '85', 'A', '419-419-419')
        self.assertIsNotNone(update)
        self.assertIsInstance(update, list)

    def test_passed(self):
        self.assertIsNotNone(self.execute.passed())
        self.assertIsInstance(self.execute.passed(), list)

    def test_passed_test1(self):
        self.assertIsNotNone(self.execute.passed_test1())
        self.assertIsInstance(self.execute.passed_test1(), list)

    def test_failed(self):
        self.assertIsNotNone(self.execute.failed())
        self.assertIsInstance(self.execute.failed(), list)

    def delete(self):
        delete_student = self.execute.delete('419-419-419')
        self.assertIsNotNone(delete_student)
        self.assertIsInstance(self.execute.delete(delete_student), list)

    def tearDown(self):
        self.execute.cursor.close()
        self.execute.connection.close()


if __name__ == '__main__':
    unittest.main()
