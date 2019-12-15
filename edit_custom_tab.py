# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_custom_tab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from FlowLayout import FlowLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(684, 476)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 664, 425))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.flowLayout = FlowLayout(self.scrollAreaWidgetContents)
        self.flowLayout.setObjectName("flowLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_pushButton = QtWidgets.QPushButton(Form)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout.addWidget(self.delete_pushButton)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.add_lab_lineEdit = QtWidgets.QLineEdit(Form)
        self.add_lab_lineEdit.setObjectName("add_lab_lineEdit")
        self.horizontalLayout.addWidget(self.add_lab_lineEdit)
        self.add_tab_pushButton = QtWidgets.QPushButton(Form)
        self.add_tab_pushButton.setObjectName("add_tab_pushButton")
        self.horizontalLayout.addWidget(self.add_tab_pushButton)
        self.confirm_pushButton = QtWidgets.QPushButton(Form)
        self.confirm_pushButton.setObjectName("confirm_pushButton")
        self.horizontalLayout.addWidget(self.confirm_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.delete_pushButton.setText(_translate("Form", "删除"))
        self.checkBox.setText(_translate("Form", "删除标签同时删除所有影片中该标签"))
        self.add_tab_pushButton.setText(_translate("Form", "添加"))
        self.confirm_pushButton.setText(_translate("Form", "确定"))
