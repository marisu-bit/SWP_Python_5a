package Pull;

public class monitor implements Observer{


    private Wetterstation ws;

    public monitor (Wetterstation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
    	System.out.println("Es hat sich was geändert");
    	System.out.println("Die geholten Werte:");
        double temp = ws.getTemp();
        double hum = ws.getHum();
        System.out.println("Temp: " + temp );
        System.out.println("Hum: " + hum);
    }
    
}
