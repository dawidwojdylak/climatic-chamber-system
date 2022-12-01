from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot 

class ChartView(QtChart.QChartView):
    def __init__(self, chart = None):
        QtChart.QChartView.__init__(self)
        self.chart = chart
        # If true draw humidity, if not draw temperature
        self.humidityOptionChecked = True 

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        # print("mmove")
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            pass

        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        print("mrelease")
        return super().mouseReleaseEvent(event)

    @Slot(bool)
    def humidityOptionChecked1(self, val):
        self.humidityOptionChecked = val
        print(self.humidityOptionChecked)