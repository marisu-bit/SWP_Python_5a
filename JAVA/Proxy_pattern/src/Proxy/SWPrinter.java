package Proxy;

public class SWPrinter implements Drucker {
	public void drucken(String text)
	{
		System.out.println("Printing in black and white: " + text);	
	}

}
