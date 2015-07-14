import android.app.IntentService;
import android.content.Intent;
import android.os.IBinder;

public class NotificationMonitor extends IntentService {
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

    @Override
    public int onStartCommand(Intent intent,int flags, int startId) {
        CallReceiver callReceiver = new CallReceiver();
        IntentFilter filter = new IntentFilter(Intent.            
    }
}
