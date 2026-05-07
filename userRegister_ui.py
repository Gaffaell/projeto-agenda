# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userRegister.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from dataBaseConnection import Database
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QMessageBox, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 180)
        self.saveUserButton = QPushButton(Dialog)
        self.saveUserButton.clicked.connect(self.getInputData)
        self.saveUserButton.setObjectName(u"saveUserButton")
        self.saveUserButton.setGeometry(QRect(230, 140, 81, 26))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 301, 119))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.userEmail = QLineEdit(self.layoutWidget)
        self.userEmail.setObjectName(u"userEmail")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.userEmail)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.userRegistration = QLineEdit(self.layoutWidget)
        self.userRegistration.setObjectName(u"userRegistration")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.userRegistration)

        self.userName = QLineEdit(self.layoutWidget)
        self.userName.setObjectName(u"userName")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.userName)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.saveUserButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Matr\u00edcula", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nome", None))
    # retranslateUi
    
    def getInputData(self):
        name = self.userName.text()
        registration = self.userRegistration.text()
        email = self.userEmail.text()
        self.userEmail.clear()
        self.userRegistration.clear()
        self.userName.clear()
        msg = QMessageBox()
        msg.setText("Usuário cadastrado com sucesso!")
        msg.setInformativeText('Nome: ' + name + '\n' + 'Matrícula: ' + registration + '\n' + 'Email: ' + email)
        msg.setWindowTitle("Sucesso")
        msg.exec()
        self.sendDataToDatabase(name, email, registration)

    def sendDataToDatabase(self, name, email, registration):
        query = f"INSERT INTO agenda (nome, email, matricula) VALUES ('{name}', '{email}', '{registration}')"
        db = Database()
        results = db.execute_query(query)
        print(results)
        db.close()

