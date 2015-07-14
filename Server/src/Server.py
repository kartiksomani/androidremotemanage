import socket
import json
from twisted.internet import reactor, protocol
from CallNotification import CallNotification
class Serve(protocol.Protocol):
    def dataReceived(self,data):
        #perform operation
        decoder = json.JSONDecoder()
        conf = decoder.decode(data)
        create_notification_obj(conf)
        
def create_notification_obj(data):
    if data['type'] == 'Call' :
        notification = CallNotification(data['source'],data['message'])
    else:
        print "Unknown Type"

def main():
    port = 1234
    factory = protocol.ServerFactory()
    factory.protocol = Serve
    reactor.listenTCP(port,factory)
    reactor.run()

if __name__ == '__main__':
    main()
