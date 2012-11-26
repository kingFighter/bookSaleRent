'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from BookInfo import Ui_Form
from Gui.MyAABook import MyAABook
from dbOperate.DbManager import DbManager

class MyBookInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None):
        MyBookInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueBookSearch)
        QtCore.QObject.connect(self.ui.pushButton ,QtCore.SIGNAL("clicked()"),self.addBook)
    def addBook(self):
        row=[]
        MyAABook(MyBookInfo.DB,self,row).show()
        '''
        improve to show the added book right now
        '''
    
    def vagueBookSearch(self):
        key = self.ui.lineEdit.text()
        v = MyBookInfo.DB.getBookManager().vagueBookSearch(key)
        rowCount=len(v)
        self.ui.tableWidget.setRowCount(rowCount)
        p = 0
        for i in v:
            for j in range(10):
                item = QtGui.QTableWidgetItem()
                self.ui.tableWidget.setItem(p, j, item)
                item = self.ui.tableWidget.item(p, j)
                item.setText(str(i[j]))
            p +=1
        


if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyBookInfo(DB)
    myapp.show()
    sys.exit(app.exec_())
