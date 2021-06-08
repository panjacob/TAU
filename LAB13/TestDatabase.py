import unittest

from Database import Database


class TestDatabase(unittest.TestCase):
    def test_create(self):
        db = Database()
        data = [("Jakub", "Kwiatkowski", 1), ("Janusz", "Kowalski", 2), ("Grażyna", "Bąk", 3)]
        for firstname, lastname, id in data:
            result = db.add_student(firstname, lastname, id)
            # Kiedy wiersz został zmieniony arraysize == 1
            self.assertTrue(result.arraysize == 1)

    def test_read(self):
        db = Database()
        result = db.select("SELECT * FROM students")
        self.assertTrue(len(result) >= 2)

    def test_update(self):
        db = Database()
        db.execute(
            "UPDATE students SET firstname = 'TEST', lastname = 'TEST' WHERE firstname = 'Jakub' and lastname = 'Kwiatkowski'")
        result = db.select("SELECT * FROM students WHERE firstname = 'Jakub' and lastname = 'Kwiatkowski'")
        self.assertTrue(len(result) == 0)

    def test_delete(self):
        db = Database()
        result1 = db.select("SELECT * FROM students WHERE firstname = 'TEST' and lastname = 'TEST'")
        self.assertGreater(len(result1), 0)
        db.execute("DELETE FROM students WHERE firstname = 'TEST' and lastname = 'TEST'")
        result2 = db.select("SELECT * FROM students WHERE firstname = 'TEST' and lastname = 'TEST'")
        self.assertEqual(len(result2), 0)
