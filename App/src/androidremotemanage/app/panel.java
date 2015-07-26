package androidremotemanage.app;
import android.widget.Toast;
import android.app.Activity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.view.View;
import android.view.View.OnClickListener;
import android.content.IntentFilter;
import android.content.Intent;
import com.google.gson.Gson;
public class panel extends Activity
{
    private CallReceiver callReceiver;
    EditText txtIP,txtPort;
    IntentFilter intentFilter;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        Button btnStart;


        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        //TODO check if the NotificationMonitor service is running or not
        //and accordingly set the status and activate the button to start service
        //Start barcode scanner
        Intent intent = new Intent("com.google.zxing.client.android.SCAN");
        intent.putExtra("SCAN_MODE","QR_CODE_MODE");
        startActivityForResult(intent,0);

        btnStart = (Button)findViewById(R.id.start_server_button);
        txtIP = (EditText)findViewById(R.id.server_ip_address);
        txtPort = (EditText)findViewById(R.id.server_port);

        intentFilter = new IntentFilter("android.intent.action.PHONE_STATE");
        btnStart.setOnClickListener(new View.OnClickListener() {
                public void onClick(View view) {
                    //register receiver to listen to events
                    //TODO Change status on the UI to indicate service is started
                    String port;
                    String ipAddress;
                    ipAddress = txtIP.getText().toString();
                    port = txtPort.getText().toString();
        callReceiver = new CallReceiver(ipAddress,port);
                    registerReceiver(callReceiver,intentFilter);
                }
            });
    }

    @Override
    protected void onDestroy() {
        unregisterReceiver(callReceiver);
        super.onDestroy();
    }

    public void onActivityResult(int requestCode,int resultCode,Intent intent) {
        Gson gson;
        ServerDetails serverDetails;
          if (requestCode == 0) {
            if(resultCode == Activity.RESULT_OK) {
                String json = intent.getStringExtra("SCAN_RESULT");
                gson = new Gson();
                serverDetails = gson.fromJson(json,ServerDetails.class);
                txtIP.setText(serverDetails.getIpAddress());
                txtPort.setText(serverDetails.getPort());
            }
            else if(resultCode == Activity.RESULT_CANCELED) {
                //handle cancel
            }
        }
        else {
            //handle other intents
            }
        
    }
}
