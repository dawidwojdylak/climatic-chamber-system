import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
import os

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connects:

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    sys.exit(app.exec_())

