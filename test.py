# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calx.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startSessionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startSessionBtn.setGeometry(QtCore.QRect(180, 200, 131, 31))
        self.startSessionBtn.setObjectName("startSessionBtn")
        self.historiqueBtn = QtWidgets.QPushButton(self.centralwidget)
        self.historiqueBtn.setGeometry(QtCore.QRect(320, 200, 131, 31))
        self.historiqueBtn.setObjectName("historiqueBtn")
        self.sessionWidget = QtWidgets.QWidget(self.centralwidget)
        self.sessionWidget.setEnabled(True)
        self.sessionWidget.setGeometry(QtCore.QRect(180, -20, 211, 211))
        self.sessionWidget.setObjectName("sessionWidget")
        self.secondOperandLbl = QtWidgets.QLabel(self.sessionWidget)
        self.secondOperandLbl.setGeometry(QtCore.QRect(110, 60, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.secondOperandLbl.setFont(font)
        self.secondOperandLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.secondOperandLbl.setScaledContents(False)
        self.secondOperandLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.secondOperandLbl.setObjectName("secondOperandLbl")
        self.firstOperandeLbl = QtWidgets.QLabel(self.sessionWidget)
        self.firstOperandeLbl.setGeometry(QtCore.QRect(110, 20, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.firstOperandeLbl.setFont(font)
        self.firstOperandeLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firstOperandeLbl.setScaledContents(False)
        self.firstOperandeLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.firstOperandeLbl.setObjectName("firstOperandeLbl")
        self.operationLbl = QtWidgets.QLabel(self.sessionWidget)
        self.operationLbl.setGeometry(QtCore.QRect(80, 60, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.operationLbl.setFont(font)
        self.operationLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.operationLbl.setScaledContents(False)
        self.operationLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.operationLbl.setObjectName("operationLbl")
        self.line = QtWidgets.QFrame(self.sessionWidget)
        self.line.setGeometry(QtCore.QRect(80, 120, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.resultEdit = QtWidgets.QLineEdit(self.sessionWidget)
        self.resultEdit.setGeometry(QtCore.QRect(80, 130, 113, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.resultEdit.setFont(font)
        self.resultEdit.setAutoFillBackground(False)
        self.resultEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultEdit.setObjectName("resultEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calx"))
        self.startSessionBtn.setText(_translate("MainWindow", "Commencer une session"))
        self.historiqueBtn.setText(_translate("MainWindow", "Voir l\'historique"))
        self.secondOperandLbl.setText(_translate("MainWindow", "22"))
        self.firstOperandeLbl.setText(_translate("MainWindow", "22"))
        self.operationLbl.setText(_translate("MainWindow", "+"))
        self.resultEdit.setText(_translate("MainWindow", "44"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
