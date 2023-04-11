package Proxy;

public class PrinterProxy implements Drucker{
	

	 private Drucker swPrinter;
	   private Drucker colorPrinter;
	   private Drucker currentPrinter;
	
	   public void drucken (String text) {
		   currentPrinter.drucken(text);
	   }
	   
	   public PrinterProxy() {
		   swPrinter = new SWPrinter();
		   colorPrinter = new colorPrinter();
		   currentPrinter= swPrinter;
	   }

	public void switchToColor() {
		 currentPrinter = colorPrinter;
	   }
	public void switchtoSw() {
		 currentPrinter = swPrinter;
	   }
}
