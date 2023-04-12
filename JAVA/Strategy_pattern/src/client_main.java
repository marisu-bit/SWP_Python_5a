
public class client_main {

	public static void main(String[] args) {

		Numberlist list = new Numberlist();
		
		list.fill(10); // liste befüllen mit 10 zahlen
		
		list.print();
		
		list.sort(new BubblesortStrategy());
		
	}

}
