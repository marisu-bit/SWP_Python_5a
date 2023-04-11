package Pull;

public interface Observable {

	public abstract void addClient(Observer client);
	public abstract void deleteClient(Observer client);
	public abstract void All();

}
