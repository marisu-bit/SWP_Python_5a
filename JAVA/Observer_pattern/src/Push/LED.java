package Push;

public class LED implements Observer{

	private Wetterstation ws;

    public LED(Wetterstation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update(int temp, int hum) {

    	// in der Pull methode muss man sich die hum und temp holen
    	// in der Push werden sie üergeben
        
        if (temp <= 35){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
        if (hum <= 60){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
    }
    
}
