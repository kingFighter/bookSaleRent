import sys
from PyQt4 import QtCore, QtGui
from untitled import Ui_Form

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"),self.file_dialog)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.file_save)
        QtCore.QObject.connect(self.ui.editor_window,QtCore.SIGNAL("textChanged()"), self.enable_save)
    def enable_save(self):
        self.ui.pushButton.setEnabled(True)
    def file_dialog(self):
         fd = QtGui.QFileDialog(self)
         self.filename = fd.getOpenFileName()
         from os.path import isfile
         if isfile(self.filename):
             text = open(self.filename).read()
             self.ui.editor_window.setText(text)
             self.ui.pushButton.setEnabled(False)
    def file_save(self):
           from os.path import isfile
           if isfile(self.filename):
               file = open(self.filename, 'w')
               file.write(self.ui.editor_window.toPlainText())
               file.close()
               self.ui.pushButton.setEnabled(False)




if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
