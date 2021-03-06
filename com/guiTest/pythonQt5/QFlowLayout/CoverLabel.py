import os
from os import startfile

from PIL import Image
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QFont, QLinearGradient, QGradient, QColor, QBrush, QPixmap, QMovie
from utils import CommonUtils
from PyQt5.QtWidgets import QLabel, QAction, QMenu, QMessageBox

import Const
from SqlUtils import SqlUtils
from edit_video_custom_tab import edit_video_custom_tab
from edit_video_info import edit_video_info


class CoverLabel(QLabel):
    def __init__(self, cover_path, cover_title, video_path, video_hash, *args, **kwargs):
        super(CoverLabel, self).__init__(*args, **kwargs)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)  # 开放右键策略
        self.setCursor(Qt.PointingHandCursor)
        self.cover_path = cover_path
        # self.setScaledContents(True)
        # self.setMinimumSize(Const.GL_image_weight, Const.GL_image_height)
        # self.setMaximumSize(Const.GL_image_weight, Const.GL_image_height)
        self.video_hash = video_hash
        self.cover_title = cover_title
        self.video_path = video_path
        if not (os.path.exists(cover_path)):
            print("the img is not exist : "+cover_path)
            cover_path = "cache/coverimg/default.jpg"
        img = Image.open("cache/coverimg/default.jpg")
        try:
            img = Image.open(cover_path)
        except Exception as e:
            print("图片已损坏 : "+str(e))
            os.remove(cover_path)
            # 将下载状态置为1
            sql = "UPDATE video SET is_download = ? WHERE hash = ?"
            SqlUtils.update_video(sql, (1,video_hash))
            cover_path = "cache/coverimg/default.jpg"
        img_height = Const.GL_image_weight / img.size[0] * img.size[1]
        if cover_path.endswith('.gif'):
            movie = QMovie(cover_path)
            # movie.setScaledSize(self.size())
            movie.setScaledSize(QSize(Const.GL_image_weight, img_height))

            self.setMinimumSize(Const.GL_image_weight, img_height)
            self.setMaximumSize(Const.GL_image_weight, img_height)
            # self.parent().setMaximumSize(GL_widget_weight, img_height+100)
            # self.parent().setMaximumSize(GL_widget_weight, img_height+100)
            self.parent().setFixedWidth(Const.GL_widget_weight)
            self.setMovie(movie)
            movie.start()
        else:
            cover_img = QPixmap(cover_path)
            self.setPixmap(cover_img.scaled(Const.GL_image_weight, img_height))
            self.setMinimumSize(Const.GL_image_weight, img_height)
            self.setMaximumSize(Const.GL_image_weight, img_height)
            # self.parent().setMaximumSize(GL_widget_weight, img_height+100)
            # self.parent().setMaximumSize(GL_widget_weight, img_height+100)
            self.parent().setFixedWidth(Const.GL_widget_weight)
            # self.setPixmap(cover_img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def setCoverPath(self, path):
        self.cover_path = path

    '''重载一下鼠标按下事件(单击)'''

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
            # super(CoverLabel, self).mousePressEvent(event)
            if self.video_path is None:
                self.isRemoveMovieDialog("该影片路径为空，是否移出影片库？")
                print("video_path is None")
                return
            if not (os.path.exists(self.video_path)):
                self.isRemoveMovieDialog("该影片不存在或已删除，是否移出影片库？")
                print("video_path is not exist")
                return
            startfile(self.video_path)
            print("单击鼠标左键")  # 响应测试语句
        # elif event.buttons() == QtCore.Qt.RightButton:  # 右键按下
        #     print("单击鼠标右键")  # 响应测试语句
        elif event.buttons() == QtCore.Qt.MidButton:  # 中键按下
            print("单击鼠标中键")  # 响应测试语句

    def isRemoveMovieDialog(self, message):
        reply = QMessageBox.question(self, "提示框", message,
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            SqlUtils.delete_video(self.video_hash)
            if  os.path.exists(self.cover_path):
                os.remove(self.cover_path)
                print("Yes")


    def rightMenuShow(self, point):
        # 添加右键菜单
        self.popMenu = QMenu()

        download_pic_button = QAction(u'下载图片', self)
        download_info_button = QAction(u'下载信息', self)
        edit_info_button = QAction(u'编辑详情', self)
        edit_tab_button = QAction(u'编辑标签', self)
        open_pic_folder_button = QAction(u'打开图片所在位置', self)
        open_video_folder_button = QAction(u'打开视频所在位置', self)
        self.popMenu.addAction(download_pic_button)
        self.popMenu.addAction(download_info_button)
        self.popMenu.addAction(edit_info_button)
        self.popMenu.addAction(edit_tab_button)
        self.popMenu.addAction(open_pic_folder_button)
        self.popMenu.addAction(open_video_folder_button)
        # 绑定事件
        download_pic_button.triggered.connect(self.download_pic)
        download_info_button.triggered.connect(self.download_info)
        edit_info_button.triggered.connect(self.edit_info)
        edit_tab_button.triggered.connect(self.edit_tab)
        open_pic_folder_button.triggered.connect(self.open_pic_folder)
        open_video_folder_button.triggered.connect(self.open_video_folder)
        self.showContextMenu(QtGui.QCursor.pos())

    def open_pic_folder(self):
        print(self.cover_path)
        os.system(r"start explorer.exe /select, " + self.cover_path.replace("/", "\\"))
        # os.system(r"start " + self.cover_path[0:self.cover_path.rindex("/")].replace("/", "\\"))

    def open_video_folder(self):
        print(self.video_path)
        os.system(r"start explorer.exe /select, " + self.video_path.replace("/", "\\"))
        # os.system(r"start " + self.video_path[0:self.video_path.rindex("/")])

    def download_pic(self):
        try:
            video = SqlUtils._select_("SELECT identifier,img_url from video where hash = "  + '\''+  self.video_hash+'\'')
            is_success_download_img = CommonUtils.download_img(video[0][0], video[0][1])
            if is_success_download_img:
                sql = "UPDATE video SET is_download = ? WHERE hash = ?"
                SqlUtils.update_video(sql, (2, self.video_hash))
                # self.statusbar.showMessage("图片下载成功", 5000)
                print("2222")
        except Exception as e:
            print(e)

    def download_info(self):
        # todo
        print("待开发")

    def edit_info(self):
        self._edit_video_info = edit_video_info(self.video_hash,self.parentWidget())
        self._edit_video_info.show()
        print("edit_info" + str(self.video_hash))

    def edit_tab(self):
        self._edit_video_custom_tab = edit_video_custom_tab(self.video_hash,self.parentWidget())
        self._edit_video_custom_tab.show()
        print("edit_info" + str(self.video_hash))

    def showContextMenu(self, pos):
        # 调整位置
        # 右键点击时调用的函数
        # 菜单显示前，将它移动到鼠标点击的位置
        self.popMenu.move(pos)
        self.popMenu.show()

    def paintEvent(self, event):
        super(CoverLabel, self).paintEvent(event)
        if hasattr(self, "cover_title") and self.cover_title != "" and self.cover_title is not None:
            # 底部绘制文字
            painter = QPainter(self)
            rect = self.rect()
            # 粗略字体高度
            painter.save()
            fheight = self.fontMetrics().height()
            # 底部矩形框背景渐变颜色
            bottomRectColor = QLinearGradient(
                rect.width() / 2, rect.height() - 24 - fheight,
                rect.width() / 2, rect.height())
            bottomRectColor.setSpread(QGradient.PadSpread)
            bottomRectColor.setColorAt(0, QColor(255, 255, 255, 0))
            bottomRectColor.setColorAt(1, QColor(0, 0, 0, 255))
            # 画半透明渐变矩形框
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(bottomRectColor))
            painter.drawRect(rect.x(), rect.height() - 24 -
                             fheight, rect.width(), 24 + fheight)
            painter.restore()
            # 距离底部一定高度画文字
            font = self.font() or QFont()
            font.setPointSize(10)
            painter.setFont(font)
            painter.setPen(Qt.white)
            rect.setHeight(rect.height() - 4)  # 底部减去一定高度
            painter.drawText(rect, Qt.AlignBottom, self.cover_title)
