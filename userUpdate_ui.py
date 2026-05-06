# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userUpdate.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QTableView,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 427)
        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 241, 171))
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 180, 229, 131))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_4)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID aluno", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Matr\u00edcula", None))
    # retranslateUi

