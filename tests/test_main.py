import unittest
from PySide6 import QtWidgets  # type: ignore
from unittest.mock import patch, MagicMock


class TestBudgetBuddy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    def setUp(self):

        self.data_mock = MagicMock()

        self.data_mock.total_balance.return_value = "1000$"
        self.data_mock.total_income.return_value = "1500$"
        self.data_mock.total_outcome.return_value = "500$"
        self.data_mock.total_groceries.return_value = "200$"
        self.data_mock.total_auto.return_value = "300$"
        self.data_mock.total_entertainment.return_value = "400$"
        self.data_mock.total_other.return_value = "100$"

        self.model_mock = MagicMock()
        self.data_mock.model = self.model_mock

        self.patcher = patch("main.Data", return_value=self.data_mock)
        self.patcher.start()

        from main import BudgetBuddy

        self.window = BudgetBuddy()

    def tearDown(self):
        self.window.close()
        self.patcher.stop()

    def test_initial_ui(self):
        self.assertIsNotNone(self.window.ui)
        self.assertIsNotNone(self.window.ui.tableView)
        self.assertEqual(self.window.ui.current_balance.text(), "1000$")

    def test_reload_data(self):
        self.window.reload_data()
        self.assertEqual(self.window.ui.current_balance.text(), "1000$")
        self.assertEqual(self.window.ui.income_balance.text(), "1500$")
        self.assertEqual(self.window.ui.outcome_balance.text(), "500$")


if __name__ == "__main__":
    unittest.main()