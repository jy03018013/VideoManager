# -*- coding: utf-8 -*-
import configparser

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from moviepy.editor import *
import re
import CommonUtils
import QQSettingPanel
from CommonUtils import file_md5
from QFlowLayout.CustomLayout import Ui_MainWindow
from SqlUtils import SqlUtils
from custom_lab_widget import custom_lab_widget


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.openfile.triggered.connect(self._openfiles)
        self.openfolder.triggered.connect(self._openfolder)
        self.setting.triggered.connect(self._set_settings)
        self.setting_window = QQSettingPanel.Window()

        self.edit_tab.triggered.connect(self._edit_tab)
        self.edit_tab_window = custom_lab_widget()

    def _edit_tab(self):
        self.edit_tab_window.show()

    def _set_settings(self):
        self.setting_window.show()

    def _process_video_list(self, video_list):
        config = CommonUtils.read_config()
        for video_path in video_list:
            _hash = file_md5(video_path)
            if SqlUtils.hash_exists(_hash):
                # todo
                print("数据库中已存在Hash相同的视频")
            else:
                try:
                    video_path = video_path.replace("\\", "/")
                    _video_name = video_path[video_path.rfind('/') + 1:video_path.rfind('.')]
                    _qb_identifier = self._get_qb_identifier(config, _video_name)
                    print(_video_name + " : " + _qb_identifier)
                except Exception as e:
                    print(e)
                    pass
                img_path = "cache/covergif/" + _video_name + ".gif"
                if not (os.path.exists(img_path)):
                    clip = (VideoFileClip(video_path)
                            .subclip(config.get('DEFAULT', 'gif_start'),
                                     config.get('DEFAULT', 'gif_end')).resize(config.get('DEFAULT', 'gif_interval')))
                    clip.write_gif(img_path)
                # sql = "INSERT INTO video (video_name,hash,img_type) VALUES ("+_video_name+", "+_hash+",2 )"
                sql = "INSERT INTO video (video_name,hash,img_type,video_path) VALUES (?,?,?,?)"
                SqlUtils.insert_video(sql, (_video_name, _hash, 2, video_path))
                print(_hash)

    def _get_qb_identifier(self, config, _video_name):
        _video_name_upper = _video_name.upper()
        qb_identifier_str = config.get('DEFAULT', 'qb_identifier')
        qb_identifier_arr = qb_identifier_str.split(",")
        for series in qb_identifier_arr:
            try:
                series_upper = series.upper()
                if series_upper in _video_name_upper:
                    pattern = re.compile(str(series_upper) + '(.*?)\d+')  # 用于匹配指定符号及其后的数字及中间的字符串
                    m = pattern.search(_video_name_upper)
                    pattern = re.compile('\d+')  # 匹配数字
                    n = pattern.search(m.group().replace(series_upper, ""))  # 防止300MIUM-010 : 300MIUM-300
                    num = n.group()
                    if len(num) > 3:
                        num = num.lstrip("0")
                    return series_upper + "-" + num
            except Exception as e:
                print(e)
                pass
        print("无法识别：" + _video_name)
        return ""

    def _openfolder(self):
        try:
            directory = QFileDialog.getExistingDirectory(self, "选取文件夹", self._get_last_open_folder())  # 起始路径
            if directory.strip() == "":
                return
            self._save_last_open_folder(directory)
            video_list = []
            self._listdir(directory, video_list)
            self._process_video_list(video_list)
        except Exception as e:
            print(e)
            pass

    def _openfiles(self):
        try:
            files, file_type = QFileDialog.getOpenFileNames(self, "多文件选择", self._get_last_open_folder(),
                                                            "All Files (*)")
            # files, file_type = QFileDialog.getOpenFileName(self, 'Open File', '',  "All Files (*)",options = QFileDialog.DontUseNativeDialog)
            if len(files) == 0:
                return
            self._save_last_open_folder(files[0])
            video_list = []
            for file in files:
                if self.judge_file_is_movie(file):
                    video_list.append(file)
            self._process_video_list(video_list)
        except Exception as e:
            print(e)
            pass

    def _get_last_open_folder(self):
        try:
            config = CommonUtils.read_config()
            return config['DEFAULT']['last_open_folder']
        except Exception as e:
            print(e)
            return "./"

    def _save_last_open_folder(self, path):
        try:
            config = CommonUtils.read_config()
            config.set('DEFAULT', 'last_open_folder', path)
            config.write(open('setting.ini', 'w', encoding='UTF-8'))
        except Exception as e:
            print(e)
            pass

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
        return file_name.lower().endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso', '.rmvb', 'mov', 'rm', '3gp', 'flv'))


if __name__ == "__main__":
    os.makedirs("cache", exist_ok=True)
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    win.scrollArea._widget.load()
    # app.setStyleSheet(open("otherPage/Data/style.qss", "rb").read().decode("utf-8"))
    sys.exit(app.exec_())
