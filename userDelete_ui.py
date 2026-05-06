# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userDelete.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 323)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 250, 221, 34))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.userId = QLineEdit(self.formLayoutWidget)
        self.userId.setObjectName(u"userId")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.userId)

        self.deleteUsertButton = QPushButton(Dialog)
        self.deleteUsertButton.setObjectName(u"deleteUsertButton")
        self.deleteUsertButton.setGeometry(QRect(150, 290, 81, 26))
        self.userList = QTableView(Dialog)
        self.userList.setObjectName(u"userList")
        self.userList.setGeometry(QRect(0, 0, 241, 241))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID aluno", None))
        self.deleteUsertButton.setText(QCoreApplication.translate("Dialog", u"Excluir aluno", None))
    # retranslateUi

