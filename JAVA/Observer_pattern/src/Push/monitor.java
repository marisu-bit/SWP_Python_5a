package Push;

public class monitor implements Observer{


    private Wetterstation ws;

    public monitor (Wetterstation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update(int temp, int hum) {
 
    	System.out.println("�bergeben Werte");
    	System.out.println("Die ge�nderten Werte:");
        
        System.out.println("Temp: " + temp );
        System.out.println("Hum: " + hum);
    }
    
}
