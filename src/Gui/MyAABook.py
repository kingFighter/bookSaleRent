'''
Created on 2012-11-26

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from AABook import Ui_Dialog
from dbOperate.DbManager import DbManager

class MyAABook(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,row=[]):
        self.row=row
        MyAABook.DB=db
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        v = MyAABook.DB.getSupplierManager().getAllSupplierInfo()
        for i in range(len(v)):
            self.ui.comboBox.addItem("")
            self.ui.comboBox.setItemText( 0,v[i])
        
        
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addBook)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.close)
    def clearBookInfo(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_7.setText("")
        
    def getBookInfo(self):
        bookIden=self.ui.lineEdit.text()
        supplierIden=self.ui.comboBox.currentText()
        
        bookName =self.ui.lineEdit_2.text()
        bookType=self.ui.comboBox_2.currentText()
        
        yearT=self.ui.dateEdit.date().getDate()
        year=yearT[0]
        author=self.ui.lineEdit_5.text()
        retailP=self.ui.lineEdit_3.text()
        rentP=self.ui.lineEdit_6.text()
        originalP=self.ui.lineEdit_4.text()
        amount=self.ui.lineEdit_7.text()
        
        return bookIden,supplierIden,bookName,bookType,year,author,retailP,rentP,originalP,amount
    def addBook(self):
        v=self.getBookInfo()
        judge=MyAABook.DB.getBookManager().addBook(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9])
        self.clearBookInfo()
        message = QtGui.QMessageBox(self)
        if judge:
            message.setText("Add A Book Successfully!")
            message.exec_()
            print('ok')
        else:
            message.setText("Add A Book Unsuccessfully!")
            message.exec_()
            print('false')
        
        
    

if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyAABook(DB,None,[])
    myapp.show()
    sys.exit(app.exec_())
