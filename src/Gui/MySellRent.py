'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from dbHelp.StatusManager import StatusManager
import sellCusInfo
import sellBookInfo
from PyQt4 import QtCore, QtGui
from sellRent import Ui_Form
from Gui.MyAAUser import MyAAUser
from dbOperate.DbManager import DbManager
import time


class MySellBookInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,judge=True):
        self.p=parent
        MySellBookInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = sellBookInfo.Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueBookSearch)
        QtCore.QObject.connect(self.ui.pushButton ,QtCore.SIGNAL("clicked()"),self.addBook)
        
        
    def getSelect(self):
        row = self.ui.tableWidget.currentRow()
        result=[]
        if row == -1:
            return []
        for i in range(10):
            if i==1:
                continue
            item=self.ui.tableWidget.item(row, i)
            if i == 8:
                result.append('1')
                continue
            result.append(item.text())
        
        return result
    
    def addBook(self):
        v = self.getSelect()
        rowCount=self.p.ui.tableWidget.rowCount()+1 
        
        self.p.ui.tableWidget.setRowCount(rowCount)
        p = rowCount-1
        
        for j in range(9):
            item = QtGui.QTableWidgetItem()
            self.p.ui.tableWidget.setItem(p, j, item)
            item = self.p.ui.tableWidget.item(p, j)
            item.setText(str(v[j]))

    
    def vagueBookSearch(self):
        key = self.ui.lineEdit.text()
        v = MySellBookInfo.DB.getBookManager().vagueBookSearch(key)
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
        


class MySellCusInfo(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None): 
        self.p=parent    
        MySellCusInfo.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = sellCusInfo.Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.vagueCusSearch)
        QtCore.QObject.connect(self.ui.pushButton_3 ,QtCore.SIGNAL("clicked()"),self.getSelect)
        QtCore.QObject.connect(self.ui.pushButton_3 ,QtCore.SIGNAL("clicked()"),self.close)
        
        
    def getSelect(self):
        row = self.ui.tableWidget.currentRow()
        result=[]
        if row == -1:
            return
        
        item=self.ui.tableWidget.item(row, 0)
        self.p.ui.lineEdit_6.setText(item.text())
               
        '''
        improve to show the added book right now
        '''
    
    def vagueCusSearch(self):
        key = self.ui.lineEdit.text()
        v = MySellCusInfo.DB.getCusManager().vagueCusSearch(key)
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
        



class MySellRent(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None):
        self.MySellCusInfo=MySellCusInfo(db)
        
        MySellRent.DB=db
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(time.strftime('%Y%m%d%H%M%S ',time.localtime(time.time())))
        self.ui.lineEdit_2.setText(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.ui.lineEdit_7.setText(StatusManager.loginId)
        
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.openCusInfo)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.openBookInfo)
        QtCore.QObject.connect(self.ui.pushButton_5,QtCore.SIGNAL("clicked()"),self.lock)
        QtCore.QObject.connect(self.ui.pushButton_6,QtCore.SIGNAL("clicked()"),self.cal)
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.sell)
    
    def sell(self):
         index=self.ui.comboBox_2.currentIndex()
         row = self.ui.tableWidget.rowCount()
         print(index)
         if index==0:
             
             for i in range(row):
                 item = self.ui.tableWidget.item(i, 0)
                 bookId=item.text()
                 item = self.ui.tableWidget.item(i, 7)
                 bookSAmount = item.text()
                 item = self.ui.tableWidget.item(i, 8)
                 bookTAmount = item.text()
                 cusId=self.ui.lineEdit_6.text()
                 MySellRent.DB.getBookManager().sell(bookId,bookSAmount,bookTAmount,cusId)
         else:
             pass
                 
             
         message = QtGui.QMessageBox(self)
         message.setText("Sell Successfully!")
         message.exec_()
    
    def cal(self):
        sum=float(self.ui.lineEdit_3.text())
        receiveP=self.ui.lineEdit_4.text()
        self.ui.lineEdit_5.setText(str(float(receiveP)-sum))
    def lock(self):
        rowCount=self.ui.tableWidget.rowCount()
        sum=0
        for i in range(rowCount):
            retailP= self.ui.tableWidget.item(i, 5).text()
            rentP= self.ui.tableWidget.item(i, 6).text()
            amount= self.ui.tableWidget.item(i, 7).text()
            leftA= self.ui.tableWidget.item(i, 8).text()
            sum = sum+float(retailP)*float(amount)
        self.ui.lineEdit_3.setText(str(sum))
        
        
    def openBookInfo(self):
        MySellBookInfo(MySellRent.DB,self).show()
        
    def openCusInfo(self):
        MySellCusInfo(MySellRent.DB,self).show()
        
        
        
                
if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MySellRent(DB)
    myapp.show()
    sys.exit(app.exec_())
