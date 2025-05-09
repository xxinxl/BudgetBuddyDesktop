import pytest
from PySide6.QtWidgets import QDialog
from new_transaction import Ui_Dialog


@pytest.fixture
def dialog(qtbot):
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    qtbot.addWidget(dialog)
    dialog.ui = ui
    return dialog


def test_dialog_initial_state(dialog):
    ui = dialog.ui
    assert ui.lbl_new_transaction.text() == "New transaction"
    assert ui.cb_choose_category.count() == 5
    assert ui.cb_status.count() == 2
    assert ui.le_description.placeholderText() == "Description"
    assert ui.le_balance.placeholderText() == "Balance"
    assert ui.cb_choose_category.placeholderText() == "Choose category"
    assert ui.cb_status.placeholderText() == "Choose status"
    assert ui.btn_new_transaction.text() == "Save new transaction"


def test_combobox_interaction(dialog, qtbot):
    ui = dialog.ui
    ui.cb_choose_category.setCurrentIndex(2)
    assert ui.cb_choose_category.currentText() == "Other"

    ui.cb_status.setCurrentIndex(1)
    assert ui.cb_status.currentText() == "Outcome"


def test_lineedit_input(dialog, qtbot):
    ui = dialog.ui
    ui.le_description.setText("Lunch with client")
    ui.le_balance.setText("45.60")
    assert ui.le_description.text() == "Lunch with client"
    assert ui.le_balance.text() == "45.60"


def test_date_edit(dialog):
    ui = dialog.ui
    date = ui.dateEdit.date()
    assert date.year() == 2025
    assert date.month() == 1
    assert date.day() == 1
