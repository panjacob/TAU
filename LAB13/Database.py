import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()

    def select(self, query):
        result = []
        for row in self.cursor.execute(query):
            result.append(row)
        return result


    def execute(self, query):
        result = self.cursor.execute(query)
        self.con.commit()
        return result

    def add_student(self, firstname, lastname, id):
        return self.execute(f"INSERT INTO students (firstname, lastname) VALUES ('{firstname}', '{lastname}');")

