import java.util.ArrayList;
import java.util.List;
import java.util.Random;
public class Numberlist {

	Random random= new Random();
	List<number> numbers;
	
	public Numberlist() {
		this.numbers = new ArrayList<number>();
	}
	
	public void addNumber(number num) {
		this.numbers.add(num);
	}
	
	public void fill(int anz) {
		
		for( int i= 0; i<anz; i ++ ) {
			number num = new number(random.nextInt());
			addNumber(num);
		}
	}
	
	public void print() {
		
		for(int i=0;i< numbers.size(); i ++) {
			System.out.println(numbers.get(i));
		}
	}
	
}
