import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import QObject, Signal, Slot 
from MainWindow import Ui_MainWindow
import ChamberControler 
import Communicator
import os

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chamberControler = ChamberControler.ChamberControler("./CTS_Interface_Protocol.xml")
        
        
        # user input table
        self.ui.tableWidget_userValue.hide()
        self.ui.tableWidget_userValue.resize(self.ui.tableWidget_userValue.width(), 100)
        self.ui.tableWidget_userValue.setRowCount(1)
        self.ui.tableWidget_userValue.setColumnCount(2)
        self.ui.tableWidget_userValue.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # connects:
        self.ui.listWidget_commandList.itemClicked.connect(self.onCommandListItemClicked)
        self.ui.pushButton_sendCommand.clicked.connect(self.onPushButton_sendCommandClicked)
        Communicator.printErrSignal.connect(self.onCommunicatorErrMsgReceived)

    def updateCommandList(self):
        commands = self.chamberControler.getCommands()
        self.ui.listWidget_commandList.clear()
        for c in commands:
            # try icons
            item = QtWidgets.QListWidgetItem(c.getName().replace("_", " "))
            item.setToolTip(c.getDescription())
            self.ui.listWidget_commandList.addItem(item)

    # @Slot(str)
    def printErrorToStatusBar(self, msg : str):
        self.ui.statusbar.showMessage(str, 2000)
    
    def onCommandListItemClicked(self):
        selectedCommandIndex = self.ui.listWidget_commandList.currentRow() 
        self.selectedCommand = self.chamberControler.getCommands()[selectedCommandIndex]
        self.ui.statusbar.showMessage(self.selectedCommand.getDescription())
        if self.selectedCommand.isUserModifiable():
            self.ui.tableWidget_userValue.clear()
            for idx, arg in enumerate(self.selectedCommand.getUserModifiableArguments()):
                print(arg)
                descrStr = arg.descr
                if arg.unit:
                    descrStr += " [" + arg.unit + "]"
                argDescription = QtWidgets.QTableWidgetItem(descrStr)
                argDescription.setFlags(QtCore.Qt.ItemIsSelectable)
                self.ui.tableWidget_userValue.setItem(idx, 0, argDescription)
            self.ui.tableWidget_userValue.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Argument"))
            self.ui.tableWidget_userValue.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Value to set"))
            self.ui.tableWidget_userValue.show()
        else:
            self.ui.tableWidget_userValue.clear()
            self.ui.tableWidget_userValue.hide()

    def onPushButton_sendCommandClicked(self):
        # currentCommand = self.chamberControler.getCommands()[self.selectedCommandIndex]
        userValue = self.ui.tableWidget_userValue.item(0, 1).text()
        self.selectedCommand.setValue(userValue)
        self.chamberControler.sendCommandToChamber(self.selectedCommand)

    def onCommunicatorErrMsgReceived(self, msg : str):
        self.ui.statusbar.showMessage(msg, 3000)

    

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    
    uiC.updateCommandList() # should not be called here
    
    sys.exit(app.exec_())


