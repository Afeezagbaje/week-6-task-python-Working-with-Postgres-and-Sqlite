import sqlite3
import csv


class CsvToDatabase:
    """
       This class add csv files into the database
       ......
       def create_table() create the columns in our database
       def load_data() read data from the csv file and add them into the database
       def all_student_result() returns all the students and their in the database
       def add_student() adds new student into the database
       def update() help update an already existing user
       def passed() returns all student that their total score is above 50
       def passed_test1() returns all student that scored above 45 in test1
       def failed() returns all students that score below 50 in their total score
       def delete() delete a student using their SSN

       """
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
        with open('csv_sql/grades.csv', 'r') as file:
            file_reader = csv.reader(file)
            csv_data = list(file_reader)
            data_body = csv_data[1:]
        for row in data_body:
            row_tuple = tuple(row)
            self.cursor.execute('INSERT INTO grades VALUES (?,?,?,?,?,?,?,?,?)', row_tuple)
        self.connection.commit()

    def all_student_result(self):
        self.cursor.execute('SELECT * FROM grades')
        return self.cursor.fetchall()

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
        return self.cursor.fetchall()

    def passed_test1(self):
        self.cursor.execute('SELECT * FROM grades WHERE test1>="45"')
        return self.cursor.fetchall()

    def failed(self):
        self.cursor.execute('SELECT * FROM grades WHERE final<"50"')
        return self.cursor.fetchall()

    def delete(self, SSN):
        delete_query = 'DELETE FROM grades WHERE SSN=?'
        self.cursor.execute(delete_query, (str(SSN),))
        self.connection.commit()
        return self.all_student_result()
