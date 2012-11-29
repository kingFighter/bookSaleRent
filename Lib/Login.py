# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\PyProject\Login.ui'
#
# Created: Mon Nov 26 20:51:35 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 133, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton = QtGui.QRadioButton(Login)
        self.radioButton.setGeometry(QtCore.QRect(100, 170, 89, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Login)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 170, 89, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Login)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 170, 89, 16))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.layoutWidget = QtGui.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 80, 44, 32))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(101, 131, 30, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(151, 131, 133, 20))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Login", "登陆", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Login", "超级管理员", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Login", "管理员", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Login", "操作员", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Login", "用户名:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Login", "密码:", None, QtGui.QApplication.UnicodeUTF8))

