from utils.connection import connection


class User:
    """
    This class create an interface where we can interact with the users table in the database
    ......
    def all() Fetch all users available
    def get() Fetch one user by id
    def create() Create a user record
    def update() Update a user record
    def delete() Delete a user record

    """
    def __init__(self):
        self.connection = connection()
        self.cursor = self.connection.cursor()

    def all(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get(self, id):
        self.cursor.execute(f'SELECT * FROM users WHERE id={id}')
        return self.cursor.fetchone()

    def create(self, username, firstname, lastname):
        create_query = 'INSERT INTO users (username, first_name, last_name) VALUES (%s, %s, %s)'
        self.cursor.execute(create_query, (username, firstname, lastname))
        self.connection.commit()

    def update(self, id, username, firstname, lastname):
        update_query = "UPDATE users SET username = %s, first_name = %s, last_name = %s, updated_at = now() " \
                       "WHERE id = %s "
        self.cursor.execute(update_query, (username, firstname, lastname, str(id)))
        self.connection.commit()

    def destroy(self, id):
        self.cursor.execute('DELETE FROM users WHERE id=%s', (str(id),))
        self.connection.commit()
        return self.all()
