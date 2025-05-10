import unittest
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication


class TestData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Инициализация QApplication

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()  # Завершение приложения

    def setUp(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(":memory:")
        self.db.open()

        query = QSqlQuery()
        query.exec(
            "CREATE TABLE transactions (id INTEGER PRIMARY KEY, Description TEXT)"
        )

    def tearDown(self):
        self.db.close()
        QSqlDatabase.removeDatabase("QSQLITE")

    def test_add_new_transaction(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec()  # Заменено на exec()

        query.prepare("SELECT Description FROM transactions WHERE Description = 'Test'")
        query.exec()  # Заменено на exec()
        query.next()
        self.assertEqual(query.value(0), "Test")  # Получаем значение по индексу

    def test_delete_transaction(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec()  # Заменено на exec()

        query.prepare("DELETE FROM transactions WHERE Description = 'Test'")
        query.exec()  # Заменено на exec()

        query.prepare("SELECT Description FROM transactions WHERE Description = 'Test'")
        query.exec()  # Заменено на exec()
        self.assertFalse(query.next())  # Проверка, что запись удалена

    def test_total_methods(self):
        pass  # Здесь можно добавить тесты по вашему усмотрению

    def test_update_transaction(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO transactions (Description) VALUES ('Test')")
        query.exec()  # Заменено на exec()

        query.prepare(
            "UPDATE transactions SET Description = 'Updated' WHERE Description = 'Test'"
        )
        query.exec()  # Заменено на exec()

        query.prepare(
            "SELECT Description FROM transactions WHERE Description = 'Updated'"
        )
        query.exec()  # Заменено на exec()
        query.next()
        self.assertEqual(query.value(0), "Updated")  # Получаем значение по индексу


if __name__ == "__main__":
    unittest.main()
