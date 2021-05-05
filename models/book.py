import psycopg2
from utils.connection import connection


class Book:
    def __init__(self):
        self.connection = connection()
        self.cursor = self.connection.cursor()

    def all(self, user_id):
        self.cursor.execute('SELECT * FROM books WHERE user_id=%s', str(user_id))
        return self.cursor.fetchall()

    def get_all_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()

    def get(self, id):
        self.cursor.execute('SELECT * FROM books WHERE id=%s', (id,))
        return self.cursor.fetchone()

    def create(self, user_id, name, pages):
        try:
            create_query = 'INSERT INTO books (user_id, name, pages) VALUES (%s, %s, %s)'
            self.cursor.execute(create_query, (user_id, name, pages))
            self.connection.commit()
            return self.all(user_id)
        except psycopg2.errors.UndefinedColumn:
            return 'User does not exist. Please assign the book to an existing User'

    def update(self, id, user_id, name, pages):
        update_query = "UPDATE books SET user_id = %s, name = %s, pages = %s, updated_at = now() WHERE id = %s"
        self.cursor.execute(update_query, (user_id, name, pages, id))
        self.connection.commit()
        return self.cursor.fetchone()

    def destroy(self, id):
        self.cursor.execute('DELETE FROM books WHERE id=%s', (id,))
        self.connection.commit()
        return self.cursor.fetchone()