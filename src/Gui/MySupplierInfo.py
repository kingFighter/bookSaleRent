'''
Created on 2012-11-26

@author: Kevin Lui
'''
'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from SupplierInfo import Ui_Form
from dbOperate.DbManager import DbManager
from Gui.MyAASu import MyAASu

class MySupplierInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,judge=True):
        MySupplierInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueSupplierSearch)
        
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addSu)
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.delSu)
        
        self.ui.pushButton_2.close()
        if judge:
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
    
    def delSu(self):
        v = self.getSelect()
        MySupplierInfo.DB.getSupplierManager().delSupplier(v[0])     
        message = QtGui.QMessageBox(self)
        if len(v)==0:
            message.setText("del A Supplier Unsuccessfully!")
            message.exec_()
        else:
            message.setText("del A Supplier Successfully!")
            message.exec_()
    def addSu(self):
        row=[]
        MyAASu(MySupplierInfo.DB,self,row).show()
        '''
        improve to show the added book right now
        '''
    def vagueSupplierSearch(self):
        key = self.ui.lineEdit.text()
        v = MySupplierInfo.DB.getSupplierManager().vagueSupplierSearch(key)
        rowCount=len(v)
        self.ui.tableWidget.setRowCount(rowCount)
        p = 0
        for i in v:
            for j in range(4):
                item = QtGui.QTableWidgetItem()
                self.ui.tableWidget.setItem(p, j, item)
                item = self.ui.tableWidget.item(p, j)
                item.setText(str(i[j]))
            p +=1
        


if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MySupplierInfo(DB)
    myapp.show()
    sys.exit(app.exec_())
