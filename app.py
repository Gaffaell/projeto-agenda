#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataBaseConnection import Database
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from main_ui import Ui_MainWindow
from userRegister_ui import Ui_Dialog as Ui_RegisterDialog
from userList_ui import Ui_Dialog as Ui_ListDialog
from userUpdate_ui import Ui_Dialog as Ui_UpdateDialog
from userDelete_ui import Ui_Dialog as Ui_DeleteDialog

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterDialog()
        self.ui.setupUi(self)


class ListDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ListDialog()
        self.ui.setupUi(self)
        query = "SELECT * FROM agenda"
        db = Database()
        results = db.fetch_all(query)
        print(results)
        db.close()


class UpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UpdateDialog()
        self.ui.setupUi(self)
        # coloca uma forma de pegar os dados da aplicação
        query = "UPDATE agenda SET nome = 'Gaffaell Updated' WHERE id = 2"
        db = Database()
        results = db.execute_query(query)
        print(results)
        db.close()



class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteDialog()
        self.ui.setupUi(self)
        # coloca uma forma de pegar os dados da aplicação
        query = "DELETE FROM agenda WHERE id = 1"
        db = Database()
        results = db.execute_query(query)
        print(results)
        db.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.registerButton.clicked.connect(self.open_register_dialog)
        self.ui.listButton.clicked.connect(self.open_list_dialog)
        self.ui.updateButton.clicked.connect(self.open_update_dialog)
        self.ui.deleteButton.clicked.connect(self.open_delete_dialog)

    def open_register_dialog(self):
        dialog = RegisterDialog()
        dialog.exec()

    def open_list_dialog(self):
        dialog = ListDialog()
        dialog.exec()

    def open_update_dialog(self):
        dialog = UpdateDialog()
        dialog.exec()

    def open_delete_dialog(self):
        dialog = DeleteDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
