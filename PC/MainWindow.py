# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_centralWidget = QtWidgets.QHBoxLayout()
        self.horizontalLayout_centralWidget.setObjectName("horizontalLayout_centralWidget")
        self.verticalLayout_sideBar = QtWidgets.QVBoxLayout()
        self.verticalLayout_sideBar.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_sideBar.setObjectName("verticalLayout_sideBar")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_sideBar.addWidget(self.pushButton_login)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.verticalLayout_sideBar.addWidget(self.pushButton_logout)
        self.line_chart = QtWidgets.QFrame(self.centralwidget)
        self.line_chart.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_chart.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_chart.setObjectName("line_chart")
        self.verticalLayout_sideBar.addWidget(self.line_chart)
        self.pushButton_logClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logClear.setObjectName("pushButton_logClear")
        self.verticalLayout_sideBar.addWidget(self.pushButton_logClear)
        self.label_chart = QtWidgets.QLabel(self.centralwidget)
        self.label_chart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chart.setObjectName("label_chart")
        self.verticalLayout_sideBar.addWidget(self.label_chart)
        self.radioButton_chartHumidity = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_chartHumidity.setObjectName("radioButton_chartHumidity")
        self.verticalLayout_sideBar.addWidget(self.radioButton_chartHumidity)
        self.radioButton_chartTemperature = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_chartTemperature.setObjectName("radioButton_chartTemperature")
        self.verticalLayout_sideBar.addWidget(self.radioButton_chartTemperature)
        self.checkBox_chartScatter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chartScatter.setChecked(True)
        self.checkBox_chartScatter.setObjectName("checkBox_chartScatter")
        self.verticalLayout_sideBar.addWidget(self.checkBox_chartScatter)
        self.label_chartMousePos = QtWidgets.QLabel(self.centralwidget)
        self.label_chartMousePos.setText("")
        self.label_chartMousePos.setObjectName("label_chartMousePos")
        self.verticalLayout_sideBar.addWidget(self.label_chartMousePos)
        self.label_chartDeltaT = QtWidgets.QLabel(self.centralwidget)
        self.label_chartDeltaT.setText("")
        self.label_chartDeltaT.setObjectName("label_chartDeltaT")
        self.verticalLayout_sideBar.addWidget(self.label_chartDeltaT)
        self.pushButton_chartSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chartSend.setObjectName("pushButton_chartSend")
        self.verticalLayout_sideBar.addWidget(self.pushButton_chartSend)
        self.pushButton_chartDeleteLast = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chartDeleteLast.setObjectName("pushButton_chartDeleteLast")
        self.verticalLayout_sideBar.addWidget(self.pushButton_chartDeleteLast)
        self.pushButton_chartClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chartClear.setObjectName("pushButton_chartClear")
        self.verticalLayout_sideBar.addWidget(self.pushButton_chartClear)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_sideBar.addItem(spacerItem)
        self.horizontalLayout_centralWidget.addLayout(self.verticalLayout_sideBar)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_centralWidget.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.ChartTab = QtWidgets.QWidget()
        self.ChartTab.setObjectName("ChartTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ChartTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.ChartTab, "")
        self.CommandsTab = QtWidgets.QWidget()
        self.CommandsTab.setObjectName("CommandsTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CommandsTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.CommandsTab)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.CommandsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.listWidget_commandList = QtWidgets.QListWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_commandList.sizePolicy().hasHeightForWidth())
        self.listWidget_commandList.setSizePolicy(sizePolicy)
        self.listWidget_commandList.setObjectName("listWidget_commandList")
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_userInput1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_userInput1.setObjectName("horizontalLayout_userInput1")
        self.label_userInput1 = QtWidgets.QLabel(self.CommandsTab)
        self.label_userInput1.setObjectName("label_userInput1")
        self.horizontalLayout_userInput1.addWidget(self.label_userInput1)
        self.doubleSpinBox_userInput1 = QtWidgets.QDoubleSpinBox(self.CommandsTab)
        self.doubleSpinBox_userInput1.setSingleStep(0.1)
        self.doubleSpinBox_userInput1.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_userInput1.setObjectName("doubleSpinBox_userInput1")
        self.horizontalLayout_userInput1.addWidget(self.doubleSpinBox_userInput1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_userInput1)
        self.pushButton_sendCommand = QtWidgets.QPushButton(self.CommandsTab)
        self.pushButton_sendCommand.setObjectName("pushButton_sendCommand")
        self.verticalLayout_2.addWidget(self.pushButton_sendCommand)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.CommandsTab)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.textBrowser_chamberResponse = QtWidgets.QTextBrowser(self.CommandsTab)
        self.textBrowser_chamberResponse.setObjectName("textBrowser_chamberResponse")
        self.verticalLayout_4.addWidget(self.textBrowser_chamberResponse)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.CommandsTab, "")
        self.horizontalLayout_centralWidget.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout_centralWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_checkConnection = QtWidgets.QAction(MainWindow)
        self.action_checkConnection.setObjectName("action_checkConnection")
        self.actionConnect_to_server = QtWidgets.QAction(MainWindow)
        self.actionConnect_to_server.setObjectName("actionConnect_to_server")
        self.actionClose_connection = QtWidgets.QAction(MainWindow)
        self.actionClose_connection.setObjectName("actionClose_connection")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_xml_config_file = QtWidgets.QAction(MainWindow)
        self.actionImport_xml_config_file.setObjectName("actionImport_xml_config_file")
        self.actionSave_script = QtWidgets.QAction(MainWindow)
        self.actionSave_script.setObjectName("actionSave_script")
        self.actionOpen_script = QtWidgets.QAction(MainWindow)
        self.actionOpen_script.setObjectName("actionOpen_script")
        self.menuFile.addAction(self.actionConnect_to_server)
        self.menuFile.addAction(self.action_checkConnection)
        self.menuFile.addAction(self.actionClose_connection)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_xml_config_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_script)
        self.menuFile.addAction(self.actionOpen_script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_login.setText(_translate("MainWindow", "Log In"))
        self.pushButton_logout.setText(_translate("MainWindow", "Log out"))
        self.pushButton_logClear.setText(_translate("MainWindow", "Clear"))
        self.label_chart.setText(_translate("MainWindow", "Plot settings"))
        self.radioButton_chartHumidity.setText(_translate("MainWindow", "Humidity"))
        self.radioButton_chartTemperature.setText(_translate("MainWindow", "Temperature"))
        self.checkBox_chartScatter.setText(_translate("MainWindow", "Scatter"))
        self.pushButton_chartSend.setText(_translate("MainWindow", "Send"))
        self.pushButton_chartDeleteLast.setText(_translate("MainWindow", "Delete last point"))
        self.pushButton_chartClear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ChartTab), _translate("MainWindow", "Chart"))
        self.label.setText(_translate("MainWindow", "Available commands"))
        self.label_userInput1.setText(_translate("MainWindow", "Value to set"))
        self.pushButton_sendCommand.setText(_translate("MainWindow", "Send command"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.textBrowser_chamberResponse.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CommandsTab), _translate("MainWindow", "Commands"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_checkConnection.setText(_translate("MainWindow", "Check connection"))
        self.actionConnect_to_server.setText(_translate("MainWindow", "Connect to server"))
        self.actionClose_connection.setText(_translate("MainWindow", "Close connection"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionImport_xml_config_file.setText(_translate("MainWindow", "Import .xml config file"))
        self.actionSave_script.setText(_translate("MainWindow", "Save script..."))
        self.actionOpen_script.setText(_translate("MainWindow", "Open script..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
