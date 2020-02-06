import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser, QScrollArea
import os

class Demo(QScrollArea):  # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)  # 2

    def dragEnterEvent(self, QDragEnterEvent):  # 3
        print('Drag Enter')
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()

    # def dragMoveEvent(self, QDragMoveEvent):  # 4
    #     print('Drag Move')
    #
    # def dragLeaveEvent(self, QDragLeaveEvent):  # 5
    #     print('Drag Leave')

    def dropEvent(self, QDropEvent):  # 6
        for path in QDropEvent.mimeData().text().split("\n"):
            path = path.replace("file:///","")
            if os.path.isdir(path):
                print("isdir")
            elif os.path.isfile(path):
                print("isfile")
            else:
                print("nothing "+path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
