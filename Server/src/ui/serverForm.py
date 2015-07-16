# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Thu Jul 16 18:58:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_formServer(object):
    def setupUi(self, formServer):
        formServer.setObjectName(_fromUtf8("formServer"))
        formServer.resize(399, 306)
        self.gridLayoutWidget = QtGui.QWidget(formServer)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 391, 291))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.listInterfaces = QtGui.QComboBox(self.gridLayoutWidget)
        self.listInterfaces.setObjectName(_fromUtf8("listInterfaces"))
        self.horizontalLayout.addWidget(self.listInterfaces)
        self.btnStart = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout.addWidget(self.btnStart)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.qrCode = QtGui.QGraphicsView(self.gridLayoutWidget)
        self.qrCode.setObjectName(_fromUtf8("qrCode"))
        self.gridLayout.addWidget(self.qrCode, 1, 0, 1, 1)

        self.retranslateUi(formServer)
        QtCore.QMetaObject.connectSlotsByName(formServer)

    def retranslateUi(self, formServer):
        formServer.setWindowTitle(_translate("formServer", "Android Remote Manage", None))
        self.label.setText(_translate("formServer", "Interface:", None))
        self.btnStart.setText(_translate("formServer", "Start", None))

