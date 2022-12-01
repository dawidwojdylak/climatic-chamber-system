from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot, Signal

class ChartView(QtChart.QChartView):
    def __init__(self, chart = None, parent = None):
        QtChart.QChartView.__init__(self)
        self.chart = chart
        self.parent = parent
        # If true draw humidity, if not draw temperature
        self.humidityOptionChecked = True 
        
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        wPos = event.localPos()
        sPos = self.mapToScene(int(wPos.x()), int(wPos.y()))
        chartItemPos = self.mapFromScene(sPos)
        self.currentCursorPosOnChart = self.chart.mapToValue(chartItemPos)

        self.currentCursorPosOnChart = QtCore.QPointF(
            round(2 * self.currentCursorPosOnChart.x()) / 2,
            round(2 * self.currentCursorPosOnChart.y()) / 2,
        )

        self.parent.onMouseOnChartMoved(
            round(self.currentCursorPosOnChart.x(), 1), 
                round(self.currentCursorPosOnChart.y(),1)
        )
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.chart.addPoint(
                round(self.currentCursorPosOnChart.x(), 1), 
                round(self.currentCursorPosOnChart.y(),1),
                self.humidityOptionChecked)

        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(event)

    @Slot(bool)
    def humidityOptionChecked1(self, val):
        self.humidityOptionChecked = val
