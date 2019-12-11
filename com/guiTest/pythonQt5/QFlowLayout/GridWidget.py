import os
import sqlite3

from PyQt5.QtCore import QUrl, QTimer, pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWidgets import QWidget

import Const
from QFlowLayout.ItemWidget import ItemWidget
from QFlowLayout.FlowLayout import FlowLayout
from lxml.etree import HTML

from QFlowLayout.SqlUtils import SqlUtils

Url = "http://v.qq.com/x/list/movie?pay=-1&offset={0}"
# 主演
Actor = '''<a href="{href}" target="_blank" title="{title}" style="text-decoration: none;font-size: 12px;color: #999999;">{title}</a>&nbsp;'''


class GridWidget(QWidget):
    Page = 0
    loadStarted = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self._layout = FlowLayout(self)  # 使用自定义流式布局
        # 异步网络下载管理器
        # self._manager = QNetworkAccessManager(self)
        # self._manager.finished.connect(self.onFinished)

    def load(self):
        if self.Page == -1:
            return
        self.loadStarted.emit(True)
        # 延迟一秒后调用目的在于显示进度条
        # QTimer.singleShot(1000, self._load)
        QTimer.singleShot(1, self.loadFromSQL)

    def loadFromSQL(self):
        if self.Page == -1:
            return
        self.loadStarted.emit(True)
        # 延迟一秒后调用目的在于显示进度条
        QTimer.singleShot(1, self._loadFromSQL)

    def _loadFromSQL(self):
        video_list = SqlUtils.select_videos("SELECT * from video")
        for video in video_list:
            if video.img_type == Const.GL_gif_type:
                cover_path = "cache/covergif/"+video.video_name+".gif"
            else:
                cover_path = "cache/coverimg/IMG_20180729_110141.jpg"
            video_url = "www.baidu.com"
            cover_url = "http:"  # 封面图片
            path = "cache/{0}.jpg".format(
                os.path.splitext(os.path.basename(video_url))[0])
            if os.path.isfile(path):
                cover_path = path
            iwidget = ItemWidget(cover_path, video.tag, video.video_name,
                                 video.country, video.company, "11", video_url, cover_url, path, self)
            self._layout.addWidget(iwidget)
        self.loadStarted.emit(False)

    # print("id = ", row[0])
    # print("type = ", row[1])
    # print("video_name = ", row[2])
    # print("actor_name = ", row[3])
    # print("tag = ", row[4])
    # print("country = ", row[5])
    # print("company = ", row[6])
    # print("series = ", row[7])
    # print("hash = ", row[8], "\n")

    # def _load(self):
    #     print("load url:", Url.format(self.Page * 30))
    #     url = QUrl(Url.format(self.Page * 30))
    #     self._manager.get(QNetworkRequest(url))
    #
    # def onFinished(self, reply):
    #     # 请求完成后会调用该函数
    #     req = reply.request()  # 获取请求
    #     iwidget = req.attribute(QNetworkRequest.User + 1, None)
    #     path = req.attribute(QNetworkRequest.User + 2, None)
    #     html = reply.readAll().data()
    #     reply.deleteLater()
    #     del reply
    #     if iwidget and path and html:
    #         # 这里是图片下载完毕
    #         open(path, "wb").write(html)
    #         iwidget.setCover(path)
    #         return
    #     # 解析网页
    #     self._parseHtml(html)
    #     self.loadStarted.emit(False)
    #
    # def _parseHtml(self, html):
    #     #         encoding = chardet.detect(html) or {}
    #     #         html = html.decode(encoding.get("encoding","utf-8"))
    #     html = HTML(html)
    #     # 查找所有的li list_item
    #     lis = html.xpath("//li[@class='list_item']")
    #     if not lis:
    #         self.Page = -1  # 后面没有页面了
    #         return
    #     self.Page += 1
    #     self._makeItem(lis)
    #
    # def _makeItem(self, lis):
    #     for li in lis:
    #         a = li.find("a")
    #         video_url = a.get("href")  # 视频播放地址
    #         img = a.find("img")
    #         cover_url = "http:" + img.get("r-lazyload")  # 封面图片
    #         figure_title = img.get("alt")  # 电影名
    #         figure_info = a.find("div/span")
    #         figure_info = "" if figure_info is None else figure_info.text  # 影片信息
    #         figure_score = "".join(li.xpath(".//em/text()"))  # 评分
    #         # 主演
    #         figure_desc = "<span style=\"font-size: 12px;\">主演：</span>" + \
    #                       "".join([Actor.format(**dict(fd.items()))
    #                                for fd in li.xpath(".//div[@class='figure_desc']/a")])
    #         # 播放数
    #         figure_count = (
    #                 li.xpath(".//div[@class='figure_count']/span/text()") or [""])[0]
    #         path = "cache/{0}.jpg".format(
    #             os.path.splitext(os.path.basename(video_url))[0])
    #         cover_path = "Data/pic_v.png"
    #         if os.path.isfile(path):
    #             cover_path = path
    #         iwidget = ItemWidget(cover_path, figure_info, figure_title,
    #                              figure_score, figure_desc, figure_count, video_url, cover_url, path, self)
    #         self._layout.addWidget(iwidget)
