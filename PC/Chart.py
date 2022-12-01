from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot 

class Chart(QtChart.QChart):
    def __init__(self):
        QtChart.QChart.__init__(self)

        self.tempPoints = []
        self.humidPoints = []

        self.lineSeriesTemp = QtChart.QLineSeries()
        self.lineSeriesHumid = QtChart.QLineSeries()
        self.scatterSeriesTemp = QtChart.QScatterSeries()
        self.scatterSeriesHumid = QtChart.QScatterSeries()

        self.addSeries(self.lineSeriesTemp)
        self.addSeries(self.lineSeriesHumid)
        self.addSeries(self.scatterSeriesTemp)
        self.addSeries(self.scatterSeriesHumid)

        self.xAxis = QtChart.QValueAxis()
        self.xAxis.setMin(0)
        self.xAxis.setMax(100)
        self.xAxis.setTitleText("Time [s]")
        self.addAxis(self.xAxis, QtCore.Qt.AlignBottom)

        self.yAxis = QtChart.QValueAxis()
        self.yAxis.setMin(-40.)
        self.yAxis.setMax(80.)
        self.yAxis.setTickCount(13)
        self.yAxis.setTitleText(r'Value')
        self.addAxis(self.yAxis, QtCore.Qt.AlignLeft)

        self.lineSeriesTemp.attachAxis(self.xAxis)
        self.scatterSeriesTemp.attachAxis(self.xAxis)
        self.lineSeriesHumid.attachAxis(self.xAxis)
        self.scatterSeriesHumid.attachAxis(self.xAxis)

        self.lineSeriesTemp.attachAxis(self.yAxis)
        self.scatterSeriesTemp.attachAxis(self.yAxis)
        self.lineSeriesHumid.attachAxis(self.yAxis)
        self.scatterSeriesHumid.attachAxis(self.yAxis)


    def addHumidPoint(self, point : QtCore.QPointF):
        self.humidPoints.append(point)
        self.updatePoints()

    def addTempPoint(self, point : QtCore.QPointF):
        self.tempPoints.append(point)
        self.updatePoints()

    def updatePoints(self):
        self.lineSeriesTemp.clear()
        self.lineSeriesHumid.clear()
        self.scatterSeriesTemp.clear()
        self.scatterSeriesHumid.clear()

        for i in self.tempPoints:
            self.lineSeriesTemp << i
            self.scatterSeriesTemp << i
        for i in self.humidPoints:
            self.lineSeriesHumid << i
            self.scatterSeriesTemp << i
        
        self.update()

    def test(self):
        self.updatePoints()
        for i in range(10):
            self.scatterSeriesHumid << QtCore.QPointF(i, i) 
            self.lineSeriesHumid << QtCore.QPointF(i, i) 

        self.update()
    
    def addPoint(self, x : float, y : float, isHumid : bool):
        if isHumid:
            self.addHumidPoint(QtCore.QPointF(x, y))
        else:
            self.addTempPoint(QtCore.QPointF(x, y))
        self.updatePoints()

    @Slot()
    def clearChart(self):
        self.tempPoints.clear()
        self.humidPoints.clear()
        self.updatePoints()
            