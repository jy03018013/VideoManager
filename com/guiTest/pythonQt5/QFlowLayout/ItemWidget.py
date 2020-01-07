from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtGui import QPaintEvent, QPixmap
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, \
    QHBoxLayout, QSpacerItem, QSizePolicy, QGraphicsView

from Const import GL_widget_weight
from QFlowLayout.CoverLabel import CoverLabel

# 播放量图标
Svg_icon_play_sm = '''<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <path d="M10.83 8.31v.022l-4.08 2.539-.005.003-.048.03-.012-.005c-.073.051-.15.101-.246.101-.217 0-.376-.165-.413-.369l-.027-.011V5.461l.009-.005c0-.009-.009-.014-.009-.022 0-.24.197-.435.44-.435.096 0 .174.049.247.101l.031-.017 4.129 2.569v.016a.42.42 0 0 1 .153.317.418.418 0 0 1-.169.325zm3.493 2.604a.986.986 0 0 1-.948.742 1 1 0 0 1-1-1 .98.98 0 0 1 .094-.412l-.019-.01C12.79 9.559 13 8.807 13 8a5 5 0 1 0-5 5c.766 0 1.484-.186 2.133-.494l.013.03a.975.975 0 0 1 .417-.097 1 1 0 0 1 1 1 .987.987 0 0 1-.77.954A6.936 6.936 0 0 1 8 14.999a7 7 0 1 1 7-7c0 1.048-.261 2.024-.677 2.915z" fill="#999999"></path>
</svg>
'''.encode()


class ItemWidget(QWidget):

    def __init__(self, cover_path, video_tag, video_name,
                 country, actor_name, like_stars, video_path, cover_url, img_url, video_hash, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        # self.setMaximumSize(GL_widget_weight, 420)
        # self.setMaximumSize(GL_widget_weight, 420)
        self.setFixedWidth(GL_widget_weight)
        self.img_url = img_url
        self.cover_url = cover_url
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 0)
        # 图片label
        self.clabel = CoverLabel(cover_path, video_tag, video_path, video_hash, self)
        layout.addWidget(self.clabel)

        # 片名和国家
        flayout = QHBoxLayout()
        flayout.addWidget(QLabel(video_name, self))
        flayout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        flayout.addWidget(QLabel(country, self, styleSheet="color: red;"))
        layout.addLayout(flayout)

        # 演员
        if not (actor_name is None):
            if not actor_name.strip() == "":
                layout.addWidget(
                    QLabel(actor_name, self, styleSheet="color: #999999;", openExternalLinks=True))

        # 喜爱程度
        blayout = QHBoxLayout()
        lable = QLabel(self)
        # lable.setAutoFillBackground(True)
        lable.setScaledContents(True)
        lable.setMaximumSize(14, 14)
        pixmap = QPixmap('source/stars.png')
        lable.setPixmap(pixmap)
        blayout.addWidget(lable)
        # count_icon = QSvgWidget(self)
        # count_icon.setMaximumSize(16, 16)
        # count_icon.load(Svg_icon_play_sm)
        # blayout.addWidget(count_icon)
        blayout.addWidget(
            QLabel(str(like_stars), self, styleSheet="color: #999999;"))
        layout.addLayout(blayout)

    def setCover(self, path):
        self.clabel.setCoverPath(path)
        self.clabel.setPixmap(QPixmap(path))

    # def sizeHint(self):
    #     # 每个item控件的大小
    #     return QSize(GL_widget_weight, 420)

    def event(self, event):
        if isinstance(event, QPaintEvent):
            if event.rect().height() > 20 and hasattr(self, "clabel"):
                if self.clabel.cover_path.find("pic_v.png") > -1:  # 封面未加载
                    #                     print("start download img:", self.cover_url)
                    req = QNetworkRequest(QUrl(self.cover_url))
                    # 设置两个自定义属性方便后期reply中处理
                    req.setAttribute(QNetworkRequest.User + 1, self)
                    req.setAttribute(QNetworkRequest.User + 2, self.img_url)
                    self.parentWidget()._manager.get(req)  # 调用父窗口中的下载器下载
        return super(ItemWidget, self).event(event)
