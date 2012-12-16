'''
Created on 2012-12-16

@author: Kevin Lui
'''

import sys
from PyQt4 import QtCore, QtGui
from Email import Ui_Dialog

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'lkymlf598@163.com'
smtpserver = 'smtp.163.com'
username = 'lkymlf598@163.com'
password = 'feilingma6'

class MyEmail(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
                    
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.sendEmail)


    def sendEmail(self):
        receiver = self.ui.lineEdit.text()
        subject = self.ui.lineEdit_2.text();
        content= self.ui.textEdit.toPlainText()
        msg = MIMEText(content,'plain','utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        
        message = QtGui.QMessageBox(self)
        message.setText("Send Email Successfully!")
        message.exec_()
        
        receiver = self.ui.lineEdit.setText("")
        subject = self.ui.lineEdit_2.setText("");
        content= self.ui.textEdit.setText("")
               
        
    

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=MyEmail()
    myapp.show()
    sys.exit(app.exec_())
