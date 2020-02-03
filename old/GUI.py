# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dominik\Desktop\rec.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest

import os
print('Loading Tensorflow...')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # disable console info from tensorflow
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # don't use GPU

import Predict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(225, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 120, 51, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Light")
        font.setPointSize(36)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setEnabled(True)
        self.dial.setGeometry(QtCore.QRect(10, 210, 51, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.dial.setPalette(palette)
        self.dial.setStatusTip("")
        self.dial.setAccessibleDescription("")
        self.dial.setAutoFillBackground(False)
        self.dial.setMaximum(0)
        self.dial.setTracking(False)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(False)
        self.dial.setObjectName("dial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.rec)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "RECORD"))


    def change_red(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 36, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        self.dial.setPalette(palette)

    def change_grey(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        self.dial.setPalette(palette)

    def rec(self):
        self.change_red()
        QtTest.QTest.qWait(10)

        self.plainTextEdit.setPlainText('j')
        data = Predict.recording()
        letter = Predict.predicting(data, 'model.h5')
        self.plainTextEdit.setPlainText(letter)

        self.change_grey()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
