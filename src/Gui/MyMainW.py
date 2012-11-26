'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from Gui.MyBookInfo import MyBookInfo
from Gui.MySupplierInfo import MySupplierInfo 
from Gui.MyCusInfo import MyCusInfo
from MainWindow import Ui_MainWindow
from dbOperate.DbManager import DbManager
import time
class MyMainW(QtGui.QMainWindow):
    DB = None
    def __init__(self, db,parent=None):
        MyMainW.DB=db
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(time.strftime('%Y-%m-%d ',time.localtime(time.time())))
        str="Welcome! Happy Every Day!"
        self.ui.textEdit.setText(str)
        QtCore.QObject.connect(self.ui.action_2,QtCore.SIGNAL("triggered()"),self.openBookInfo)
        QtCore.QObject.connect(self.ui.action_3,QtCore.SIGNAL("triggered()"),self.openSupplierInfo)
        QtCore.QObject.connect(self.ui.action_4,QtCore.SIGNAL("triggered()"),self.openCusInfo)
    def openBookInfo(self):
        MyBookInfo(MyMainW.DB,self).show()
    def openSupplierInfo(self):
        MySupplierInfo(MyMainW.DB,self).show()
    def openCusInfo(self):
        MyCusInfo(MyMainW.DB,self).show()
    
if __name__=='__main__':
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyMainW(DB)
    myapp.show()
    sys.exit(app.exec_())

