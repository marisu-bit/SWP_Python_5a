import java.util.List;
import java.util.ArrayList;

public class BubblesortStrategy implements SortStrategy{

	
	public BubblesortStrategy () {
		
	}
	
	
	//@Override
    public void sort(Numberlist list) {
    	int [] intArr;
    	
    	list.toArray(intArr);
    	
        int k;
        for (int i = 0; i < intArr.length - 1; i++) {
            if (intArr[i] < intArr[i + 1]) {
                continue;
            }
            k = intArr[i];
            intArr[i] = intArr[i + 1];
            intArr[i + 1] = k;
            sort(intArr);
        }
        for (int i = 0; i < intArr.length; i++) {
            System.out.println(i + 1 + ": " + intArr[i]);
        }
    }

    
     
    
}
