import sys

from PyQt5 import QtWidgets, sip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QCheckBox, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout

from utils import CommonUtils
from SqlUtils import SqlUtils
from video_custom_tab import Ui_Form


class edit_video_custom_tab(QWidget, Ui_Form):

    def __init__(self, video_hash,parentWidget):
        super(edit_video_custom_tab, self).__init__()
        self.video_hash = video_hash
        self.setupUi(self)
        self.parentWidget = parentWidget
        self.confirm_pushButton.clicked.connect(self._confirm_pushButton_on_click)
        custom_tag_str = str(CommonUtils.get_setting_ini_('DEFAULT', 'custom_tag', ""))
        video_tag_str = SqlUtils._select_("SELECT custom_tag from video where hash = "  + '\''+  video_hash+'\'')[0][0]
        if video_tag_str == None:
            video_tag_str = ''
        video_tag_list = video_tag_str.split(",")
        for tag in custom_tag_str.split(","):
            if tag.strip() == '':
                continue
            self.checkBox = QCheckBox(tag)
            self.checkBox.setChecked(False)
            if tag in video_tag_list:
                self.checkBox.setChecked(True)
            self.flowLayout.addWidget(self.checkBox)

    def _confirm_pushButton_on_click(self):
        tag_list = ""
        for item in self.flowLayout.itemList:
            if item.widget().isChecked():
                tag_list = tag_list + "," + item.widget().text()
        sql = "UPDATE video SET custom_tag = ? WHERE hash = ?"
        SqlUtils.update_video(sql, (tag_list, self.video_hash))

        # self.parentWidget.tag_out_layout.removeItem(self.parentWidget.tag_layout)
        # sip.delete(self.parentWidget.tag_layout)  # 删除控件的一个坑 https://my.oschina.net/yehun/blog/1813698
        # self.parentWidget.tag_layout = QHBoxLayout()

        # 删除所有子控件
        try:
            for i in range(self.parentWidget.tag_layout.count()):
                if self.parentWidget.tag_layout.itemAt(i).widget() != None:
                    self.parentWidget.tag_layout.itemAt(i).widget().deleteLater()
                else:
                    self.parentWidget.tag_layout.removeItem(self.parentWidget.tag_layout.itemAt(i))
                    print()
        except Exception as e:
            print(e)

        if (tag_list is not None) and (tag_list.strip() != ""):
            tag_array = tag_list.split(",")
            tag_text = QLabel("标签：")
            self.parentWidget.tag_layout.addWidget(tag_text)
            for tag in tag_array:
                if (tag is None) or (tag.strip() == ""):
                    continue
                tag_lab = QLabel(tag)
                tag_lab.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
                tag_lab.setWordWrap(True)
                tag_lab.setFont(QFont("Microsoft YaHei"))
                tag_lab.setStyleSheet("color:red");  # 文本颜色
                # tag_lab.setStyleSheet("background-color:red");  # 背景色
                self.parentWidget.tag_layout.addWidget(tag_lab)
            spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.parentWidget.tag_layout.addItem(spacerItem)
        self.parentWidget.tag_out_layout.addLayout(self.parentWidget.tag_layout)
        # if (tag_list is None) or (tag_list.strip() == ""):
        #     intro = ''
        #     self.parentWidget.intro_lab.setMaximumHeight(0)
        # else:
        #     intro = "简介：" + intro
        #     self.parentWidget.intro_lab.setMaximumHeight(1000)
        # self.parentWidget.intro_lab.setText(intro)

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = edit_video_custom_tab()
    form.show()
    sys.exit(app.exec_())
