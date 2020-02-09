# coding:utf-8
from PyQt5.QtWidgets import QMainWindow, QProgressBar, QApplication, QLabel, QPushButton
import sys
import numpy as np


class SampleBar(QMainWindow):
    """Main Application"""

    def __init__(self, parent=None):
        super(SampleBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Pre Params:
        self.setMinimumSize(800, 600)

        # File Menus & Status Bar:
        self.statusBar().showMessage('准备中...')
        self.progressBar = QPushButton("按键显示新的数据")
        self.label = QLabel()
        self.label2 = QLabel()
        self.set2("显示第二个数字")
        self.sets("显示第一个数字")
        self.progressBar.clicked.connect(self.suijishu)
        self.statusBar().addPermanentWidget(self.progressBar, stretch=3)

    def suijishu(self):
        suijishu = 0
        for _ in range(1):
            suijishu = np.random.uniform(1, 5)
        self.sets(text=str(suijishu))
        self.set2(text=str(suijishu * 110))

    def sets(self, text):
        self.label.clear()
        self.label.setText(text)
        self.statusBar().addPermanentWidget(self.label, stretch=3)

    def set2(self, text):
        # self.statusBar().addPermanentWidget(self.label)
        self.label2.clear()
        self.label2.setText(text)
        self.statusBar().addPermanentWidget(self.label2, stretch=4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main2 = SampleBar()
    main2.show()
    sys.exit(app.exec_())
