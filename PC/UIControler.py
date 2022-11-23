import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, Signal, Slot 
from MainWindow import Ui_MainWindow
import ChamberControler 
from Communicator import Communicator
import os

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chamberControler = ChamberControler.ChamberControler("./CTS_Interface_Protocol.xml")
        self.communicator = Communicator()
        
        # user input widget
        self.setVisibleUserInput(False)

        # connects:
        self.ui.listWidget_commandList.itemClicked.connect(self.onCommandListItemClicked)
        self.ui.pushButton_sendCommand.clicked.connect(self.onPushButton_sendCommandClicked)
        self.communicator.printErrSignal.connect(self.onCommunicatorErrMsgReceived)

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

    def setVisibleUserInput(self, val : bool):
        for i in range(self.ui.verticalLayout_userInput.count()):
            layout = self.ui.verticalLayout_userInput.itemAt(i).layout()
            if layout:
                for j in range(layout.count()):
                    item = layout.itemAt(j).widget()
                    if item:
                        item.setVisible(val)
        if val:
            self.ui.splitter.setStretchFactor(0, 5)
            self.ui.splitter.setStretchFactor(1, 1)
        else:
            self.ui.splitter.setStretchFactor(0, 1)
            self.ui.splitter.setStretchFactor(1, 0)
            
        # TODO: fix sizes
        # print(self.ui.splitter.sizes())
        
    
    def onCommandListItemClicked(self):
        selectedCommandIndex = self.ui.listWidget_commandList.currentRow() 
        self.selectedCommand = self.chamberControler.getCommands()[selectedCommandIndex]
        self.ui.statusbar.showMessage(self.selectedCommand.getDescription())
        # TODO: append controls for more than one user arguments
        if self.selectedCommand.isUserModifiable():
            for idx, arg in enumerate(self.selectedCommand.getUserModifiableArguments()):
                descrStr = arg.descr
                if arg.unit:
                    descrStr += " [" + arg.unit + "]"
                self.ui.label_userInput1.setText(descrStr)
                self.ui.doubleSpinBox_userInput1.setMinimum(arg.min if arg.min != None else 0)
                self.ui.doubleSpinBox_userInput1.setMaximum(arg.max if arg.max != None else 100)


            self.setVisibleUserInput(True)
        #     self.ui.tableWidget_userValue.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Argument"))
        #     self.ui.tableWidget_userValue.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Value to set"))

        else:
            self.setVisibleUserInput(False)

    def onPushButton_sendCommandClicked(self):
        # currentCommand = self.chamberControler.getCommands()[self.selectedCommandIndex]
        # try to optimize this method
        userValue = ''
        try:
            if self.selectedCommand.isUserModifiable():
                userValue = self.ui.doubleSpinBox_userInput1.value()
                self.selectedCommand.setValue(userValue)
        except Exception as e:
            self.onCommunicatorErrMsgReceived(str(e))
            return 
        response = self.chamberControler.sendCommandToChamber(self.selectedCommand)
        self.ui.textBrowser_chamberResponse.clear()
        self.ui.textBrowser_chamberResponse.setText(response)

    @Slot(str)
    def onCommunicatorErrMsgReceived(self, msg : str):
        print("slot str " + msg)
        self.ui.statusbar.showMessage(msg, 3000)

    

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    
    uiC.updateCommandList() # should not be called here # create method for such functions
    
    sys.exit(app.exec_())


