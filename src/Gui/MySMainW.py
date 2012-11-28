'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from Gui.MyBookInfo import MyBookInfo
from Gui.MySupplierInfo import MySupplierInfo 
from Gui.MyCusInfo import MyCusInfo
from Gui.MyUserInfo import MyUserInfo
from Gui.MyAABook import MyAABook
from Gui.MyStockInfo import MyStockInfo
from SMainWindow import Ui_MainWindow
from dbOperate.DbManager import DbManager
import time
import os
class MySMainW(QtGui.QMainWindow):
    DB = None
    def __init__(self, db,parent=None):
        MySMainW.DB=db
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(time.strftime('%Y-%m-%d ',time.localtime(time.time())))
        str="Welcome! Happy Every Day!"
        self.ui.textEdit.setText(str)
        QtCore.QObject.connect(self.ui.action_2,QtCore.SIGNAL("triggered()"),self.openBookInfo)
        QtCore.QObject.connect(self.ui.action_3,QtCore.SIGNAL("triggered()"),self.openSupplierInfo)
        QtCore.QObject.connect(self.ui.action_4,QtCore.SIGNAL("triggered()"),self.openCusInfo)
        QtCore.QObject.connect(self.ui.action_6,QtCore.SIGNAL("triggered()"),self.backup)
        QtCore.QObject.connect(self.ui.action_8,QtCore.SIGNAL("triggered()"),self.restore)
        
        QtCore.QObject.connect(self.ui.action_7,QtCore.SIGNAL("triggered()"),self.openAboutInfo)
        QtCore.QObject.connect(self.ui.action,QtCore.SIGNAL("triggered()"),self.openUserInfo)
    def backup(self):
#        path=os.popen('pwd').readlines()[0]
#        path=path.replace('/','\\')
        command=r'mysqldump  -u root --password=jdbc back > D:\Project\PyProject\backup.sql'
        os.system(command)
        message = QtGui.QMessageBox(self)
        message.setText("Backup successfully!")
        message.exec_()
        
    def restore(self):
        command=r'mysqldump  -u root --password=jdbc back < D:\Project\PyProject\backup.sql'
        os.system(command)
        message = QtGui.QMessageBox(self)
        message.setText("resotre successfully!")
        message.exec_()
    
    def openAboutInfo(self):
        message = QtGui.QMessageBox(self)
        message.setText("version:2.0\nCopyright (c) 2012 Lv Kaiyang")
        message.exec_()
    def openBookInfo(self):
        MyBookInfo(MySMainW.DB,self).show()
    def openSupplierInfo(self):
        MySupplierInfo(MySMainW.DB,self,False).show()
    def openCusInfo(self):
        MyCusInfo(MySMainW.DB,self).show()
    def openUserInfo(self):
        MyUserInfo(MySMainW.DB,self).show()
    
if __name__=='__main__':
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MySMainW(DB)
    myapp.show()
    sys.exit(app.exec_())

