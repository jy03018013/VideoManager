import os
import sys
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QLinearGradient, QGradient, QColor, QBrush, QPixmap, QMovie

from PyQt5.QtWidgets import QLabel


class CoverLabel(QLabel):
    def __init__(self, cover_path, cover_title, video_url, *args, **kwargs):
        super(CoverLabel, self).__init__(*args, **kwargs)
        self.setCursor(Qt.PointingHandCursor)
        self.setScaledContents(True)
        self.setMinimumSize(220, 308)
        self.setMaximumSize(220, 308)
        self.cover_path = cover_path
        self.cover_title = cover_title
        self.video_url = video_url

        if cover_path.endswith('.gif'):
            movie = QMovie(cover_path)
            self.setMovie(movie)
            movie.start()
        else:
            self.setPixmap(QPixmap(cover_path))

    def setCoverPath(self, path):
        self.cover_path = path

    def mouseReleaseEvent(self, event):
        super(CoverLabel, self).mouseReleaseEvent(event)
        webbrowser.open_new_tab(self.video_url)

    def paintEvent(self, event):
        super(CoverLabel, self).paintEvent(event)
        if hasattr(self, "cover_title") and self.cover_title != "":
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
            bottomRectColor.setColorAt(0, QColor(255, 255, 255, 70))
            bottomRectColor.setColorAt(1, QColor(0, 0, 0, 50))
            # 画半透明渐变矩形框
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(bottomRectColor))
            painter.drawRect(rect.x(), rect.height() - 24 -
                             fheight, rect.width(), 24 + fheight)
            painter.restore()
            # 距离底部一定高度画文字
            font = self.font() or QFont()
            font.setPointSize(8)
            painter.setFont(font)
            painter.setPen(Qt.white)
            rect.setHeight(rect.height() - 12)  # 底部减去一定高度
            painter.drawText(rect, Qt.AlignHCenter |
                             Qt.AlignBottom, self.cover_title)
