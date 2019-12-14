# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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
        self.menu.addAction(self.openfile)
        self.menu.addAction(self.openfolder)
        self.setting.addAction(self.open_setting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.setting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.setting.setTitle(_translate("MainWindow", "设置"))
        self.openfile.setText(_translate("MainWindow", "打开文件"))
        self.openfolder.setText(_translate("MainWindow", "打开文件夹"))
        self.open_setting.setText(_translate("MainWindow", "打开设置"))
