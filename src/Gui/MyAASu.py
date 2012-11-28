'''
Created on 2012-11-26

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from AASu import Ui_Dialog
from dbOperate.DbManager import DbManager

class MyAASu(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,row=[]):
        self.row=row
        MyAASu.DB=db
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)    
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addSu)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.close)
    def clearSuInfo(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_3.setText("")
       
        
    def getSuInfo(self):
        
        suIden=self.ui.lineEdit.text()
        suName =self.ui.lineEdit_2.text()
        phone=self.ui.lineEdit_3.text()
        email=self.ui.lineEdit_4.text()
        return suIden,suName,phone,email

    
    def addSu(self):

        v=self.getSuInfo()
        print(v)
        judge=MyAASu.DB.getSupplierManager().addSupplier(v[0],v[1],v[2],v[3])
        self.clearSuInfo()
        message = QtGui.QMessageBox(self)
        if judge:
            message.setText("Add A Supplier Successfully!")
            message.exec_()
            print('ok')
        else:
            message.setText("Add A Supplier Unsuccessfully!")
            message.exec_()
            print('false')
#        
#        
    

if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyAASu(DB,None,[])
    myapp.show()
    sys.exit(app.exec_())
