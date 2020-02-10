# -*- coding: utf-8 -*-
from PyQt5 import sip

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from moviepy.editor import *
import re
from ScrollWindow import ScrollWindow
from utils import CommonUtils
import QQSettingPanel
from QFlowLayout.CustomLayout import Ui_MainWindow
from SqlUtils import SqlUtils
from custom_lab_widget import custom_lab_widget


# from utils.AddMovieUtils import _openfolder, _openfiles, get_video_type, _get_qb_identifier


class MainForm(QMainWindow, Ui_MainWindow):
    # 初始化
    def __init__(self):
        super(MainForm, self).__init__()
        self.setAcceptDrops(True)
        self.setupUi(self)
        self.setting_window = QQSettingPanel.Window()
        self.edit_tab_window = custom_lab_widget()

        # import os
        # os.path.exists("C:\\Users\\Administrator\\Desktop\\视频\\Rename Pro.exe")

        self.open_file_action.triggered.connect(self._openfiles)
        self.open_folder_action.triggered.connect(self._openfolder)
        self.open_setting_action.triggered.connect(self._set_settings)
        self.edit_tab_action.triggered.connect(self._edit_tab)
        self.downlowd_infoaction_action.triggered.connect(self._downlowd_info)
        self.downlowd_img_action.triggered.connect(self._downlowd_img)
        self.refresh_pushButton.clicked.connect(self.refresh_pushButton_clicked)
        self.statusbar.showMessage("启动完成", 5000)

    def refresh_pushButton_clicked(self):
        self.verticalLayout_2.removeWidget(self.scrollArea)  # 加载之前先清空子控件
        sip.delete(self.scrollArea)# 删除控件的一个坑 https://my.oschina.net/yehun/blog/1813698
        self.scrollArea = ScrollWindow()
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.scrollArea._widget.load()
        print("刷新成功")

    # 不能删，否则拖拽无效
    def dragEnterEvent(self, QDragEnterEvent):
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()

    # 覆写拖拽事件，可以将电影拖拽入库
    def dropEvent(self, QDropEvent):
        for path in QDropEvent.mimeData().text().split("\n"):
            path = path.replace("file:///", "")
            if os.path.isdir(path):
                self.process_folder(path)
                print("isdir")
            elif os.path.isfile(path):
                self.process_files([path])
                print("isfile")

    # 下载电影信息
    def _downlowd_info(self):
        video_list = SqlUtils._select_("SELECT identifier,hash from video where is_download = 0 and type = 1")
        for video in video_list:
            self.statusbar.showMessage("下载影片信息中， 影片本地名称：" + video[1] + " 识别码：" + video[0])
            CommonUtils.get_video_info(video[0], video[1], 1)
            self.statusbar.showMessage("影片-" + video[1] + "-信息下载完成")
        self.statusbar.showMessage("所有影片信息下载完成")

    # 下载电影图片
    def _downlowd_img(self):
        video_list = SqlUtils._select_(
            "SELECT video_name_local,img_url,hash from video where is_download = 1 and type = 1")
        for video in video_list:
            if not (os.path.exists('cache/coverimg/' + video[0] + '.jpg')):
                is_success_download_img = CommonUtils.download_img(video[0], video[1])
                if is_success_download_img:
                    sql = "UPDATE video SET is_download = ? WHERE hash = ?"
                    SqlUtils.update_video(sql, (2, video[2]))
                    self.statusbar.showMessage("图片下载成功", 5000)
                    print("2222")

    def _downlowd_info_and_img(self):
        print("3333")

    def _edit_tab(self):
        self.edit_tab_window.show()

    def _set_settings(self):
        self.setting_window.show()

    # 生成gif封面图
    def make_gif_cover(self, _video_name, video_path, config):
        img_url = "cache/covergif/" + _video_name + ".gif"
        if not (os.path.exists(img_url)):
            clip = (VideoFileClip(video_path)
                    .subclip(config.get('DEFAULT', 'gif_start'),
                             config.get('DEFAULT', 'gif_end')).resize(config.get('DEFAULT', 'gif_interval')))
            clip.write_gif(img_url)

    # 处理导入的电影列表
    def _process_video_list(self, video_list):
        config = CommonUtils.read_config()
        image_type = config.get('DEFAULT', 'default_img_type')
        qb_identifier_str = config.get('DEFAULT', 'qb_identifier')
        qb_identifier_arr = qb_identifier_str.split(",")
        for _video_path in video_list:
            _video_path = _video_path.replace("\\", "/")
            _video_name = _video_path[_video_path.rfind('/') + 1:_video_path.rfind('.')]
            _hash = _video_name
            # _hash = file_md5(_video_path)
            is_exists, video_path_in_datebase = SqlUtils.hash_exists(_hash)
            if is_exists:
                if video_path_in_datebase != _video_path:
                    reply = QMessageBox.question(None, _video_name, "数据库中已存在名称相同的视频，是否更新视频路径？",
                                                 QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        sql = "UPDATE video SET video_path = ?,video_name_local=? WHERE hash = ?"
                        SqlUtils.update_video(sql, (_video_path, _video_name, _hash))
                        self.statusbar.showMessage("更新路径完成", 5000)
            else:
                _identifier = ""
                _serious = ""
                _video_type = 0
                try:
                    _video_type = self.get_video_type(_video_name, qb_identifier_arr)
                    if _video_type == 1:
                        _identifier, _serious = self._get_qb_identifier(qb_identifier_arr, _video_name)
                        print(_video_name + " : " + _identifier)
                    else:
                        pass
                except Exception as e:
                    print(e)
                    pass
                video = VideoFileClip(_video_path)  # 打开视频
                video.close()  # 关闭视频
                video_width = str(video.size[0])
                video_height = str(video.size[1])
                resolution = video_width + ',' + video_height

                sql = "INSERT INTO video (resolution,series,identifier,type,video_name_local,video_path,img_type,hash) VALUES (?,?,?,?,?,?,?,?)"
                SqlUtils.update_video(sql,
                                      (resolution, _serious, _identifier, _video_type, _video_name, _video_path,
                                       image_type, _hash))
                self.statusbar.showMessage(_video_name + " : " + _identifier + " 已导入", 5000)
                print(_hash)
        self.statusbar.showMessage("导入完成", 5000)

    # 打开文件夹
    def _openfolder(self):
        try:
            directory = QFileDialog.getExistingDirectory(None, "选取文件夹",
                                                         CommonUtils.get_setting_ini_('DEFAULT', 'last_open_folder',
                                                                                      "./"))  # 起始路径
            if directory.strip() == "":
                return
            CommonUtils.update_setting_ini_('DEFAULT', 'last_open_folder', directory)
            self.process_folder(directory)
        except Exception as e:
            print(e)
            pass

    # 处理文件夹
    def process_folder(self, directory):
        video_list = []
        self._listdir(directory, video_list)
        self._process_video_list(video_list)

    # 打开文件
    def _openfiles(self):
        try:
            files, file_type = QFileDialog.getOpenFileNames(None, "多文件选择", CommonUtils.get_setting_ini_
            ('DEFAULT', 'last_open_folder', "./"), "All Files (*)")
            # files, file_type = QFileDialog.getOpenFileName(self, 'Open File', '',  "All Files (*)",options = QFileDialog.DontUseNativeDialog)
            if len(files) == 0:
                return
            CommonUtils.update_setting_ini_('DEFAULT', 'last_open_folder', files[0])
            # self._save_last_open_folder(files[0])
            self.process_files(files)
        except Exception as e:
            print(e)
            pass

    # 处理文件
    def process_files(self, files):
        video_list = []
        for file in files:
            if self.judge_file_is_movie(file):
                video_list.append(file)
        self._process_video_list(video_list)

    # 自动识别识别码
    def _get_qb_identifier(self, qb_identifier_arr, _video_name):
        _video_name_upper = _video_name.upper()
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
                    return (series_upper + "-" + num, series_upper)
            except Exception as e:
                print(e)
                pass
        print("无法识别：" + _video_name)
        return ("", "")

    # 判断电影类型
    def get_video_type(self, _video_name, qb_identifier_arr):
        _video_name_upper = _video_name.upper()
        for series in qb_identifier_arr:
            try:
                series_upper = series.upper()
                if series_upper in _video_name_upper:
                    return 1
            except Exception as e:
                print("无法识别：" + _video_name + "  " + e)
                pass
        return 0

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
