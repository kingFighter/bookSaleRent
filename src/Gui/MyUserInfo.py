'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from UserInfo import Ui_Form
from Gui.MyAAUser import MyAAUser
from dbOperate.DbManager import DbManager

class MyUserInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None):
        MyUserInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueUserSearch)
        QtCore.QObject.connect(self.ui.pushButton ,QtCore.SIGNAL("clicked()"),self.addUser)
        QtCore.QObject.connect(self.ui.pushButton_2 ,QtCore.SIGNAL("clicked()"),self.delUser)
        
        self.ui.pushButton_3.close()
                
    def getSelect(self):
        row = self.ui.tableWidget.currentRow()
        result=[]
        if row == -1:
            return []
        
        item=self.ui.tableWidget.item(row, 0)
        result.append(item.text())
        item=self.ui.tableWidget.item(row, 1)
        result.append(item.text())
        return result
    
    def delUser(self):
        v = self.getSelect()
        MyUserInfo.DB.getUserManager().delUser(v[0],v[1])
        message = QtGui.QMessageBox(self)
        if len(v)==0:
            message.setText("del A User Unsuccessfully!")
            message.exec_()
        else:
            message.setText("del A User Successfully!")
            message.exec_()
            
    def addUser(self):
        row=[]
        MyAAUser(MyUserInfo.DB,self,row).show()
        '''
        improve to show the added User right now
        '''
    
    def vagueUserSearch(self):
        key = self.ui.lineEdit.text()
        v = MyUserInfo.DB.getUserManager().vagueUserSearch(key)
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
    myapp=MyUserInfo(DB)
    myapp.show()
    sys.exit(app.exec_())
