# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sogou.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmbox = QtWidgets.QComboBox(self.centralwidget)
        self.cmbox.setGeometry(QtCore.QRect(20, 30, 291, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.cmbox.setFont(font)
        self.cmbox.setObjectName("cmbox")
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(330, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.bt1.setFont(font)
        self.bt1.setObjectName("bt1")
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(420, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.bt2.setFont(font)
        self.bt2.setObjectName("bt2")
        self.txt = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt.setGeometry(QtCore.QRect(660, 10, 661, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.txt.setFont(font)
        self.txt.setObjectName("txt")
        self.time = QtWidgets.QSpinBox(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(510, 40, 42, 22))
        self.time.setMinimum(1)
        self.time.setObjectName("time")
        self.web1 = QtWebKitWidgets.QWebView(self.centralwidget)
        self.web1.setGeometry(QtCore.QRect(10, 100, 1311, 751))
        self.web1.setUrl(QtCore.QUrl("about:blank"))
        self.web1.setObjectName("web1")
        self.bt3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3.setGeometry(QtCore.QRect(560, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.bt3.setFont(font)
        self.bt3.setObjectName("bt3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "答题助手-搜狗"))
        self.bt1.setText(_translate("MainWindow", "开始"))
        self.bt2.setText(_translate("MainWindow", "结束"))
        self.bt3.setText(_translate("MainWindow", "测试 "))

from PyQt5 import QtWebKitWidgets
