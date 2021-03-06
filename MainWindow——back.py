# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ScrollWindow import ScrollWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 589)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 223, 109))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.groupbox = QtWidgets.QGroupBox(self.widget)
        self.groupbox.setObjectName("groupbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_3.setMaximumSize(QtCore.QSize(42, 16777215))
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_2.setMaximumSize(QtCore.QSize(42, 16777215))
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton.setMaximumSize(QtCore.QSize(42, 16777215))
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.verticalLayout.addWidget(self.groupbox)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.scrollArea = ScrollWindow()

        # self.scrollArea = QtWidgets.QScrollArea(self.widget)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 69, 105))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setting = QtWidgets.QMenu(self.menubar)
        self.setting.setObjectName("setting")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openfile = QtWidgets.QAction(MainWindow)
        self.openfile.setObjectName("openfile")
        self.openfolder = QtWidgets.QAction(MainWindow)
        self.openfolder.setObjectName("openfolder")
        self.open_setting = QtWidgets.QAction(MainWindow)
        self.open_setting.setObjectName("open_setting")
        self.edit_tab = QtWidgets.QAction(MainWindow)
        self.edit_tab.setObjectName("edit_tab")
        self.downlowd_info = QtWidgets.QAction(MainWindow)
        self.downlowd_info.setObjectName("downlowd_info")
        self.downlowd_info_and_img = QtWidgets.QAction(MainWindow)
        self.downlowd_info_and_img.setObjectName("downlowd_info_and_img")
        self.downlowd_img = QtWidgets.QAction(MainWindow)
        self.downlowd_img.setObjectName("downlowd_img")
        self.menu.addAction(self.openfile)
        self.menu.addAction(self.openfolder)
        self.setting.addAction(self.open_setting)
        self.menu_2.addAction(self.edit_tab)
        self.menu_2.addAction(self.downlowd_info)
        self.menu_2.addAction(self.downlowd_img)
        self.menu_2.addAction(self.downlowd_info_and_img)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.setting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "类型"))
        self.radioButton_3.setText(_translate("MainWindow", "全部"))
        self.radioButton_2.setText(_translate("MainWindow", "无码"))
        self.radioButton.setText(_translate("MainWindow", "有码"))
        self.label.setText(_translate("MainWindow", "标签"))
        self.label_3.setText(_translate("MainWindow", "全部"))
        self.label_4.setText(_translate("MainWindow", "日产"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.setting.setTitle(_translate("MainWindow", "设置"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.openfile.setText(_translate("MainWindow", "打开文件"))
        self.openfolder.setText(_translate("MainWindow", "打开文件夹"))
        self.open_setting.setText(_translate("MainWindow", "打开设置"))
        self.edit_tab.setText(_translate("MainWindow", "编辑标签"))
        self.downlowd_info.setText(_translate("MainWindow", "下载信息"))
        self.downlowd_info_and_img.setText(_translate("MainWindow", "下载信息和图片"))
        self.downlowd_img.setText(_translate("MainWindow", "下载图片(需先下载信息)"))
