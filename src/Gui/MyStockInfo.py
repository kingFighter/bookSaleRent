'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from StockInfo import Ui_Form
from dbOperate.DbManager import DbManager

class MyStockInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None):
        MyStockInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.showStock()
        
        self.ui.pushButton.close()
        
    def showStock(self):
        v = MyStockInfo.DB.getBookManager().showStock()
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
    myapp=MyStockInfo(DB)
    myapp.show()
    sys.exit(app.exec_())
