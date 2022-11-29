from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

class ChartView(QtChart.QChartView):
    def __init__(self, chart):
        super().__init__(self)
        self.chart = chart

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        print("mmove")
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print("mpress")
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        print("mrelease")
        return super().mouseReleaseEvent(event)