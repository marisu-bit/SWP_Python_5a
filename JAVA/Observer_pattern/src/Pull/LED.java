package Pull;

public class LED implements Observer{

	private Wetterstation ws;

    public LED(Wetterstation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double newTemp = ws.getTemp();
        double newHumidity = ws.getHum();
        
        
        
        if (newTemp <= 35){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
        if (newHumidity <= 60){
            System.out.println("LED_grün");
        }else{
            System.out.println("LED_rot");
        }
    }
    
}
