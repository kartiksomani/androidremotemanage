package androidremotemanage.app;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.telephony.TelephonyManager;

public class CallReceiver extends BroadcastReceiver {
    Notification notification;
    
    public CallReceiver(String ipAddress,String port) {
        
        notification = new Notification(ipAddress,Integer.parseInt(port));
    }

    @Override
    public void onReceive(Context ctx,Intent intent) {
        String caller;
        String message;
        String incomingNumber;
        //Code to send the notification message over the wifi network
        incomingNumber = "";
        message = "";
        try{
            String state = intent.getStringExtra(TelephonyManager.EXTRA_STATE);   
            if (TelephonyManager.EXTRA_STATE_RINGING.equals(state)) {
                incomingNumber =
                    intent.getStringExtra(TelephonyManager.EXTRA_INCOMING_NUMBER);
                caller = incomingNumber;
                notification.sendNotification(NotificationType.Call,caller,message);
            }
        }
        catch (Exception e){
            System.out.println("Phone receive Error" + e);
        }
    }
}
