import sys
import netifaces as ni
import qrcode
from Server import Serve
from PyQt4 import QtCore,QtGui
from ui.serverForm import Ui_formServer
from netifaces import AF_INET,AF_INET6,AF_LINK,AF_PACKET,AF_BRIDGE


class ServerUI(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_formServer()
        self.ui.setupUi(self)
        interfacesList = ni.interfaces()
        self.ui.listInterfaces.addItems(interfacesList)
        self.ui.btnStart.clicked.connect(self.startServer)
        
    def startServer(self):
        selectedIface = str(self.ui.listInterfaces.currentText())
        ipAddress = ni.ifaddresses(selectedIface)[AF_INET][0]['addr']
        self.ui.lblStatus.setText(ipAddress)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    serverUI = ServerUI()
    serverUI.show()
    sys.exit(app.exec_())
    
