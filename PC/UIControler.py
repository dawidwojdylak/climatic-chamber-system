import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtGui import QKeySequence
from PySide2.QtCore import QObject, Signal, Slot
from MainWindow import Ui_MainWindow
from Login import Ui_Login
import ChamberControler 
from ChartView import ChartView
from Chart import Chart
import time
import csv

# pyuic5 -x  -o

class UIControler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loginPopUp = Ui_Login()
        self.chamberControler = ChamberControler.ChamberControler()
        try:
            self.chamberControler.importXmlFile("./CtsInterfaceProtocol.xml")
            self.setWindowTitle(self.chamberControler.xmlParser.getChamberName())
        except Exception as e:
            self.logError(str(e))


        self.chartSplitter = QtWidgets.QSplitter(self.ui.ChartTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.chartSplitter.sizePolicy().hasHeightForWidth())
        self.chartSplitter.setSizePolicy(sizePolicy)
        self.chartSplitter.setOrientation(QtCore.Qt.Vertical)
        self.chartSplitter.setObjectName("chartSplitter")
        
        self.chart = QtChart.QChart()
        self.chart = Chart(self)
        self.chartView = ChartView(self.chart, self)
        self.chartView.setChart(self.chart)
        self.ui.verticalLayout.addWidget(self.chartSplitter)
        self.chartSplitter.addWidget(self.chartView)

        self.pointsTable = QtWidgets.QTableWidget(self.ui.ChartTab)
        self.pointsTable.setColumnCount(1)
        self.pointsTable.setRowCount(3)
        self.pointsTable.setVerticalHeaderLabels(['time', 'temperature', 'humidity'])
        self.chartSplitter.addWidget(self.pointsTable)
        self.pointsTable.setVisible(False)


        # user input widget
        self.setVisibleUserInput(False)
        self.ui.pushButton_logClear.setVisible(False)
        self.ui.radioButton_chartHumidity.setChecked(True)

        # connects:
        self.ui.listWidget_commandList.itemSelectionChanged.connect(self.onCommandListItemClicked)
        self.ui.listWidget_commandList.itemDoubleClicked.connect(self.onPushButton_sendCommandClicked)
        self.ui.pushButton_sendCommand.clicked.connect(self.onPushButton_sendCommandClicked)
        QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(QtWidgets.QApplication.instance().quit)
        self.ui.radioButton_chartHumidity.toggled.connect(self.chart.humidityOptionChecked)
        self.ui.tabWidget.currentChanged.connect(self.setVisibleChartControls)
        self.ui.pushButton_login.clicked.connect(self.loginPopUp.exec)
        self.loginPopUp.accepted.connect(self.onPushButtonClicked_login)
        self.ui.pushButton_chartClear.clicked.connect(self.chart.clearChart)
        self.ui.checkBox_chartScatter.clicked.connect(self.chart.scatterEnabled)
        self.ui.pushButton_chartDeleteLast.clicked.connect(self.chart.deleteLastPoint)
        self.ui.pushButton_chartSend.clicked.connect(self.onChartSendButtonClicked)
        self.ui.pushButton_logClear.clicked.connect(self.ui.textBrowser_chamberResponse.clear)
        self.ui.action_checkConnection.triggered.connect(self.onCheckConnectionToggled)
        self.ui.actionConnect_to_server.triggered.connect(self.loginPopUp.exec)
        self.ui.actionClose_connection.triggered.connect(self.onCloseConnectionToggled)
        self.ui.pushButton_logout.clicked.connect(self.onCloseConnectionToggled)
        self.ui.actionImport_xml_config_file.triggered.connect(self.onImportXmlToggled)
        self.ui.actionExit.triggered.connect(QtWidgets.QApplication.instance().quit)
        self.ui.actionSave_script.triggered.connect(self.onSaveScript)
        self.ui.actionOpen_script.triggered.connect(self.onOpenScript)



    def updateCommandList(self):
        try:
            commands = self.chamberControler.getCommands()
        except Exception as e:
            self.logError(str(e))
            return
        self.ui.listWidget_commandList.clear()
        for c in commands:
            item = QtWidgets.QListWidgetItem(c.getName().replace("_", " "))
            item.setToolTip(c.getDescription())
            self.ui.listWidget_commandList.addItem(item)


    def printErrorToStatusBar(self, msg : str):
        self.ui.statusbar.showMessage(msg, 4000)

    def setVisibleUserInput(self, val : bool):
        layout = self.ui.horizontalLayout_userInput1
        for j in range(layout.count()):
            item = layout.itemAt(j).widget()
            if item:
                item.setVisible(val)

    def setVisibleChartControls(self, val):
        val = True if val == 0 else 0 # 0 is index of chart tab
        self.ui.label_chart.setVisible(val)
        self.ui.radioButton_chartHumidity.setVisible(val)
        self.ui.radioButton_chartTemperature.setVisible(val)
        self.ui.pushButton_chartClear.setVisible(val)
        self.ui.label_chartMousePos.setVisible(val)
        self.ui.checkBox_chartScatter.setVisible(val)
        self.ui.pushButton_chartDeleteLast.setVisible(val)
        self.ui.label_chartDeltaT.setVisible(val)
        self.ui.pushButton_chartSend.setVisible(val)
        self.ui.pushButton_logClear.setVisible(not val)
        

    def logError(self, errorMsg : str, timeout=4000):
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        textWindow = self.ui.textBrowser_chamberResponse 
        textWindow.setTextColor(QtGui.QColor('#b00202'))
        textWindow.append("[" + now + "] " + errorMsg)
        textWindow.setTextColor(QtGui.QColor('#000000'))
        self.ui.statusbar.showMessage(errorMsg, timeout)

    def logMsg(self, msg : str, timeout=4000):
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        textWindow = self.ui.textBrowser_chamberResponse
        textWindow.setTextColor(QtGui.QColor('#000000'))
        textWindow.append("[" + now + "] " + msg)
        self.ui.statusbar.showMessage(msg, timeout)


    @Slot()
    def onCommandListItemClicked(self):
        selectedCommandIndex = self.ui.listWidget_commandList.currentRow() 
        self.selectedCommand = self.chamberControler.getCommands()[selectedCommandIndex]
        self.ui.statusbar.showMessage(self.selectedCommand.getDescription())
        if self.selectedCommand.isUserModifiable():
            for idx, arg in enumerate(self.selectedCommand.getUserModifiableArguments()):
                descrStr = arg.descr
                if arg.unit:
                    descrStr += " [" + arg.unit + "]"
                self.ui.label_userInput1.setText(descrStr)
                self.ui.doubleSpinBox_userInput1.setMinimum(arg.min if arg.min != None else 0)
                self.ui.doubleSpinBox_userInput1.setMaximum(arg.max if arg.max != None else 100)
            self.setVisibleUserInput(True)
        else:
            self.setVisibleUserInput(False)

    @Slot()
    def onPushButton_sendCommandClicked(self):
        textWindow = self.ui.textBrowser_chamberResponse 
        try:
            connection = self.chamberControler.sshSender.checkConnection()
        except Exception as e:
            self.logError("User is not logged in. Cannot send request.")
            return
        if  connection == False:
            self.logError("User is not logged in. Cannot send request.")
            return
        userValue = ''
        try:
            if self.selectedCommand.isUserModifiable():
                userValue = self.ui.doubleSpinBox_userInput1.value()
                self.selectedCommand.setValue(userValue)
            response = self.chamberControler.sendCommandToChamber(self.selectedCommand)
        except Exception as e:
            self.logError(str(e))
            return
        if type(response) != dict:
            return
        for key, value in response.items():
            textWindow.setFontWeight(50)
            textWindow.insertPlainText(key + ": ")
            textWindow.setFontWeight(100)
            textWindow.insertPlainText(value + "\n")
        
    @Slot()    
    def onPushButtonClicked_login(self):
        try:
            self.chamberControler.sshSender.logIn(self.loginPopUp.pwd, self.loginPopUp.login)
        except Exception as e:
            self.logError("Cannot login: " + str(e))
            return
        self.logMsg("Logging in...")
        if self.chamberControler.sshSender.checkConnection():
            self.logMsg("Logged in succesfully", 4000)
        else:
            self.logError("Login failed")

    @Slot()
    def onCheckConnectionToggled(self):
        try:
            if self.chamberControler.sshSender.checkConnection():
                self.logMsg("Connected")
            else:
                self.logError("Connection failed", 3000)
        except Exception as e:
            self.logError("Connection failed")

    @Slot()
    def onCloseConnectionToggled(self):
        self.ui.statusbar.showMessage("Connection closed")
        self.chamberControler.sshSender.logOut()

    @Slot()
    def onMouseOnChartHover(self, x : float, y : float):
        text = 'x: %2.1f, y: %2.1f' % (x, y)
        self.ui.label_chartMousePos.setText(text)

    @Slot()
    def onPointAdded(self, d : float):
        if d < 0:
            self.ui.label_chartDeltaT.setText('')
            return
        text = 'delta t: %.1f [min]' % (d)
        self.ui.label_chartDeltaT.setText(text)

    @Slot()
    def onChartSendButtonClicked(self):
        import re
        try:
            tempScript, humidScript = self.chart.getScripts()
            def parse(scr):
                scr = scr.splitlines()
                result = ''
                for comm in scr:
                    current = re.split('\\(|\\)', comm)
                    if current[0] == 'sleep':
                        result += comm + '\n'
                    else:
                        self.selectedCommand = self.chamberControler.getCommand(current[0])
                        self.selectedCommand.setValue(current[1])
                        result += 'send(\"' + self.selectedCommand.prepareRequest() + '\")'+ '\n'
                return result
            tempScriptParsed = parse(tempScript)
            humidScriptParsed = parse(humidScript)

            self.chamberControler.sshSender.execScript(tempScriptParsed)
            self.chamberControler.sshSender.execScript(humidScriptParsed)
        except Exception as e:
            self.logError(str(e))

    @Slot()
    def onImportXmlToggled(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'XML config file', 'c:\\',"xml file (*.xml)")
        try:
            self.chamberControler.importXmlFile(fname[0])
            self.setWindowTitle(self.chamberControler.xmlParser.getChamberName())
        except Exception as e:
            self.logError(str(e))
        self.updateCommandList()

    @Slot()
    def onSaveScript(self):
        path, filter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
        if not path.endswith(".csv"): path += ".csv"
        with open(path, 'w') as f:
            try:
                writer = csv.writer(f)
                writer.writerow(['tempVal', 'tempTime'])
                for i in self.chart.tempPoints:
                    writer.writerow([i.x(), i.y()])
                writer.writerow(['humidVal', 'humidTime'])
                for i in self.chart.humidPoints:
                    writer.writerow([i.x(), i.y()])
            except Exception as e:
                self.logError(str(e))

    @Slot()
    def onOpenScript(self):
        try:
            path, filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open csv file', filter='*.csv')
            with open(path, 'r') as f:
                reader = csv.reader(f)
                humidPoints = []
                tempPoints = []
                isHumid = False
                for i in reader:
                    if i[0] == 'tempVal' and i[1] == 'tempTime':
                        isHumid = False
                        continue
                    elif i[0] == 'humidVal' and i[1] == 'humidTime':
                        isHumid = True
                        continue
                    if isHumid:
                        humidPoints.append(QtCore.QPointF(float(i[0]), float(i[1])))
                    else:
                        tempPoints.append(QtCore.QPointF(float(i[0]), float(i[1])))
                self.chart.importScript(tempPoints=tempPoints, humidPoints=humidPoints)
        except Exception as e:
            self.logError(str(e))

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    uiC = UIControler()
    uiC.show()
    uiC.updateCommandList() 
    sys.exit(app.exec_())
