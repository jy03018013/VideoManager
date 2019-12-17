# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ScrollWindow import ScrollWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scrollArea = ScrollWindow()

        # self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 828, 522))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
