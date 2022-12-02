from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PySide2.QtCore import Slot, Signal

class ChartView(QtChart.QChartView):
    def __init__(self, chart = None, parent = None):
        QtChart.QChartView.__init__(self)
        self.chart = chart
        self.parent = parent
        self.zoomFactor = 1.
        
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
                round(self.currentCursorPosOnChart.y(),1)
                )

        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        # self.chart.zoomReset()
        # dx = 1.
        # dx *= .5 if event.angleDelta().x() > 0 else 2.
        # rect = self.chart.plotArea()
        # cent = self.chart.plotArea().center()
        # rect.setWidth(dx * rect.width())
        # rect.moveCenter(cent)
        # self.chart.zoomIn(rect)

        # event.accept()
        
        # self.chart.zoomReset()
        
        self.zoomFactor += 1. if event.angleDelta().y() > 0 else -1.
        if self.zoomFactor >= 3.: 
            self.zoomFactor = 3.
            return 

        width = self.chart.plotArea().width()
        if self.zoomFactor > 0:
            width = self.chart.plotArea().width() / self.zoomFactor
        elif self.zoomFactor < 0:
            width = self.chart.plotArea().width() * -self.zoomFactor

        rect = QtCore.QRectF(
            self.chart.plotArea().left(), 
            self.chart.plotArea().top(),
            width, 
            self.chart.plotArea().height()
        )

        print(self.zoomFactor)
        if self.zoomFactor > 0:
            self.chart.zoomIn(rect)
        elif self.zoomFactor < 0:
            self.chart.zoomReset() 
            self.chart.zoomIn(rect)

        # factor = event.angleDelta().y()
        # factor = .5 if factor > 0 else 2.
        # self.chart.zoom(factor)

        return super().wheelEvent(event)