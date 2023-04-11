
public class PizzeriaRostockFactory extends Pizzeria {
	@Override
	protected Pizza createPizza(String name) {
		Pizza pizza = null;
		if(name.equals("Hawaii")) {
			pizza = new Hawaii();
		}else if(name.equals("Salami")){
			pizza = new Salami();
		}else if(name.equals("Calzone")){
			pizza = new Calzone();
		}else if(name.equals("QuattroStagioni")){
			pizza = new QuattroStagioni();
		}else if(name.equals("RostockSalami")){
			pizza = new RostockSalami();
		}else {
			System.out.println("Ungültig!");
		}
		return pizza;
	}
}
