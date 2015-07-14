from Notification import Notification
class CallNotification(Notification):
    caller=""
    def __init__(self,caller,incoming_message):
        Notification.__init__(self,incoming_message)
        self.caller = caller
        self.notify()
    def create_display_message(self):
        self.title="New Call"
        self.display_message="Incoming Call from " + self.caller

    
