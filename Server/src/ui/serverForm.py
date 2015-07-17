# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Fri Jul 17 23:16:27 2015
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
        self.btnStart = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.gridLayout.addWidget(self.btnStart, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.listInterfaces = QtGui.QComboBox(self.gridLayoutWidget)
        self.listInterfaces.setObjectName(_fromUtf8("listInterfaces"))
        self.horizontalLayout.addWidget(self.listInterfaces)
        self.lblPort = QtGui.QLabel(self.gridLayoutWidget)
        self.lblPort.setObjectName(_fromUtf8("lblPort"))
        self.horizontalLayout.addWidget(self.lblPort)
        self.txtPort = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPort.setObjectName(_fromUtf8("txtPort"))
        self.horizontalLayout.addWidget(self.txtPort)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.imgQrCode = QtGui.QGraphicsView(self.gridLayoutWidget)
        self.imgQrCode.setObjectName(_fromUtf8("imgQrCode"))
        self.gridLayout.addWidget(self.imgQrCode, 9, 0, 1, 1)
        self.lblStatus = QtGui.QLabel(self.gridLayoutWidget)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.gridLayout.addWidget(self.lblStatus, 7, 0, 1, 1)

        self.retranslateUi(formServer)
        QtCore.QMetaObject.connectSlotsByName(formServer)

    def retranslateUi(self, formServer):
        formServer.setWindowTitle(_translate("formServer", "Android Remote Manage", None))
        self.btnStart.setText(_translate("formServer", "Start", None))
        self.label.setText(_translate("formServer", "Interface:", None))
        self.lblPort.setText(_translate("formServer", "Port:", None))
        self.lblStatus.setText(_translate("formServer", "Idle", None))

