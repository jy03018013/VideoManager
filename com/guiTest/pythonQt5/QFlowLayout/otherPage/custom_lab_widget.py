import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox

from utils import CommonUtils
from edit_custom_tab import Ui_Form


class custom_lab_widget(QWidget, Ui_Form):

    def __init__(self):
        super(custom_lab_widget, self).__init__()
        self.setupUi(self)
        self.add_tab_pushButton.clicked.connect(self._add_lab_on_click)
        self.confirm_pushButton.clicked.connect(self._confirm_pushButton_on_click)
        custom_tag_str = str(CommonUtils.get_setting_ini_('DEFAULT', 'custom_tag', ""))
        for tag in custom_tag_str.split(","):
            if tag.strip() == '':
                continue
            self.checkBox = QCheckBox(tag)
            self.checkBox.setChecked(False)
            self.flowLayout.addWidget(self.checkBox)


    def _confirm_pushButton_on_click(self):
        tag_list = ""
        for item in self.flowLayout.itemList:
            tag_list = tag_list + "," + item.widget().text()
        CommonUtils.update_setting_ini_('DEFAULT', 'custom_tag', tag_list)
        self.close()
        # self.flowLayout.itemList[0].widget().text()

    def _add_lab_on_click(self):
        if self.add_lab_lineEdit.text() is None:
            return
        if self.add_lab_lineEdit.text().strip() == "":
            return
        self.checkBox1 = QCheckBox(self.add_lab_lineEdit.text())
        self.checkBox1.setChecked(False)
        self.flowLayout.addWidget(self.checkBox1)
        print(self.add_lab_lineEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = custom_lab_widget()
    form.show()
    sys.exit(app.exec_())
