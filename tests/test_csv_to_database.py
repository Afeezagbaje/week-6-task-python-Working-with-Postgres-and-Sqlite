import unittest
from ..csv_to_database import CsvToDatabase


class TestCsvToDatabase(unittest.TestCase):
    def setUp(self):
        self.execute = CsvToDatabase()
        self.execute.load_data()
        
    def test_all_student_result(self):
        self.assertIsNotNone(self.execute.all_student_result())
        self.assertIsInstance(self.execute.all_student_result(), list)
        
    def test_add_student(self):
        self.assertIsNotNone(self.execute.add_student())
        self.assertIsInstance(self.execute.add_student, list)
    
    def test_update(self):
        self.assertIsNotNone(self.execute.update())
        self.assertIsInstance(self.execute.update(), list)
    
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
        self.assertIsNotNone(self.execute.delete())
        self.assertIsInstance(self.execute.delete(), list)
        
    def tearDown(self):
        self.execute.cursor.close()
        self.execute.connection.close()

        
if __name__ == '__main__':
    unittest.main()