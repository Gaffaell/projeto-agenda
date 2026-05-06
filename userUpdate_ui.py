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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 400)
        self.userList = QTableView(Dialog)
        self.userList.setObjectName(u"userList")
        self.userList.setGeometry(QRect(0, 0, 251, 211))
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 230, 231, 131))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.userRegistration = QLineEdit(self.formLayoutWidget)
        self.userRegistration.setObjectName(u"userRegistration")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.userRegistration)

        self.userName = QLineEdit(self.formLayoutWidget)
        self.userName.setObjectName(u"userName")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.userName)

        self.userId = QLineEdit(self.formLayoutWidget)
        self.userId.setObjectName(u"userId")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.userId)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.userEmail = QLineEdit(self.formLayoutWidget)
        self.userEmail.setObjectName(u"userEmail")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.userEmail)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.userUpdateButton = QPushButton(Dialog)
        self.userUpdateButton.setObjectName(u"userUpdateButton")
        self.userUpdateButton.setGeometry(QRect(160, 370, 81, 26))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 221, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID aluno", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Matr\u00edcula", None))
        self.userUpdateButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u00cdnsira o ID do aluno que deseja modificar", None))
    # retranslateUi

