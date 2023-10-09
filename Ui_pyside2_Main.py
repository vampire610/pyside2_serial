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
        Form_Main.resize(495, 347)
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
        self.label = QLabel(Form_Main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 230, 101, 21))
        self.lineEdit_data1 = QLineEdit(Form_Main)
        self.lineEdit_data1.setObjectName(u"lineEdit_data1")
        self.lineEdit_data1.setGeometry(QRect(10, 250, 81, 20))
        self.label_3 = QLabel(Form_Main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 230, 101, 21))
        self.lineEdit_data3 = QLineEdit(Form_Main)
        self.lineEdit_data3.setObjectName(u"lineEdit_data3")
        self.lineEdit_data3.setGeometry(QRect(230, 250, 113, 20))
        self.label_4 = QLabel(Form_Main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 230, 101, 21))
        self.lineEdit_data2 = QLineEdit(Form_Main)
        self.lineEdit_data2.setObjectName(u"lineEdit_data2")
        self.lineEdit_data2.setGeometry(QRect(120, 250, 71, 20))
        self.label_5 = QLabel(Form_Main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 230, 101, 21))
        self.lineEdit_data4 = QLineEdit(Form_Main)
        self.lineEdit_data4.setObjectName(u"lineEdit_data4")
        self.lineEdit_data4.setGeometry(QRect(360, 250, 113, 20))
        self.lineEdit_full = QLineEdit(Form_Main)
        self.lineEdit_full.setObjectName(u"lineEdit_full")
        self.lineEdit_full.setGeometry(QRect(50, 290, 351, 20))
        self.textBrowser = QTextBrowser(Form_Main)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QRect(30, 140, 421, 81))

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
        self.label.setText(QCoreApplication.translate("Form_Main", u"\u7b2c\u4e00\u4e2a\u6570\u636e", None))
        self.label_3.setText(QCoreApplication.translate("Form_Main", u"\u7b2c\u4e09\u4e2a\u6570\u636e", None))
        self.label_4.setText(QCoreApplication.translate("Form_Main", u"\u7b2c\u4e8c\u4e2a\u6570\u636e", None))
        self.label_5.setText(QCoreApplication.translate("Form_Main", u"\u7b2c\u56db\u4e2a\u6570\u636e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6d4b\u8bd5\u89e3\u6790\u6570\u636e\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ASCII(\u9017\u53f7\u5206\u9694\uff0c\\r\\n\u7ed3\u5c3e)\uff1a 1\uff0c2\uff0c3\uff0c4/r/n</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HEX\uff1a   AB CD 00 00 31 24 24 31 ff ff DF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ABCD\u4e3a"
                        "\u5934\uff0c\u540e\u9762\u6bcf\u4e24\u5b57\u8282\u4e3a\u4e00\u4e2a\u6570\u636e\uff0c\u524d\u4e24\u4e2a\u6570\u636e\u4e3a\u5927\u7aef\uff0c\u540e\u4e24\u4e2a\u4e3a\u5c0f\u7aef</p></body></html>", None))
    # retranslateUi

