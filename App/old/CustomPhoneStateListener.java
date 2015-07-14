package androidremotemanager.app;

private class CustomPhoneStateListener extends PhoneStateListener {
    
        public void onCallStateChanged(int state,String incomingNumber) {
            String notificationJson;
            if (state == 1) {
                notificationJson = Notification.getJson();
                NotificationSender.sendNotification(notificationJson);
            }
        }
        
    }
