'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from Gui.MyBookInfo import MyBookInfo
from MainWindow import Ui_MainWindow
from dbOperate.DbManager import DbManager
import time
class MyMainW(QtGui.QMainWindow):
   
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(time.strftime('%Y-%m-%d ',time.localtime(time.time())))
        str="Welcome! Happy Every Day!"
        self.ui.textEdit.setText(str)
        QtCore.QObject.connect(self.ui.action_2,QtCore.SIGNAL("triggered()"),self.openBookInfo)
    
    def openBookInfo(self):
        MyBookInfo(self).show()
        
        
    
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp=MyMainW()
    myapp.show()
    sys.exit(app.exec_())

