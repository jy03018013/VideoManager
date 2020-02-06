import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox

from utils import CommonUtils
from SqlUtils import SqlUtils
from video_custom_tab import Ui_Form


class edit_video_custom_tab(QWidget, Ui_Form):

    def __init__(self, video_hash):
        super(edit_video_custom_tab, self).__init__()
        self.video_hash = video_hash
        self.setupUi(self)
        self.confirm_pushButton.clicked.connect(self._confirm_pushButton_on_click)
        custom_tag_str = str(CommonUtils.get_setting_ini_('DEFAULT', 'custom_tag', ""))
        video_tag_str = SqlUtils._select_("SELECT custom_tag from video where hash = "  + '\''+  video_hash+'\'')[0][0]
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
        # CommonUtils.update_setting_ini_('DEFAULT', 'custom_tag', tag_list)
        self.close()
        # self.flowLayout.itemList[0].widget().text()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = edit_video_custom_tab()
    form.show()
    sys.exit(app.exec_())
