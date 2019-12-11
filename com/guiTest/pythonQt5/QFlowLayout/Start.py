# -*- coding: utf-8 -*-
import os
import sys
from os import listdir

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from QFlowLayout.CustomLayout import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.openfile.triggered.connect(self._openfiles)
        self.openfolder.triggered.connect(self._openfolder)

    def _openfolder(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        list_name = []
        self._listdir(directory1, list_name)
        print(list_name)

    def _openfiles(self):
        files, file_type = QFileDialog.getOpenFileNames(self, "多文件选择", "./", "All Files (*)")
        list_name = []
        for file in files:
            if self.judge_file_is_movie(file):
                list_name.append(file)
        print(list_name)

    def _listdir(self, path, list_name):  # 传入存储的list
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                self._listdir(file_path, list_name)
            else:
                if self.judge_file_is_movie(file_path):
                    list_name.append(file_path)

    # 判断是不是视频
    def judge_file_is_movie(self, file_name):
        return file_name.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso', '.rmvb', 'mov', 'rm', '3GP', 'FLV'))




if __name__ == "__main__":
    os.makedirs("cache", exist_ok=True)
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    win.scrollArea._widget.load()
    sys.exit(app.exec_())
