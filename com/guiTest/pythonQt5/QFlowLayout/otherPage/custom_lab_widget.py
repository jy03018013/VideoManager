import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox

from edit_custom_tab import Ui_Form


class custom_lab_widget(QWidget, Ui_Form):

    def __init__(self):
        super(custom_lab_widget, self).__init__()
        self.setupUi(self)
        self.add_tab_pushButton.clicked.connect(self._add_lab_on_click)

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
