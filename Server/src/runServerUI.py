import sys
import netifaces as ni
from qrcode import *
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
        port = self.ui.txtPort.text()
        self.ui.lblStatus.setText(ipAddress)
        qr = QRCode(version=10,error_correction=ERROR_CORRECT_L,box_size=10)
        serverJson=self.getServerJson(ipAddress,port)
        qr.add_data(serverJson)
        qr.make()
        im=qr.make_image()
        im.save("qr.png")
        scene = QtGui.QGraphicsScene()
        view = self.ui.imgQrCode
        view.setScene(scene)
        pixmap = QtGui.QPixmap("qr.png")
        gfxPixItem = scene.addPixmap(pixmap)
        view.fitInView(gfxPixItem)
        view.show()
    def getServerJson(self,ipAddress,port):
        json = "{"
        json+="\"ipAddress\":\""
        json+=ipAddress
        json+="\","
        json+="\"port\":"
        json+=port
        json+="}"
        return json

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    serverUI = ServerUI()
    serverUI.show()
    sys.exit(app.exec_())
    
