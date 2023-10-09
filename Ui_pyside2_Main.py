# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mycombobox import MyComboBox


class Ui_Form_Main(object):
    def setupUi(self, Form_Main):
        if not Form_Main.objectName():
            Form_Main.setObjectName(u"Form_Main")
        Form_Main.resize(400, 300)
        self.comboBox_ser_select = MyComboBox(Form_Main)
        self.comboBox_ser_select.setObjectName(u"comboBox_ser_select")
        self.comboBox_ser_select.setGeometry(QRect(20, 60, 141, 21))
        self.comboBox_ser_select.setMinimumSize(QSize(0, 0))
        self.comboBox_ser_select.setEditable(False)
        self.label_ser_info = QLabel(Form_Main)
        self.label_ser_info.setObjectName(u"label_ser_info")
        self.label_ser_info.setGeometry(QRect(30, 40, 318, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_ser_info.setFont(font)
        self.lineEdit_baud = QLineEdit(Form_Main)
        self.lineEdit_baud.setObjectName(u"lineEdit_baud")
        self.lineEdit_baud.setGeometry(QRect(80, 110, 71, 21))
        self.label_2 = QLabel(Form_Main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 61, 31))
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton_ser_open = QPushButton(Form_Main)
        self.pushButton_ser_open.setObjectName(u"pushButton_ser_open")
        self.pushButton_ser_open.setGeometry(QRect(240, 60, 75, 23))

        self.retranslateUi(Form_Main)

        QMetaObject.connectSlotsByName(Form_Main)
    # setupUi

    def retranslateUi(self, Form_Main):
        Form_Main.setWindowTitle(QCoreApplication.translate("Form_Main", u"\u4e32\u53e3\u4e0a\u4f4d\u673a", None))
        self.comboBox_ser_select.setCurrentText("")
        self.comboBox_ser_select.setPlaceholderText(QCoreApplication.translate("Form_Main", u"\u9009\u62e9\u7aef\u53e3", None))
        self.label_ser_info.setText(QCoreApplication.translate("Form_Main", u"\u4e32\u53e3\u4fe1\u606f", None))
        self.lineEdit_baud.setText(QCoreApplication.translate("Form_Main", u"115200", None))
        self.label_2.setText(QCoreApplication.translate("Form_Main", u"\u6ce2\u7279\u7387", None))
        self.pushButton_ser_open.setText(QCoreApplication.translate("Form_Main", u"\u6253\u5f00\u4e32\u53e3", None))
    # retranslateUi

