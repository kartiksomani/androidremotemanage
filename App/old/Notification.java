package androidremotemanage.app;
public class Notification {
    public static String getJson(String type,String message,String source){
        String json="";
        json="{";
        json = json +"type:'"+type+"'";
        json = json + "message:'"+message+"'";
        json = json + "source:'"+source+"'";
        json = json + "}";
    }
}
