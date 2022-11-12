import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
import ChamberControler 
import os

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chamberControler = ChamberControler.ChamberControler("/home/dawidwojdylak/Projects/mip_pr-climatic_chamber_system/PC/CTS_Interface_Protocol.xml")
        # connects:

    def updateCommandList(self):
        commands = self.chamberControler.getCommandsNamesList()
        self.ui.listWidget_commandList.clear()
        for c in commands:
            self.ui.listWidget_commandList.addItem(c.replace("_", " "))

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    
    uiC.updateCommandList() # should not be called here
    
    sys.exit(app.exec_())


