from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot, Signal

class ChartView(QtChart.QChartView):
    # mouseMovedSignal = Signal(float, float)
    def __init__(self, chart = None):
        QtChart.QChartView.__init__(self)
        self.chart = chart
        # If true draw humidity, if not draw temperature
        self.humidityOptionChecked = True 
        
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        wPos = event.localPos()
        sPos = self.mapToScene(int(wPos.x()), int(wPos.y()))
        chartItemPos = self.mapFromScene(sPos)
        self.currentCursorPosOnChart = self.chart.mapToValue(chartItemPos)
        # self.mouseMovedSignal.emit(
        #     round(self.currentCursorPosOnChart.x(), 1), 
        #         round(self.currentCursorPosOnChart.y(),1)
        # )
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.chart.addPoint(
                round(self.currentCursorPosOnChart.x(), 1), 
                round(self.currentCursorPosOnChart.y(),1),
                self.humidityOptionChecked)

        # self.mouseMovedSignal.emit(1,2)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(event)

    @Slot(bool)
    def humidityOptionChecked1(self, val):
        self.humidityOptionChecked = val
        