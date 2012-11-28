'''
Created on 2012-11-26

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from AAUser import Ui_Dialog
from dbOperate.DbManager import DbManager

class MyAAUser(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,row=[]):
        self.row=row
        MyAAUser.DB=db
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addUser)
        
    def clearUserInfo(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        
    def getUserInfo(self):
        userIden=self.ui.lineEdit.text()
        userType=self.ui.comboBox.currentText()
        userName =self.ui.lineEdit_2.text()
        userPwd=self.ui.lineEdit_3.text()
        return userType,userIden,userName,userPwd
    
    def addUser(self):
        v=self.getUserInfo()
        
        judge=MyAAUser.DB.getUserManager().addUser(v[0],v[1],v[2],v[3])
        self.clearUserInfo()
        message = QtGui.QMessageBox(self)
        if judge:
            message.setText("Add A User Successfully!")
            message.exec_()
            print('ok')
        else:
            message.setText("Add A User Unsuccessfully!")
            message.exec_()
            print('false')
        
        
    

if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyAAUser(DB,None,[])
    myapp.show()
    sys.exit(app.exec_())
