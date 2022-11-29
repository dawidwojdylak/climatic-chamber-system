from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

class Chart(QtChart.QChart):
    def __init__(self):
        QtChart.QChart.__init__(self)

        self.lineSeriesTemp = QtChart.QLineSeries()
        self.lineSeriesHumid = QtChart.QLineSeries()
        self.scatterSeriesTemp = QtChart.QScatterSeries()
        self.scatterSeriesHumid = QtChart.QScatterSeries()

        self.lineSeriesTemp << QtCore.QPointF(11, 2) << QtCore.QPointF(2, 11)

        self.addSeries(self.lineSeriesTemp)
        self.addSeries(self.lineSeriesHumid)
        self.addSeries(self.scatterSeriesTemp)
        self.addSeries(self.scatterSeriesHumid)

        self.xAxis = QtChart.QValueAxis()
        self.xAxis.setMin(0)
        self.xAxis.setMax(100)
        # self.xAxis.set
        self.addAxis(self.xAxis, QtCore.Qt.AlignBottom)

        self.yAxis = QtChart.QValueAxis()
        self.yAxis.setMin(-40.)
        self.yAxis.setMax(80.)
        self.yAxis.setTickInterval(10.)
        self.addAxis(self.yAxis, QtCore.Qt.AlignLeft)

        self.yAxis = QtChart.QValueAxis

        
        self.update()