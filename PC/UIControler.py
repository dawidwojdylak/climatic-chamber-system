import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtGui import QKeySequence
from PySide2.QtCore import QObject, Signal, Slot
from MainWindow import Ui_MainWindow
import ChamberControler 
from Communicator import Communicator
import pyqtgraph as pg
import numpy as np
import os
from ChartView import ChartView
from Chart import Chart

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chamberControler = ChamberControler.ChamberControler("./CTS_Interface_Protocol.xml")
        self.communicator = Communicator()
        
        self.chart = QtChart.QChart()
        self.chart = Chart()
        self.chartView = ChartView(self.chart)
        self.chartView.setChart(self.chart)
        

        self.ui.verticalLayout.addWidget(self.chartView)
        self.setUpPlot()

        # user input widget
        self.setVisibleUserInput(False)

        # connects:
        self.ui.listWidget_commandList.itemSelectionChanged.connect(self.onCommandListItemClicked)
        self.ui.listWidget_commandList.itemDoubleClicked.connect(self.onPushButton_sendCommandClicked)
        self.ui.pushButton_sendCommand.clicked.connect(self.onPushButton_sendCommandClicked)
        self.communicator.printErrSignal.connect(self.onCommunicatorErrMsgReceived)
        QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(QtWidgets.QApplication.instance().quit)

    def updateCommandList(self):
        commands = self.chamberControler.getCommands()
        self.ui.listWidget_commandList.clear()
        for c in commands:
            # try icons
            item = QtWidgets.QListWidgetItem(c.getName().replace("_", " "))
            item.setToolTip(c.getDescription())
            self.ui.listWidget_commandList.addItem(item)

    def setUpPlot(self):
        pass
        # embed and set up graph widget


    # @Slot(str)
    def printErrorToStatusBar(self, msg : str):
        self.ui.statusbar.showMessage(str, 2000)

    def setVisibleUserInput(self, val : bool):
        layout = self.ui.horizontalLayout_userInput1
        for j in range(layout.count()):
            item = layout.itemAt(j).widget()
            if item:
                item.setVisible(val)

            
        
    
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
        if type(response) != dict:
            return
        textWindow = self.ui.textBrowser_chamberResponse 
        textWindow.clear()
        for key, value in response.items():
            textWindow.setFontWeight(50)
            textWindow.insertPlainText(key + ": ")
            textWindow.setFontWeight(100)
            textWindow.insertPlainText(value + "\n")

    def onGraphMouseHoverUpdateStatusBar(self, evt):
        pos = evt
        if self.plot.sceneBoundingRect().contains(pos):
            mousePoint = self.plot.vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            # if index > 0:  #and index < len(data1):
            self.plotLabel.setText("<span style='font-size: 12pt'>t=%0.2f[s],\t<span style='color: red'>y=%0.2f</span>" % (mousePoint.x(), mousePoint.y()))
            self.plotvLine.setPos(mousePoint.x())
            self.plothLine.setPos(mousePoint.y())

    @Slot(str)
    def onCommunicatorErrMsgReceived(self, msg : str):
        print("slot str " + msg)
        self.ui.statusbar.showMessage(msg, 3000)

    def onMousePressed(self):
        print("mouse pressed")


def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    
    uiC.updateCommandList() # should not be called here # create method for such functions
    
    sys.exit(app.exec_())


