import unittest
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QCoreApplication


class TestData(unittest.TestCase):
    def setUp(self):

        self.app = QCoreApplication([])
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(":memory:")
        self.db.open()

        query = QSqlQuery()
        query.exec_(
            "CREATE TABLE transactions (id INTEGER PRIMARY KEY, Description TEXT)"
        )

    def tearDown(self):

        self.db.close()
        QSqlDatabase.removeDatabase("QSQLITE")
        del self.app

    def test_add_new_transaction(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec_()

        query.prepare("SELECT Description FROM transactions WHERE Description = 'Test'")
        query.exec_()
        query.next()
        self.assertEqual(query.value("Description"), "Test")

    def test_delete_transaction(self):

        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec_()

        query.prepare("DELETE FROM transactions WHERE Description = 'Test'")
        query.exec_()

        query.prepare("SELECT Description FROM transactions WHERE Description = 'Test'")
        query.exec_()
        self.assertFalse(query.next())

    def test_total_methods(self):

        pass

    def test_update_transaction(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec_()

        query.prepare(
            "UPDATE transactions SET Description = 'Updated' WHERE Description = 'Test'"
        )
        query.exec_()

        query.prepare(
            "SELECT Description FROM transactions WHERE Description = 'Updated'"
        )
        query.exec_()
        query.next()
        self.assertEqual(query.value("Description"), "Updated")


if __name__ == "__main__":
    unittest.main()
