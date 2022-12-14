from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot 

class Chart(QtChart.QChart):
    def __init__(self, parent = None):
        QtChart.QChart.__init__(self)
        self.parent = parent

        self.tempPoints = []
        self.humidPoints = []
        self.scatterEnable = True
        # If true draw humidity, if not draw temperature
        self.isHumid = True

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
        # self.xAxis.setTickAnchor(0.)
        # self.xAxis.setTickInterval(10.)
        # self.xAxis.setTickType(QtCore.Qt.QValueAxis.TicksFixed)
        # self.xAxis.setTickCount(10)
        self.xAxis.setTitleText("Time [min]")
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

    def drawPoints(self):
        self.lineSeriesTemp.clear()
        self.lineSeriesHumid.clear()
        self.scatterSeriesTemp.clear()
        self.scatterSeriesHumid.clear()

        for i in self.tempPoints:
            self.lineSeriesTemp << i
            if self.scatterEnable:
                self.scatterSeriesTemp << i
        for i in self.humidPoints:
            self.lineSeriesHumid << i
            if self.scatterEnable:
                self.scatterSeriesHumid << i
        
        self.update()

    def updateDelta(self):
        delta = -1
        if self.isHumid and len(self.humidPoints) > 1:
            delta = abs(self.humidPoints[-1].x() - self.humidPoints[-2].x())
        elif len(self.tempPoints) > 1:
            delta = abs(self.tempPoints[-1].x() - self.tempPoints[-2].x())
        self.parent.onPointAdded(delta)

    def addHumidPoint(self, point : QtCore.QPointF):
        HOR_TOL = 2
        if len(self.humidPoints) > 0:
            if abs(self.humidPoints[-1].y() - point.y()) <= HOR_TOL:
                point.setY(self.humidPoints[-1].y())
            if point.x() <= self.humidPoints[-1].x():
                point.setX(self.humidPoints[-1].x() + 0.1)
        if point.y() < 0.: 
            point.setY(0.)
        self.humidPoints.append(point)
        self.drawPoints()

    def addTempPoint(self, point : QtCore.QPointF):
        HOR_TOL = 2
        if len(self.tempPoints) > 0:
            if abs(self.tempPoints[-1].y() - point.y()) <= HOR_TOL:
                point.setY(self.tempPoints[-1].y())
            if point.x() <= self.tempPoints[-1].x():
                point.setX(self.tempPoints[-1].x() + 0.1)
        self.tempPoints.append(point)
        self.drawPoints()

    def addPoint(self, x : float, y : float):
        if self.isHumid:
            self.addHumidPoint(QtCore.QPointF(x, y))
        else:
            self.addTempPoint(QtCore.QPointF(x, y))
        self.updateDelta()

    def zoom(self, factor: float) -> None:
        super().zoom(factor)
        self.yAxis.setMin(-40.)
        self.yAxis.setMax(80.)
        
    def getScripts(self):
        # remember to send humid and temp commands simultaneously
        humidScript = ""
        if (len(self.humidPoints) < 1 or len(self.tempPoints) < 1): return
        h = self.humidPoints
        if h[0].x() > 0:
            humidScript += "sleep(" + str(h[0].x()) + ")\n"
        for i in range(1, len(h)):
            delta_t = h[i].x() - h[i-1].x()
            if h[i].y() - h[i-1].y() == 0:
                humidScript += "set_humidity(" + str(h[i].y()) + ")\nsleep(" + str(delta_t) + ")\n"
            elif h[i].y() - h[i-1].y() > 0:
                a = (h[i].y() - h[i-1].y()) / (h[i].x() - h[i-1].x())                
                humidScript += "set_humidity_gradient_up(" + str(round(a, 2)) + ")\nsleep(" + str(delta_t) + ")\n"
            elif h[i].y() - h[i-1].y() < 0:
                a = (h[i].y() - h[i-1].y()) / (h[i].x() - h[i-1].x())                
                humidScript += "set_humidity_gradient_down(" + str(-round(a, 2)) + ")\nsleep(" + str(delta_t) + ")\n"
        tempScript = ""
        h = self.tempPoints
        if h[0].x() > 0:
            tempScript += "sleep(" + str(h[0].x()) + ")\n"
        for i in range(1, len(h)):
            delta_t = h[i].x() - h[i-1].x()
            if h[i].y() - h[i-1].y() == 0:
                tempScript += "set_temperature(" + str(h[i].y()) + ")\nsleep(" + str(delta_t) + ")\n"
            elif h[i].y() - h[i-1].y() > 0:
                a = (h[i].y() - h[i-1].y()) / (h[i].x() - h[i-1].x())                
                tempScript += "set_temperature_gradient_up(" + str(round(a, 2)) + ")\nsleep(" + str(delta_t) + ")\n"
            elif h[i].y() - h[i-1].y() < 0:
                a = (h[i].y() - h[i-1].y()) / (h[i].x() - h[i-1].x())                
                tempScript += "set_temperature_gradient_down(" + str(-round(a, 2)) + ")\nsleep(" + str(delta_t) + ")\n"
    
    @Slot(bool)
    def humidityOptionChecked(self, val):
        self.isHumid = val
        self.updateDelta()

    @Slot()
    def clearChart(self):
        self.tempPoints.clear()
        self.humidPoints.clear()
        self.zoomReset()
        self.drawPoints()
        self.parent.onPointAdded(-1.)

    @Slot() 
    def scatterEnabled(self, enabled : bool):
        self.scatterEnable = enabled
        self.drawPoints()
            

    @Slot()
    def deleteLastPoint(self):
        if self.isHumid and len(self.humidPoints):
            self.humidPoints.pop()
        elif len(self.tempPoints):
            self.tempPoints.pop()
        self.drawPoints()