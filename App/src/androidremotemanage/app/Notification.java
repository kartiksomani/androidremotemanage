package androidremotemanage.app;

import java.io.DataOutputStream;
import java.net.Socket;

public class Notification {
    String ipAddress;
    int port;
    public Notification(String ipAddress,int port) {
        this.ipAddress = ipAddress;
        this.port = port;
    }
    
    public  String getJson(NotificationType type,String source,String message){
        String json="";
        json="{";
        json = json +"\"type\":\""+type.name()+"\",";
        json = json + "\"message\":\""+message+"\",";
        json = json + "\"source\":\""+source+"\"";
        json = json + "}";
        return json;
    }
    public  void sendNotification(NotificationType type,String source,String message) {
        String json;
        Socket socket;
        DataOutputStream dataOutputStream;
        dataOutputStream = null;
        socket = null;
        try {
            json=getJson(type,source,message);
            socket = new Socket(this.ipAddress,this.port);
            dataOutputStream = new DataOutputStream(socket.getOutputStream());
            dataOutputStream.writeBytes(json);
        }
        catch (Exception e) {
            //TODO handle this
            e.printStackTrace();
        }
        finally {
            if(socket!=null) {
                try {
                    socket.close();
                }
                catch(Exception e) {
                    //TODO handle this
                    e.printStackTrace();
                }
            }

            if(dataOutputStream != null) {
                try {
                    dataOutputStream.close();
                }
                catch (Exception e) {
                    //TODO handle this
                    e.printStackTrace();
                }
            }
        }
        
    }
}
