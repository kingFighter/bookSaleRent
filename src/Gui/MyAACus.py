'''
Created on 2012-11-26

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from AACus import Ui_Dialog
from dbOperate.DbManager import DbManager

class MyAACus(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,row=[]):
        self.row=row
        MyAACus.DB=db
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)    
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addCus)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.close)
    def clearCusInfo(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_7.setText("")
        
    def getCusInfo(self):
        
        cusIden=self.ui.lineEdit.text()
        sex=self.ui.comboBox.currentIndex()
        cusName =self.ui.lineEdit_2.text()
        cusType=self.ui.comboBox_2.currentIndex()
        phone=self.ui.lineEdit_5.text()
        email=self.ui.lineEdit_7.text()
        return cusIden,cusIden,cusName,sex,phone,email,cusType

    
    def addCus(self):

        v=self.getCusInfo()
        print(v)
        judge=MyAACus.DB.getCusManager().addCus(v[0],v[1],v[2],v[3],v[4],v[5],v[6])
        self.clearCusInfo()
        message = QtGui.QMessageBox(self)
        if judge:
            message.setText("Add A Cus Successfully!")
            message.exec_()
            print('ok')
        else:
            message.setText("Add A Cus Unsuccessfully!")
            message.exec_()
            print('false')
#        
#        
    

if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyAACus(DB,None,[])
    myapp.show()
    sys.exit(app.exec_())
