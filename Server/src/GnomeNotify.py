from gi.repository import Notify

class GnomeNotify:
    @staticmethod
    def display_notification(title,message):
        Notify.init("Notify")
        notify_obj=Notify.Notification.new(title,message)
        notify_obj.show()
        

