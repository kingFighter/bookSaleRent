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
    def __init__(self, db,parent=None,judge=True):
        MyBookInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueBookSearch)
        QtCore.QObject.connect(self.ui.pushButton ,QtCore.SIGNAL("clicked()"),self.addBook)
        QtCore.QObject.connect(self.ui.pushButton_2 ,QtCore.SIGNAL("clicked()"),self.delBook)
        
        self.ui.pushButton_3.close()
        if not judge:
            self.ui.pushButton.close()
            self.ui.pushButton_2.close()
            self.ui.pushButton_3.close()
        
        
    def getSelect(self):
        row = self.ui.tableWidget.currentRow()
        result=[]
        if row == -1:
            return []
        
        item=self.ui.tableWidget.item(row, 0)
        result.append(item.text())
        return result
    
    def delBook(self):
        v = self.getSelect()
        MyBookInfo.DB.getBookManager().delBook(v[0])
        message = QtGui.QMessageBox(self)
        if len(v)==0:
            message.setText("del A Book Unsuccessfully!")
            message.exec_()
        else:
            message.setText("del A Book Successfully!")
            message.exec_()
            
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
