# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(725, 498)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Setting)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Setting)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.scrollArea = QtWidgets.QScrollArea(Setting)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -307, 460, 825))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(35, 20, 35, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_0 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_0.setObjectName("widget_0")
        self.formLayout = QtWidgets.QFormLayout(self.widget_0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel1 = QtWidgets.QLabel(self.widget_0)
        self.titleLabel1.setObjectName("titleLabel1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel1)
        self.RadioButton = QtWidgets.QRadioButton(self.widget_0)
        self.RadioButton.setObjectName("RadioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RadioButton)
        self.radioButton = QtWidgets.QRadioButton(self.widget_0)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_0)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.verticalLayout.addWidget(self.widget_0)
        self.widget_1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_1.setObjectName("widget_1")
        self.formLayout_8 = QtWidgets.QFormLayout(self.widget_1)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.titleLabel2 = QtWidgets.QLabel(self.widget_1)
        self.titleLabel2.setObjectName("titleLabel2")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel2)
        self.checkBox_26 = QtWidgets.QCheckBox(self.widget_1)
        self.checkBox_26.setObjectName("checkBox_26")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_26)
        self.checkBox_27 = QtWidgets.QCheckBox(self.widget_1)
        self.checkBox_27.setObjectName("checkBox_27")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_27)
        self.label_10 = QtWidgets.QLabel(self.widget_1)
        self.label_10.setObjectName("label_10")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.right1 = QtWidgets.QRadioButton(self.widget_1)
        self.right1.setObjectName("right1")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.right1)
        self.right2 = QtWidgets.QRadioButton(self.widget_1)
        self.right2.setChecked(True)
        self.right2.setObjectName("right2")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.right2)
        self.label_11 = QtWidgets.QLabel(self.widget_1)
        self.label_11.setObjectName("label_11")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.right3 = QtWidgets.QPushButton(self.widget_1)
        self.right3.setObjectName("right3")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.right3)
        self.verticalLayout.addWidget(self.widget_1)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName("widget_2")
        self.formLayout_9 = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.titleLabel3 = QtWidgets.QLabel(self.widget_2)
        self.titleLabel3.setObjectName("titleLabel3")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_9.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.checkBox_30 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_30.setObjectName("checkBox_30")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_30)
        self.right4 = QtWidgets.QLabel(self.widget_2)
        self.right4.setObjectName("right4")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.right4)
        self.checkBox_31 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_31.setObjectName("checkBox_31")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox_31)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout_9.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName("widget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.titleLabel6 = QtWidgets.QLabel(self.widget_3)
        self.titleLabel6.setObjectName("titleLabel6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel6)
        self.checkBox_20 = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_20.setObjectName("checkBox_20")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_20)
        self.checkBox_21 = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_21.setObjectName("checkBox_21")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_21)
        self.right5 = QtWidgets.QLabel(self.widget_3)
        self.right5.setObjectName("right5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.right5)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.radioButton1 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton1.setObjectName("radioButton1")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.radioButton1)
        self.radioButton_21 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_21.setObjectName("radioButton_21")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.radioButton_21)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.radioButton_3)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.listWidgetUser = QtWidgets.QListWidget(self.widget_3)
        self.listWidgetUser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetUser.setObjectName("listWidgetUser")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.listWidgetUser)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.formLayout_4.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.formLayout_5)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_6 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.titleLabel7 = QtWidgets.QLabel(self.widget_4)
        self.titleLabel7.setObjectName("titleLabel7")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel7)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName("widget_5")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_5)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.titleLabel8 = QtWidgets.QLabel(self.widget_5)
        self.titleLabel8.setEnabled(True)
        self.titleLabel8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel8.setObjectName("titleLabel8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.gifStartTime = QtWidgets.QLineEdit(self.widget_5)
        self.gifStartTime.setStatusTip("")
        self.gifStartTime.setInputMask("")
        self.gifStartTime.setText("")
        self.gifStartTime.setObjectName("gifStartTime")
        self.horizontalLayout_4.addWidget(self.gifStartTime)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.gifEndTime = QtWidgets.QLineEdit(self.widget_5)
        self.gifEndTime.setObjectName("gifEndTime")
        self.horizontalLayout_4.addWidget(self.gifEndTime)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gifInterval = QtWidgets.QLineEdit(self.widget_5)
        self.gifInterval.setObjectName("gifInterval")
        self.horizontalLayout_4.addWidget(self.gifInterval)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget_5)
        self.confirm = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.confirm.setMinimumSize(QtCore.QSize(100, 0))
        self.confirm.setObjectName("confirm")
        self.verticalLayout.addWidget(self.confirm, 0, QtCore.Qt.AlignRight)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Setting)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Setting)
        Setting.setTabOrder(self.listWidget, self.RadioButton)
        Setting.setTabOrder(self.RadioButton, self.radioButton)
        Setting.setTabOrder(self.radioButton, self.radioButton_2)
        Setting.setTabOrder(self.radioButton_2, self.checkBox_26)
        Setting.setTabOrder(self.checkBox_26, self.checkBox_27)
        Setting.setTabOrder(self.checkBox_27, self.right1)
        Setting.setTabOrder(self.right1, self.right2)
        Setting.setTabOrder(self.right2, self.right3)
        Setting.setTabOrder(self.right3, self.comboBox)
        Setting.setTabOrder(self.comboBox, self.checkBox_30)
        Setting.setTabOrder(self.checkBox_30, self.checkBox_31)
        Setting.setTabOrder(self.checkBox_31, self.pushButton_5)
        Setting.setTabOrder(self.pushButton_5, self.pushButton_4)
        Setting.setTabOrder(self.pushButton_4, self.checkBox_20)
        Setting.setTabOrder(self.checkBox_20, self.checkBox_21)
        Setting.setTabOrder(self.checkBox_21, self.radioButton)
        Setting.setTabOrder(self.radioButton, self.radioButton_2)
        Setting.setTabOrder(self.radioButton_2, self.radioButton_3)
        Setting.setTabOrder(self.radioButton_3, self.listWidgetUser)
        Setting.setTabOrder(self.listWidgetUser, self.pushButton)
        Setting.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "设置"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Setting", "默认封面类型"))
        item = self.listWidget.item(1)
        item.setText(_translate("Setting", "主面板"))
        item = self.listWidget.item(2)
        item.setText(_translate("Setting", "状态"))
        item = self.listWidget.item(3)
        item.setText(_translate("Setting", "提醒"))
        item = self.listWidget.item(4)
        item.setText(_translate("Setting", "热键"))
        item = self.listWidget.item(5)
        item.setText(_translate("Setting", "GIF生成设置"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.titleLabel1.setText(_translate("Setting", "默认封面类型："))
        self.RadioButton.setText(_translate("Setting", "小图"))
        self.radioButton.setText(_translate("Setting", "大图"))
        self.radioButton_2.setText(_translate("Setting", "自动生成GIF(初次导入会比较慢)"))
        self.titleLabel2.setText(_translate("Setting", "主面板："))
        self.checkBox_26.setText(_translate("Setting", "始终保持在其他窗口前端"))
        self.checkBox_27.setText(_translate("Setting", "停靠在桌面边缘时自动隐藏"))
        self.label_10.setText(_translate("Setting", "关闭主面板时："))
        self.right1.setText(_translate("Setting", "隐藏到任务栏通知区域，不退出程序"))
        self.right2.setText(_translate("Setting", "退出程序"))
        self.label_11.setText(_translate("Setting", "您可以自由定制适合您的面板和功能，使用QQ更有效率"))
        self.right3.setText(_translate("Setting", "界面管理器"))
        self.titleLabel3.setText(_translate("Setting", "状态："))
        self.label_13.setText(_translate("Setting", "登陆后状态为："))
        self.comboBox.setItemText(0, _translate("Setting", "我在线上"))
        self.comboBox.setItemText(1, _translate("Setting", "Q我吧"))
        self.comboBox.setItemText(2, _translate("Setting", "离开"))
        self.comboBox.setItemText(3, _translate("Setting", "忙碌"))
        self.comboBox.setItemText(4, _translate("Setting", "请勿打扰"))
        self.comboBox.setItemText(5, _translate("Setting", "隐身"))
        self.checkBox_30.setText(_translate("Setting", "运行全屏程序时切换至“忙碌“状态””"))
        self.right4.setText(_translate("Setting", "仅在“Q我吧”和“我在线上”状态下生效"))
        self.checkBox_31.setText(_translate("Setting", "离开、忙碌、请勿打扰时自动回复（100字以内）"))
        self.pushButton_5.setText(_translate("Setting", "自动回复设置"))
        self.pushButton_4.setText(_translate("Setting", "快捷回复设置"))
        self.titleLabel6.setText(_translate("Setting", "提醒："))
        self.checkBox_20.setText(_translate("Setting", "会话消息提醒"))
        self.checkBox_21.setText(_translate("Setting", "新邮件提醒"))
        self.right5.setText(_translate("Setting", "当插入安卓设备时，提示安装或者更新QQ手机版"))
        self.label_3.setText(_translate("Setting", "<html><head/><body><p>您可以设置是否在屏幕右下角收到来自QQ空间的通知，<a href=\"#\"><span style=\" text-decoration: none; color:#00aaff;\">进入设置</span></a>。</p></body></html>"))
        self.label_4.setText(_translate("Setting", "好友上线提醒"))
        self.radioButton1.setText(_translate("Setting", "关闭好友上线提醒"))
        self.radioButton_21.setText(_translate("Setting", "全部好友上线提醒"))
        self.radioButton_3.setText(_translate("Setting", "以下好友上线提醒"))
        self.pushButton.setText(_translate("Setting", "添加"))
        self.titleLabel7.setText(_translate("Setting", "热键："))
        self.label_6.setText(_translate("Setting", "您可以通过点击选择要更改的热键"))
        self.pushButton_2.setText(_translate("Setting", "设置热键"))
        self.titleLabel8.setText(_translate("Setting", "GIF生成设置："))
        self.label_2.setText(_translate("Setting", "起始"))
        self.label.setText(_translate("Setting", "结束"))
        self.label_5.setText(_translate("Setting", "间隔"))
        self.label_7.setText(_translate("Setting", "起始时间结束时间单位是秒，间隔单位是0.1秒"))
        self.confirm.setText(_translate("Setting", "确认"))
