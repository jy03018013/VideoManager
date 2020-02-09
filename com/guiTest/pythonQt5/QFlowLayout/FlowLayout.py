from PyQt5 import sip

from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtWidgets import (QApplication, QLayout, QPushButton, QSizePolicy, QWidget)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.flowLayout = FlowLayout()
        self.Short = QPushButton("Short wfawfwfawfwaf")
        self.Short.clicked.connect(self.press)
        self.flowLayout.addWidget(self.Short)
        self.flowLayout.addWidget(QPushButton("awfwfw WWWWW"))
        self.flowLayout.addWidget(QPushButton("gawgrr WWff"))
        self.flowLayout.addWidget(QPushButton("wfwfaw "))
        self.button = QPushButton("Test")
        self.button.clicked.connect(self.refresh_pushButton_clicked)
        self.flowLayout.addWidget(self.button)
        self.setLayout(self.flowLayout)
        self.setWindowTitle("Flow Layout")

    # 测试控件删除
    def refresh_pushButton_clicked(self):
        self.flowLayout.removeWidget(self.Short)
        sip.delete(self.Short)

        # layout:QWidget = self.flowLayout.itemList[0]
        # self.flowLayout.removeItem(layout) # 加载之前先清空子控件
        # sip.delete(layout)
        print(self.flowLayout.itemList.__len__())
        # self.scrollArea._widget.load()
        print("刷新成功")
    def press(self):
        print("press")


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())
