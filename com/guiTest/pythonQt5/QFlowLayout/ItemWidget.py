from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, \
    QHBoxLayout, QSpacerItem, QSizePolicy

import My
from Const import GL_widget_weight
from CustomQComboBox import QComboBox
from QFlowLayout.CoverLabel import CoverLabel
# 播放量图标
from SqlUtils import SqlUtils

Svg_icon_play_sm = '''<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <path d="M10.83 8.31v.022l-4.08 2.539-.005.003-.048.03-.012-.005c-.073.051-.15.101-.246.101-.217 0-.376-.165-.413-.369l-.027-.011V5.461l.009-.005c0-.009-.009-.014-.009-.022 0-.24.197-.435.44-.435.096 0 .174.049.247.101l.031-.017 4.129 2.569v.016a.42.42 0 0 1 .153.317.418.418 0 0 1-.169.325zm3.493 2.604a.986.986 0 0 1-.948.742 1 1 0 0 1-1-1 .98.98 0 0 1 .094-.412l-.019-.01C12.79 9.559 13 8.807 13 8a5 5 0 1 0-5 5c.766 0 1.484-.186 2.133-.494l.013.03a.975.975 0 0 1 .417-.097 1 1 0 0 1 1 1 .987.987 0 0 1-.77.954A6.936 6.936 0 0 1 8 14.999a7 7 0 1 1 7-7c0 1.048-.261 2.024-.677 2.915z" fill="#999999"></path>
</svg>
'''.encode()


class ItemWidget(QWidget):

    def __init__(self, cover_path, video_tag, video_name,
                 country, actor_name, like_stars, video_path, video_hash, title, intro, *args,
                 **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        # self.setMaximumSize(GL_widget_weight, 420)
        self.video_hash = video_hash
        self.setFixedWidth(GL_widget_weight)
        layout = QVBoxLayout(self)
        # layout.addSpacing(10)
        layout.setContentsMargins(10, 20, 10, 0)
        # 图片label
        self.clabel = CoverLabel(cover_path, video_tag, video_path, video_hash, self)
        layout.addWidget(self.clabel)

        # 片名和分辨率
        flayout = QHBoxLayout()
        video_name_tag = QLabel(video_name, self)
        video_name_tag.setToolTip(video_name)
        video_name_tag.setFont(QFont("Roman times", 10, QFont.Bold))
        video_name_tag.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        flayout.addWidget(video_name_tag)

        flayout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        flayout.addWidget(QLabel(country, self, styleSheet="color: red;"))
        flayout.setContentsMargins(0, 10, 0, 0)#标题会和图片重叠，暂时的解决办法
        layout.addLayout(flayout)

        # 影片发行标题
        if not (title is None):
            if not title.strip() == "":
                text = QLabel(title, self, styleSheet="color: #999999;")
                # text.setWordWrap(True)
                # text.setMaximumHeight(24)
                text.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
                text.setAlignment(Qt.AlignTop)
                text.setToolTip(title)
                font = QFont()
                font.setPointSize(8)
                text.setFont(font)
                layout.addWidget(text)

        # 喜爱程度
        blayout = QHBoxLayout()
        lable = My.myLabel(self)
        # lable.setAutoFillBackground(True)
        lable.setScaledContents(True)
        lable.setMaximumSize(14, 14)
        pixmap = QPixmap('source/stars.png')
        lable.setPixmap(pixmap)
        blayout.addWidget(lable)

        like_star_combobox = QComboBox(self)
        like_star_combobox.setMaximumSize(30, 18)
        like_star_combobox.addItems(['0','1', '2', '3', '4', '5', '6', '7', '8', '9'])
        like_star_combobox.setCurrentText(str(like_stars))
        like_star_combobox.currentTextChanged.connect(self.like_star_combobox_changed)
        blayout.addWidget(like_star_combobox)
        # 演员
        actor = My.myLabel(str(actor_name), self, styleSheet="color: #660000;")
        actor.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        actor.setToolTip(actor_name)
        blayout.addWidget(actor)
        layout.addLayout(blayout)
        # lable.clicked.connect(self.blayout_clicked)

        # 简介
        # if not (intro is None):
        #     if not intro.strip() == "":
        #         self.intro_lab = QLabel("简介："+intro)
        #         self.intro_lab.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #         # intro_lab.setMaximumHeight(26)
        #         self.intro_lab.setWordWrap(True)
        #         self.intro_lab.setToolTip(intro)
        #         layout.addWidget(self.intro_lab)
        if (intro is None) or (intro.strip() == ""):
            intro = ''
        else:
            intro = "简介：" + intro
        self.intro_lab = QLabel(intro)
        if (intro is None) or (intro.strip() == ""):
            self.intro_lab.setMaximumHeight(0)
        self.intro_lab.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        self.intro_lab.setWordWrap(True)
        self.intro_lab.setToolTip(intro)
        layout.addWidget(self.intro_lab)
        # 标签
        self.tag_out_layout = QHBoxLayout()
        self.tag_layout = QHBoxLayout()
        if (video_tag is not None) and (video_tag.strip() != ""):
            tag_list = video_tag.split(",")
            tag_text = QLabel("标签：")
            self.tag_layout.addWidget(tag_text)
            for tag in tag_list:
                if (tag is None) or (tag.strip() == ""):
                    continue
                tag_lab = QLabel(tag)
                tag_lab.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
                tag_lab.setWordWrap(True)
                tag_lab.setFont(QFont("Microsoft YaHei"))
                tag_lab.setStyleSheet("color:red");  # 文本颜色
                # tag_lab.setStyleSheet("background-color:red");  # 背景色
                self.tag_layout.addWidget(tag_lab)
            spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.tag_layout.addItem(spacerItem)
        self.tag_out_layout.addLayout(self.tag_layout)
        layout.addLayout(self.tag_out_layout)

    def like_star_combobox_changed(self, currentStars):
        sql = "UPDATE video SET like_stars = ? WHERE hash = ?"
        SqlUtils.update_video(sql, (currentStars, self.video_hash))
        print(currentStars)  # 响应测试语句

    def setCover(self, path):
        self.clabel.setCoverPath(path)
        self.clabel.setPixmap(QPixmap(path))

    # def sizeHint(self):
    #     # 每个item控件的大小
    #     return QSize(GL_widget_weight, 420)

    # def event(self, event):
    #     if isinstance(event, QPaintEvent):
    #         if event.rect().height() > 20 and hasattr(self, "clabel"):
    #             if self.clabel.cover_path.find("pic_v.png") > -1:  # 封面未加载
    #                 #                     print("start download img:", self.cover_url)
    #                 req = QNetworkRequest(QUrl(self.cover_url))
    #                 # 设置两个自定义属性方便后期reply中处理
    #                 req.setAttribute(QNetworkRequest.User + 1, self)
    #                 req.setAttribute(QNetworkRequest.User + 2, self.img_url)
    #                 self.parentWidget()._manager.get(req)  # 调用父窗口中的下载器下载
    #     return super(ItemWidget, self).event(event)
