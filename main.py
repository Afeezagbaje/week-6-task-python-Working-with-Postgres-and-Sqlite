from models.book import Book
from models.user import User
from csv_sql.csv_to_database import CsvToDatabase


get_book = Book()
get_user = User()
csv_data = CsvToDatabase()

if __name__ == '__main__':
    get_book.get_all_books()
    get_user.all()
    csv_data.all_student_result()
