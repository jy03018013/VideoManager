from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel


class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()
