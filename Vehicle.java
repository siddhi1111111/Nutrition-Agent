package EVProject;

public class Vehicle {
	//common properties
	private String id;
	private double rentalRate;
	private boolean isAvailable;
	private int rentedDays;
	private boolean underMaintenance;
	
	//constructor
		public Vehicle(String id, double rentalRate) {
			super();
			this.id = id;
			this.rentalRate = rentalRate;
			this.isAvailable = true;
			this.rentedDays = 0;
			this.underMaintenance = false;
		}
		
	//getters
	
	public String getId() {
		return id;
	}


	public double getRentalRate() {
		return rentalRate;
	}


	public boolean isAvailable() {
		return isAvailable;
	}


	public int getRentedDays() {
		return rentedDays;
	}


	public boolean isUnderMaintenance() {
		return underMaintenance;
	}

	
	
	
	//methods
	public boolean rent(Customer cust,int days) {//cust100
		if(isAvailable) {
			//payment email receipt
			double totalAmount=rentalRate*days;
		
			if(PaymentGateway.processPayment(totalAmount)){//bike100
				this.isAvailable=false;
				rentedDays=days;
				EmailService.sendBookingConfirmation(cust,this,days);
				ReceiptGenerator.generateReceipt(cust,this,days);
				return true;
			}
			else {
				System.out.println("Payment Failed !");
			}
			
		}
		return false;
	}
	
	public void returnVehicle() {
		this.isAvailable=true;
		this.rentedDays=0;
	}
	
	public void sendForMaintenance() {
		if(isAvailable) {
			System.out.println("Sending for maintenance ");
			this.isAvailable=false;
			this.underMaintenance=true;
		}
		else {
			System.out.println("Already under maintenance !");
		}
	}
	
	public void completeMaintenance() {
		if(underMaintenance) {
			System.out.println("Complete Maintenance ");
			this.isAvailable=true;
			this.underMaintenance=false;
		}
		else {
			System.out.println("Maintenance Already Completed !");
		}
	}

}
