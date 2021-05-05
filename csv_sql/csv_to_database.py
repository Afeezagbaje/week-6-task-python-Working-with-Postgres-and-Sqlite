import sqlite3
import csv


class CsvToDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('gradedb.sqlite')
        self.cursor = self.connection.cursor()
        self.create_table()
        self.load_data()

    def create_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS grades')
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS grades(Last_name TEXT NOT NULL,
                            First_name TEXT NOT NULL, SSN TEXT PRIMARY KEY, Test1 INTEGER NOT NULL,
                            Test2 INTEGER NOT NULL, Test3 INTEGER NOT NULL, Test4 INTEGER NOT NULL,
                            Final INTEGER NOT NULL, Grade TEXT NOT NULL);""")
        self.connection.commit()

    def load_data(self):
        with open('grades.csv') as file:
            file_reader = csv.reader(file)
            csv_data = list(file_reader)
            data_body = csv_data[1:]
        for row in data_body:
            row_tuple = tuple(row)
            self.cursor.execute('INSERT INTO grades VALUES (?,?,?,?,?,?,?,?,?)', row_tuple)
        self.connection.commit()

    def fetch_all(self):
        students = self.cursor.fetchall()
        for student in students:
            print(f'Last Name: {student[0]}\nFirst Name: {student[1]}\nSSN: {student[2]}\n'
                  f'Test1: {student[3]}\nTest2: {student[4]}\nTest3: {student[5]}\n'
                  f'Test4: {student[6]}\nFinal: {student[7]}\nGrade: {student[8]}\n')


    def all_student_result(self):
        self.cursor.execute('SELECT * FROM grades')
        return self.fetch_all()

    def add_student(self, last_name, first_name, ssn, test1, test2, test3, test4, final, grade):
        try:
            insert_into_database = 'INSERT INTO grades VALUES (?,?,?,?,?,?,?,?,?)'
            insert_values = (last_name, first_name, ssn, test1, test2, test3, test4, final, grade)
            self.cursor.execute(insert_into_database, insert_values)
            self.connection.commit()
            return self.all_student_result()

        except NameError:
            return 'Information not valid. Please try again'

    def update(self, test1, test2, test3, test4, final, grade, ssn):
        update_query = 'UPDATE grades SET test1=?, test2=?, test3=?, test4=?, final=?, grade=? WHERE ssn=?'
        data = (test1, test2, test3, test4, final, grade, ssn)
        self.cursor.execute(update_query, data)
        self.connection.commit()
        return self.all_student_result()

    def passed(self):
        self.cursor.execute('SELECT * FROM grades WHERE final>="50"')
        return self.fetch_all()

    def passed_test1(self):
        self.cursor.execute('SELECT * FROM grades WHERE test1>="45"')
        return self.fetch_all()

    def failed(self):
        self.cursor.execute('SELECT * FROM grades WHERE final<"50"')
        return self.fetch_all()

    def delete(self, ssn):
        delete_query = 'DELETE FROM grades WHERE ssn=?'
        data = (ssn,)
        self.cursor.execute(delete_query, data)
        self.connection.commit()
        return self.all_student_result()
