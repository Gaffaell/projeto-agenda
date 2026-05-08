#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataBaseConnection import Database
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
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

        data = Database().loadData()
        
        # Create a model
        model = QStandardItemModel()
        
        # Set column headers (adjust based on your database columns)
        model.setHorizontalHeaderLabels(["Nome", "Email", "Matrícula", "ID"])
        
        # Populate table with data
        for row in data:
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)
        
        # Set the model to the table view
        self.ui.userList.setModel(model)


class UpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UpdateDialog()
        self.ui.setupUi(self)

        data = Database().loadData()
        
        # Create a model
        model = QStandardItemModel()
        
        # Set column headers (adjust based on your database columns)
        model.setHorizontalHeaderLabels(["Nome", "Email", "Matrícula", "ID"])
        
        # Populate table with data
        for row in data:
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)
        
        # Set the model to the table view
        self.ui.userList.setModel(model)



class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteDialog()
        self.ui.setupUi(self)
        
        data = Database().loadData()
        
        # Create a model
        model = QStandardItemModel()
        
        # Set column headers (adjust based on your database columns)
        model.setHorizontalHeaderLabels(["Nome", "Email", "Matrícula", "ID"])
        
        # Populate table with data
        for row in data:
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)
        
        # Set the model to the table view
        self.ui.userList.setModel(model)


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
