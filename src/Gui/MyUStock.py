'''
Created on 2012-11-26

@author: Kevin Lui
'''
import sys
from PyQt4 import QtCore, QtGui
from stockBook import Ui_Dialog
from dbOperate.DbManager import DbManager

class MyUStock(QtGui.QMainWindow):
    DB=None
    def __init__(self, db,parent=None,row=[]):
        self.row=row
        MyUStock.DB=db
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
                    
        self.ui.lineEdit.setText(str(row[0]))
        self.ui.lineEdit_2.setText(str(row[2]))
        self.ui.lineEdit_3.setText(str(row[6]))
        self.ui.lineEdit_4.setText(str(row[8]))
        self.ui.lineEdit_5.setText(str(row[5]))
        self.ui.lineEdit_7.setText(str(row[7]))
        self.ui.lineEdit_6.setText(str(row[9]))
        self.ui.lineEdit_8.setText(str(row[5]))
        
        self.ui.comboBox.addItem("")
        self.ui.comboBox.setItemText( 0,str(row[1]))
        self.ui.comboBox_2.setItemText( 0,str(row[3]))
        
        
            
            
            
        
        
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.addBook)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.close)


    def addBook(self):
        MyUStock.DB.getBookManager().updateStock(self.ui.lineEdit.text(),self.ui.lineEdit_6.text())
        
        message = QtGui.QMessageBox(self)
        message.setText("update stock Successfully!")
        message.exec_()
        
               
        
    

if __name__=="__main__":
    DB= DbManager()
    app = QtGui.QApplication(sys.argv)
    myapp=MyUStock(DB,None,[1])
    myapp.show()
    sys.exit(app.exec_())
