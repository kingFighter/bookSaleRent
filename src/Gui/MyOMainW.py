'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from Gui.MyBookInfo import MyBookInfo
from Gui.MySupplierInfo import MySupplierInfo 
from Gui.MyCusInfo import MyCusInfo
from Gui.MyAABook import MyAABook
from Gui.MyStockInfo import MyStockInfo
from Gui.MySellRent import MySellRent
from OMainWindow import Ui_MainWindow
from dbOperate.DbManager import DbManager
import time
class MyOMainW(QtGui.QMainWindow):
    DB = None
    def __init__(self, db,parent=None):
        MyOMainW.DB=db
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(time.strftime('%Y-%m-%d ',time.localtime(time.time())))
        str="Welcome! Happy Every Day!"
        self.ui.textEdit.setText(str)
        
#        /self.pushButton.close()
        QtCore.QObject.connect(self.ui.action_2,QtCore.SIGNAL("triggered()"),self.openBookInfo)
        QtCore.QObject.connect(self.ui.action_4,QtCore.SIGNAL("triggered()"),self.openCusInfo)
        QtCore.QObject.connect(self.ui.action_7,QtCore.SIGNAL("triggered()"),self.openAboutInfo)
        QtCore.QObject.connect(self.ui.action_5,QtCore.SIGNAL("triggered()"),self.openSellRent)
    def openAboutInfo(self):
        message = QtGui.QMessageBox(self)
        message.setText("version:2.0\nCopyright (c) 2012 Lv Kaiyang")
        message.exec_()
    def openBookInfo(self):
        MyBookInfo(MyOMainW.DB,self,False).show()
    def openCusInfo(self):
        MyCusInfo(MyOMainW.DB,self,False).show()
    def openSellRent(self):
        MySellRent(MyOMainW.DB,self).show()
    
if __name__=='__main__':
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyOMainW(DB)
    myapp.show()
    sys.exit(app.exec_())

