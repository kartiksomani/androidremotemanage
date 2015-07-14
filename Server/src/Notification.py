from GnomeNotify import GnomeNotify
class Notification:
    incoming_message=""
    display_message=""
    title=""
    def create_display_message(self):
        display_message = incoming_message
        message_title = "Notification"
        notify();
    def notify(self):
        #Send for notification here
        self.create_display_message()
        GnomeNotify.display_notification(self.title,self.display_message)
    def __init__(self,incoming_message):
        self.incoming_message = incoming_message
        
        
            
        
