# -*- coding: utf-8 -*-
import os
import sys
from os import listdir
from moviepy.editor import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from QFlowLayout.CustomLayout import Ui_MainWindow
from CommonUtils import file_md5
from SqlUtils import SqlUtils


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.openfile.triggered.connect(self._openfiles)
        self.openfolder.triggered.connect(self._openfolder)

    def _process_video_list(self, video_list):
        for video_path in video_list:
            _hash = file_md5(video_path)
            _video_name = video_path[video_path.rfind('/') + 1:video_path.rfind('.')]
            img_path = "cache/covergif/" + _video_name + ".gif"
            if not (os.path.exists(img_path)):
                # todo 自定义时间段和时间间隔
                # 现在切割T = 4和6秒之间的剪辑
                clip = (VideoFileClip(video_path).subclip(1, 3).resize(0.1))
                clip.write_gif(img_path)  # gif将有30 fps
            # sql = "INSERT INTO video (video_name,hash,img_type) VALUES ("+_video_name+", "+_hash+",2 )"
            sql = "INSERT INTO video (video_name,hash,img_type) VALUES (?,?,?)"
            SqlUtils.insert_video(sql, (_video_name, _hash, 2))
            print(_hash)

    def _openfolder(self):
        directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        if directory.strip() == "":
            return
        video_list = []
        self._listdir(directory, video_list)
        self._process_video_list(video_list)

    def _openfiles(self):
        files, file_type = QFileDialog.getOpenFileNames(self, "多文件选择", "./", "All Files (*)")
        if len(files) == 0:
            return
        video_list = []
        for file in files:
            if self.judge_file_is_movie(file):
                video_list.append(file)
        self._process_video_list(video_list)

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
