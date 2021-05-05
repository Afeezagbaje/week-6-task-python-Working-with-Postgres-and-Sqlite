from connection import connection


class LoadData:
    def __init__(self):
        self.con = connection()
        self.cursor = self.con.cursor()
        self.load_data()

    def load_data(self):
        self.cursor.execute('DROP TABLE if exists books CASCADE')
        self.cursor.execute('DROP TABLE if exists users CASCADE')
        with open('schema.sql', 'r') as schema_file:
            self.cursor.execute(schema_file.read())
            self.con.commit()

        with open('seeder.sql', 'r') as seeder_file:
            self.cursor.execute(seeder_file.read())
            self.con.commit()
