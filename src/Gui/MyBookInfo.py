'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from BookInfo import Ui_Form
from dbOperate.DbManager import DbManager

class MyBookInfo(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueBookSearch)
    
    
        


if __name__=="__main__":
    
    app = QtGui.QApplication(sys.argv)
    myapp=MyBookInfo()
    myapp.show()
    sys.exit(app.exec_())
