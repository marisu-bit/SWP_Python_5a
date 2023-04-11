package Push;
import java.util.ArrayList;
import java.util.List;

public class Wetterstation implements Observable {

	private List<Observer> observers;
	private int temp;
	private int hum;
	

	public Wetterstation(){
		this.observers = new ArrayList<>();
	}
	
	@Override
    public void addClient(Observer client) {
        this.observers.add(client);
    }

    @Override
    public void deleteClient(Observer client) {
        this.observers.remove(client);
    }
   
    	
    public double getHum() {
        return hum;
    }

    public void setHum(int hum) {
        this.hum = hum;
        this.All();
    }
    
    
    public double getTemp() {
        return temp;
    }

    public void setTemp(int temp) {
        this.temp = temp;
        this.All();
    }

	@Override
	public void All() {
		for (Observer observer : observers){
            observer.update(this.temp,this.hum);
        }		
	}
}
