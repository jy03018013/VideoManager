# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from QFlowLayout.CustomLayout import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    os.makedirs("cache", exist_ok=True)
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    win.scrollArea._widget.load()
    sys.exit(app.exec_())
