from models.book import Book
from models.user import User
from csv_sql.csv_to_database import CsvToDatabase


get_book = Book()
# print(get_book.get_all_books())
# print(get_book.all(1))
# print(get_book.get(2))

# print(get_book.update(26, 2, 'Fort', '200'))
# print(get_book.destroy(26))
# print(get_book.destroy(3))
# print(get_book.destroy(4))
# print(get_book.destroy(5))
# print(get_book.create(1, 'fxgcvhbjnkm,Fortran', 150))

get_user = User()
# print(get_user.all())
# print(get_user.get(9))
# print(get_user.create('bako', 'Olodo', 'Rabata'))
# print(get_user.update(20, 'badguy', 'badman', 'things'))
# print(get_user.destroy(3))
# print(get_user.destroy(8))
# print(get_user.destroy(7))

# csv_data = CsvToDatabase()
# print(csv_data.all_student_result())
# print(csv_data.add_student('badmus', 'lukman', '419-419-419', 30, 40, 50, 60, 45, 'D'))
# print(csv_data.update(50, 60, 70, 80, 65, 'B', '419-419-419'))
# print(csv_data.passed())
# print(csv_data.passed_test1())
# print(csv_data.failed())
# print(csv_data.delete('419-419-419'))
# if __name__ == '__main__':
