import unittest
from csv_sql.csv_to_database import CsvToDatabase


class TestCsvToDatabase(unittest.TestCase):
    def setUp(self):
        self.exec = CsvToDatabase()

    def test_all_student_result(self):
        self.assertIsNotNone(self.exec.all_student_result())
        self.assertIsInstance(self.exec.all_student_result(), list)

    def test_add_student(self):
        before_adding_student = len(self.exec.all_student_result())
        add_student = self.exec.add_student('Agbaje', 'Afeez', '419-419-419', '100', '90', '80', '85', '85', 'A')
        after_adding_student = len(self.exec.all_student_result())
        self.assertNotEqual(before_adding_student, after_adding_student)
        self.assertIsNotNone(add_student)

    def test_update(self):
        update = self.exec.update('100', '90', '80', '85', '85', 'A', '419-419-419')
        self.assertIsNotNone(update)
        self.assertIsInstance(update, list)

    def test_passed(self):
        self.assertIsNotNone(self.exec.passed())
        self.assertIsInstance(self.exec.passed(), list)

    def test_passed_test1(self):
        self.assertIsNotNone(self.exec.passed_test1())
        self.assertIsInstance(self.exec.passed_test1(), list)

    def test_failed(self):
        self.assertIsNotNone(self.exec.failed())
        self.assertIsInstance(self.exec.failed(), list)

    def test_delete(self):
        delete_student = self.exec.delete('419-419-419')
        self.assertIsNotNone(delete_student)
        self.assertIsInstance(self.exec.delete(delete_student), list)

    def tearDown(self):
        self.exec.cursor.close()
        self.exec.connection.close()


if __name__ == '__main__':
    unittest.main()
