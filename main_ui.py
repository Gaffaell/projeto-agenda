# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 300))
        MainWindow.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 281, 241))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.registerButton = QPushButton(self.gridLayoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.registerButton, 0, 0, 1, 1)

        self.listButton = QPushButton(self.gridLayoutWidget)
        self.listButton.setObjectName(u"listButton")

        self.gridLayout_3.addWidget(self.listButton, 3, 0, 1, 1)

        self.updateButton = QPushButton(self.gridLayoutWidget)
        self.updateButton.setObjectName(u"updateButton")

        self.gridLayout_3.addWidget(self.updateButton, 1, 0, 1, 1)

        self.deleteButton = QPushButton(self.gridLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout_3.addWidget(self.deleteButton, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 33))
        self.menu_Registrador_de_alunos = QMenu(self.menubar)
        self.menu_Registrador_de_alunos.setObjectName(u"menu_Registrador_de_alunos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Registrador_de_alunos.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar aluno", None))
        self.listButton.setText(QCoreApplication.translate("MainWindow", u"Lista de alunos", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Atualizar aluno", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Excluir aluno", None))
        self.menu_Registrador_de_alunos.setTitle(QCoreApplication.translate("MainWindow", u" Registrador de alunos", None))
    # retranslateUi
    def openDialog(self, dialog):
        dialog.exec_()

