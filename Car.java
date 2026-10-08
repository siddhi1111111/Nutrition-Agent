package EVProject;

public class Car extends Vehicle{
	private int noOfSeats;
	
	public Car(String id, double rentalRate,int no) {
		super(id, rentalRate);
		this.noOfSeats=no;
	}

	public void displayInfo() {
		
	}

}
