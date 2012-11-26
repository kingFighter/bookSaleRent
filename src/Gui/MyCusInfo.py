'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from CusInfo import Ui_Form
from Gui.MyAACus import MyAACus
from dbOperate.DbManager import DbManager

class MyCusInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,judge=True):
        MyCusInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueCusSearch)
        QtCore.QObject.connect(self.ui.pushButton ,QtCore.SIGNAL("clicked()"),self.addCus)
        QtCore.QObject.connect(self.ui.pushButton_2 ,QtCore.SIGNAL("clicked()"),self.delCus)
        
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
    
    def delCus(self):
        v = self.getSelect()
        MyCusInfo.DB.getCusManager().delCus(v[0])
        message = QtGui.QMessageBox(self)
        if len(v)==0:
            message.setText("del A cus Unsuccessfully!")
            message.exec_()
        else:
            message.setText("del A cus Successfully!")
            message.exec_()
            
    def addCus(self):
        row=[]
        MyAACus(MyCusInfo.DB,self,row).show()
        '''
        improve to show the added book right now
        '''
    
    def vagueCusSearch(self):
        key = self.ui.lineEdit.text()
        v = MyCusInfo.DB.getCusManager().vagueCusSearch(key)
        rowCount=len(v)
        self.ui.tableWidget.setRowCount(rowCount)
        p = 0
        for i in v:
            for j in range(7):
                item = QtGui.QTableWidgetItem()
                self.ui.tableWidget.setItem(p, j, item)
                item = self.ui.tableWidget.item(p, j)
                item.setText(str(i[j]))
            p +=1
        


if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyCusInfo(DB)
    myapp.show()
    sys.exit(app.exec_())
