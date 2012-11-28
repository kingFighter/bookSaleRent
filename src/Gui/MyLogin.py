'''
Created on 2012-11-25

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from Login import Ui_Login
from dbOperate.DbManager import DbManager
from Gui.MyMainW import MyMainW
from Gui.MyOMainW import MyOMainW
from Gui.MySMainW import MySMainW
from dbHelp.StatusManager import StatusManager

class MyLogin(QtGui.QMainWindow):
    DB=DbManager()
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.login)
    def getUserType(self):
        if self.ui.radioButton.isChecked():
            return 'superadmin'
        elif self.ui.radioButton_2.isChecked():
            return 'administrator'
        elif self.ui.radioButton_3.isChecked():
            return 'operator' 
    
    def login(self):
        name = self.ui.lineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        check = MyLogin.DB.getUserManager().checkUser(self.getUserType(), name, pwd)
        if not check:
            self.ui.lineEdit.setText('')
            self.ui.lineEdit_2.setText('')
        if check:
            StatusManager.setLoginId1(name)
            if self.getUserType()[0]=='a':
                MyMainW(MyLogin.DB,self).show()
            elif self.getUserType()[0]=='o':
                MyOMainW(MyLogin.DB,self).show()
            else:
                MySMainW(MyLogin.DB,self).show()
            self.hide()



if __name__=="__main__":
    
    app = QtGui.QApplication(sys.argv)
    myapp=MyLogin()
    myapp.show()
    sys.exit(app.exec_())
