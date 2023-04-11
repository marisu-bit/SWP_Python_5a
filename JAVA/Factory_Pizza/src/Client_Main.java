
public class Client_Main {

	public static void main(String[] args) {
		
		Pizzeria berlinPizzeria = new PizzeriaBerlinFactory();
		berlinPizzeria.pizzaBekommen("BerlinSalami");
		
		Pizzeria HamburgPizzeria = new PizzeriaHamburgFactory();
		HamburgPizzeria.pizzaBekommen("HamburgSalami");

		Pizzeria RostockPizzeria = new PizzeriaRostockFactory();
		RostockPizzeria.pizzaBekommen("RostockSalami");

	}

}
