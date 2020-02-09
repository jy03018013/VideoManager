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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refresh_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout.addWidget(self.search_pushButton)
        self.manage_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.manage_pushButton.setObjectName("manage_pushButton")
        self.horizontalLayout.addWidget(self.manage_pushButton)
        self.order_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.order_pushButton.setObjectName("order_pushButton")
        self.horizontalLayout.addWidget(self.order_pushButton)
        self.view_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.view_pushButton.setObjectName("view_pushButton")
        self.horizontalLayout.addWidget(self.view_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scrollArea = ScrollWindow()

        # self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 911, 480))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
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
        self.open_file_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_action.setIcon(icon)
        self.open_file_action.setObjectName("open_file_action")
        self.open_folder_action = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_folder_action.setIcon(icon1)
        self.open_folder_action.setObjectName("open_folder_action")
        self.edit_tab_action = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_tab_action.setIcon(icon2)
        self.edit_tab_action.setObjectName("edit_tab_action")
        self.downlowd_infoaction_action = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/download_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downlowd_infoaction_action.setIcon(icon3)
        self.downlowd_infoaction_action.setObjectName("downlowd_infoaction_action")
        self.downlowd_img_action = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/download_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downlowd_img_action.setIcon(icon4)
        self.downlowd_img_action.setObjectName("downlowd_img_action")
        self.open_setting_action = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_setting_action.setIcon(icon5)
        self.open_setting_action.setObjectName("open_setting_action")
        self.toolBar.addAction(self.open_file_action)
        self.toolBar.addAction(self.open_folder_action)
        self.toolBar.addAction(self.edit_tab_action)
        self.toolBar.addAction(self.downlowd_infoaction_action)
        self.toolBar.addAction(self.downlowd_img_action)
        self.toolBar.addAction(self.open_setting_action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh_pushButton.setText(_translate("MainWindow", "刷新"))
        self.search_pushButton.setText(_translate("MainWindow", "检索"))
        self.manage_pushButton.setText(_translate("MainWindow", "管理"))
        self.order_pushButton.setText(_translate("MainWindow", "排序"))
        self.view_pushButton.setText(_translate("MainWindow", "视图"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.openfile.setText(_translate("MainWindow", "打开文件"))
        self.openfolder.setText(_translate("MainWindow", "打开文件夹"))
        self.open_setting.setText(_translate("MainWindow", "打开设置"))
        self.edit_tab.setText(_translate("MainWindow", "编辑标签"))
        self.downlowd_info.setText(_translate("MainWindow", "下载信息"))
        self.downlowd_info_and_img.setText(_translate("MainWindow", "下载信息和图片"))
        self.downlowd_img.setText(_translate("MainWindow", "下载图片(需先下载信息)"))
        self.open_file_action.setText(_translate("MainWindow", "打开文件"))
        self.open_file_action.setToolTip(_translate("MainWindow", "打开文件"))
        self.open_folder_action.setText(_translate("MainWindow", "打开文件夹"))
        self.open_folder_action.setToolTip(_translate("MainWindow", "打开文件夹"))
        self.edit_tab_action.setText(_translate("MainWindow", "编辑标签"))
        self.edit_tab_action.setToolTip(_translate("MainWindow", "编辑标签"))
        self.downlowd_infoaction_action.setText(_translate("MainWindow", "下载信息"))
        self.downlowd_infoaction_action.setToolTip(_translate("MainWindow", "下载信息"))
        self.downlowd_img_action.setText(_translate("MainWindow", "下载图片(需先下载信息)"))
        self.downlowd_img_action.setToolTip(_translate("MainWindow", "下载图片(需先下载信息)"))
        self.open_setting_action.setText(_translate("MainWindow", "打开设置"))
        self.open_setting_action.setToolTip(_translate("MainWindow", "打开设置"))


import resource_rc
