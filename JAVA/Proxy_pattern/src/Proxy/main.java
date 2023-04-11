package Proxy;

public class main {
public static void main(String[] args) {
	
	Drucker drucker = new PrinterProxy();
	drucker.drucken("Page printed!");
	 ((PrinterProxy) drucker).switchToColor();
	 drucker.drucken("Page printed!");
	 ((PrinterProxy) drucker).switchtoSw();	 
	 drucker.drucken("Page printed!");
	 
	
}
}
