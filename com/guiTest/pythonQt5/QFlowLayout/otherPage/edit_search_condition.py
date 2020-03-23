import sys

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QCheckBox, QLabel

import Const
from SqlUtils import SqlUtils
from search_condition import Ui_Form


class edit_search_condition(QWidget, Ui_Form):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self):
        super(edit_search_condition, self).__init__()
        self.setupUi(self)
        self.confirm_pushButton.clicked.connect(self._confirm_pushButton_on_click)
        # self.actor_clear_pushButton.clicked.connect(self.test)
        # self.cuntom_tag_clear_pushButton.clicked.connect(self.test)
        # self.series_clear_pushButton.clicked.connect(self.test)
        self.cancle_pushButton.clicked.connect(self.close)
        self.actor_lineEdit.textChanged.connect(self.actor_text_changed)
        self.custom_tag_lineEdit.textChanged.connect(self.custom_tag_text_changed)
        self.series_lineEdit.textChanged.connect(self.series_text_changed)

    def actor_text_changed(self):
        self.text_changed(self.actor_lineEdit.text(),self.actor_verticalLayout,self.actor_list)
    def custom_tag_text_changed(self):
        self.text_changed(self.custom_tag_lineEdit.text(),self.custom_tag_verticalLayout,self.custom_tag_list)
    def series_text_changed(self):
        self.text_changed(self.series_lineEdit.text(),self.series_verticalLayout,self.series_list)


    def text_changed(self, text,layout,origin_keyword_list):
        print(text)
        # 删除所有子控件的方法
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()
        if text == '':
            self.showTag(layout, origin_keyword_list)
        else:
            new_actor_list = []
            for keyword in origin_keyword_list:
                if text in keyword:
                    new_actor_list.append(keyword)
            self.showTag(layout, new_actor_list)

    def initDate(self, dict: dict):
        self.actor_list = dict.get("演员")
        self.series_list = dict.get("系列")
        self.custom_tag_list = dict.get("自定义标签")

        self.actor_verticalLayout = QtWidgets.QVBoxLayout(self.actor_scrollAreaWidgetContents)
        self.series_verticalLayout = QtWidgets.QVBoxLayout(self.series_scrollAreaWidgetContents)
        self.custom_tag_verticalLayout = QtWidgets.QVBoxLayout(self.custom_tag_scrollAreaWidgetContents)

        self.showTag(self.actor_verticalLayout, self.actor_list)
        self.showTag(self.series_verticalLayout, self.series_list)
        self.showTag(self.custom_tag_verticalLayout, self.custom_tag_list)

    def showTag(self, verticalLayout, tag_list):
        for tag in tag_list:
            if tag.strip() == '':
                continue
            self.checkBox = QCheckBox(tag)
            self.checkBox.setChecked(False)
            verticalLayout.addWidget(self.checkBox)
        print()

    def _confirm_pushButton_on_click(self):
        actor_list = []
        series_list = []
        custom_tag_list = []
        for item in self.actor_scrollAreaWidgetContents.children():
            if isinstance(item, PyQt5.QtWidgets.QCheckBox):
                if item.isChecked():
                    word = item.text()[0:item.text().index('(')]
                    actor_list.append("actor_name LIKE '%" + word + ",%'")
        for item in self.series_scrollAreaWidgetContents.children():
            if isinstance(item, PyQt5.QtWidgets.QCheckBox):
                if item.isChecked():
                    word = item.text()[0:item.text().index('(')]
                    series_list.append("series = '" + word + "'")
        for item in self.custom_tag_scrollAreaWidgetContents.children():
            if isinstance(item, PyQt5.QtWidgets.QCheckBox):
                if item.isChecked():
                    word = item.text()[0:item.text().index('(')]
                    custom_tag_list.append("custom_tag LIKE '%" + word + "%'")
        if len(actor_list) == 0 and len(series_list) == 0 and len(custom_tag_list) == 0:
            Const.Where = ''
        else:
            sql_where = " WHERE"
            sql_actor = self.getSqlWithOr(actor_list)
            sql_custom_tag = self.getSqlWithOr(custom_tag_list)
            sql_series = self.getSqlWithOr(series_list)
            if self.qie_actor_radioButton.isChecked():
                sql_actor = self.getSqlWithAnd(actor_list)
            if self.qie_tag_radioButton.isChecked():
                sql_custom_tag = self.getSqlWithAnd(custom_tag_list)
            if self.qie_series_radioButton.isChecked():
                sql_series = self.getSqlWithAnd(series_list)
            if sql_actor != '':
                sql_where = sql_where + sql_actor
            if sql_custom_tag != '':
                if sql_where == ' WHERE':
                    sql_where = sql_where + sql_custom_tag
                else:
                    sql_where = sql_where + " And " + sql_custom_tag
            if sql_series != '':
                if sql_where == ' WHERE':
                    sql_where = sql_where + sql_series
                else:
                    sql_where = sql_where + " And " + sql_series
            Const.Where = sql_where
        self.close()
        self.Signal_OneParameter.emit("已发送where 信号")

    def getSqlWithOr(self, tag_list: list):
        sql = ""
        if len(tag_list) == 0:
            return sql
        for tag in tag_list:
            sql = sql + ' ' + tag + ' or'
        sql = sql[0:sql.rfind('or')]
        return "(" + sql + ")"

    def getSqlWithAnd(self, tag_list: list):
        sql = ""
        if len(tag_list) == 0:
            return sql
        for tag in tag_list:
            sql = sql + ' ' + tag + ' and'
        sql = sql[0:sql.rfind('and')]
        return "(" + sql + ")"

    # CommonUtils.update_setting_ini_('DEFAULT', 'custom_tag', tag_list)
    # self.flowLayout.itemList[0].widget().text()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tag_to_list = dict()
    form = edit_search_condition("类型", ['有码', '无码'])
    form.show()
    sys.exit(app.exec_())
