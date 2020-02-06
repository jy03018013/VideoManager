import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QScrollArea, QAbstractSlider
from QFlowLayout.GridWidget import GridWidget
# from utils.AddMovieUtils import process_folder, process_files

Svg_icon_loading = '''<svg width="100%" height="100%" viewBox="0 0 38 38" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">
            <stop stop-color="#03a9f4" stop-opacity="0" offset="0%"/>
            <stop stop-color="#03a9f4" stop-opacity=".631" offset="63.146%"/>
            <stop stop-color="#03a9f4" offset="100%"/>
        </linearGradient>
    </defs>
    <g fill="none" fill-rule="evenodd">
        <g transform="translate(1 1)">
            <path d="M36 18c0-9.94-8.06-18-18-18" id="Oval-2" stroke="url(#a)" stroke-width="2">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </path>
            <circle fill="#03a9f4" cx="36" cy="18" r="4">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </circle>
        </g>
    </g>
</svg>'''.encode()


class ScrollWindow(QScrollArea):
    def __init__(self, *args, **kwargs):
        super(ScrollWindow, self).__init__(*args, **kwargs)
        # self.setAcceptDrops(True)  # 2
        self.resize(800, 600)
        self.setFrameShape(self.NoFrame)
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        self._loadStart = False
        # 网格窗口
        self._widget = GridWidget(self)
        self._widget.loadStarted.connect(self.setLoadStarted)
        self.setWidget(self._widget)
        ####################################################
        # 连接竖着的滚动条滚动事件
        # self.verticalScrollBar().actionTriggered.connect(self.onActionTriggered)
        ####################################################
        # 进度条
        self.loadWidget = QSvgWidget(
            self, minimumHeight=180, minimumWidth=180, visible=False)
        self.loadWidget.load(Svg_icon_loading)

    def setLoadStarted(self, started):
        self._loadStart = started
        self.loadWidget.setVisible(started)

    def onActionTriggered(self, action):
        # 这里要判断action=QAbstractSlider.SliderMove，可以避免窗口大小改变的问题
        # 同时防止多次加载同一个url
        if action != QAbstractSlider.SliderMove or self._loadStart:
            return
        # 使用sliderPosition获取值可以同时满足鼠标滑动和拖动判断
        if self.verticalScrollBar().sliderPosition() == self.verticalScrollBar().maximum():
            # 可以下一页了
            self._widget.load()

    def resizeEvent(self, event):
        super(ScrollWindow, self).resizeEvent(event)
        self.loadWidget.setGeometry(
            int((self.width() - self.loadWidget.minimumWidth()) / 2),
            int((self.height() - self.loadWidget.minimumHeight()) / 2),
            self.loadWidget.minimumWidth(),
            self.loadWidget.minimumHeight()
        )

    # def dragEnterEvent(self, QDragEnterEvent):
    #     if QDragEnterEvent.mimeData().hasText():
    #         QDragEnterEvent.acceptProposedAction()
    #
    # def dropEvent(self, QDropEvent):
    #     for path in QDropEvent.mimeData().text().split("\n"):
    #         path = path.replace("file:///","")
    #         if os.path.isdir(path):
    #             process_folder(path)
    #             print("isdir")
    #         elif os.path.isfile(path):
    #             process_files([path])
    #             print("isfile")


if __name__ == "__main__":
    os.makedirs("cache", exist_ok=True)
    app = QApplication(sys.argv)
    w = ScrollWindow()
    w.show()
    w._widget.load()
    sys.exit(app.exec_())
