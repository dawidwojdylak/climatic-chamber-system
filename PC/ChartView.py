from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot, Signal

class ChartView(QtChart.QChartView):
    def __init__(self, chart = None, parent = None):
        QtChart.QChartView.__init__(self)
        self.chart = chart
        self.parent = parent
        self.zoomFactor = 1.
        self.ctrlClicked = False
        
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        wPos = event.localPos()
        sPos = self.mapToScene(int(wPos.x()), int(wPos.y()))
        chartItemPos = self.mapFromScene(sPos)
        self.currentCursorPosOnChart = self.chart.mapToValue(chartItemPos)
        self.currentCursorPosOnChart = QtCore.QPointF(
            round(2 * self.currentCursorPosOnChart.x()) / 2,
            round(2 * self.currentCursorPosOnChart.y()) / 2,
        )

        self.parent.onMouseOnChartHover(
            round(self.currentCursorPosOnChart.x(), 1), 
                round(self.currentCursorPosOnChart.y(),1)
        )
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.chart.addPoint(
                round(self.currentCursorPosOnChart.x(), 1), 
                round(self.currentCursorPosOnChart.y(),1)
                )

        return super().mousePressEvent(event)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        if self.ctrlClicked:
            factor = event.angleDelta().y()
            factor = .8 if factor > 0 else 1.2
            self.chart.zoom(factor)

        else: 
            self.chart.scroll(self.chart.plotArea().width() / (50*120) * event.angleDelta().y(), 0)
        return super().wheelEvent(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlClicked = True
        return super().keyPressEvent(event)


    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlClicked = False
        return super().keyReleaseEvent(event)
