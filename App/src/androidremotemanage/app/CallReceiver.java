package androidremotemanage.app;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.telephony.TelephonyManager;
import android.provider.ContactsContract;
import android.net.Uri;
import android.database.Cursor;

public class CallReceiver extends BroadcastReceiver {
    Notification notification;
    
    public CallReceiver(String ipAddress,String port) {
        
        notification = new Notification(ipAddress,Integer.parseInt(port));
    }

    public String getCallerName(Context ctx,String phoneNumber) {
        String callerName;
        
        callerName = "";
        String [] projection = new String[] {
            ContactsContract.PhoneLookup.DISPLAY_NAME,
            ContactsContract.PhoneLookup.NUMBER,
            ContactsContract.PhoneLookup.HAS_PHONE_NUMBER
        };
        Uri contactUri = Uri.withAppendedPath(
                                              ContactsContract.PhoneLookup.CONTENT_FILTER_URI,
                                              Uri.encode(phoneNumber));
        Cursor cursor = ctx.getContentResolver().
            query(contactUri,projection,null,null,null);
        if(cursor.moveToFirst()) {
            callerName = cursor.getString(cursor
                                          .getColumnIndex(ContactsContract.PhoneLookup.DISPLAY_NAME));
        }
        cursor.close();
        if(callerName.equals("")) {
            callerName = phoneNumber;
        }
        return callerName;
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
                caller = getCallerName(ctx,incomingNumber);
                notification.sendNotification(NotificationType.Call,caller,message);
            }
        }
        catch (Exception e){
            System.out.println("Phone receive Error" + e);
        }
    }
}
