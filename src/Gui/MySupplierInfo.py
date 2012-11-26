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

class MySupplierInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None):
        MySupplierInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueSupplierSearch)
        

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
