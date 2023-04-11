package Pull;

public class main {
	public static void main(String[] args) {
		Wetterstation ws = new Wetterstation();
		
		LED l1= new LED(ws);
		LED l2= new LED(ws);
		monitor m1 = new monitor(ws);
		monitor m2 = new monitor(ws);
		monitor m3 = new monitor(ws);
		
	ws.setHum(30);
	ws.setTemp(14);
		
	}
}
