package EVProject;

import java.util.ArrayList;

public class Customer {

	private String name;
	private long mobile;
	private boolean isLicenseAvailable;
	private ArrayList<Vehicle>rentedVehicles=new ArrayList<Vehicle>();
	//[]
	
	public Customer(String name, long mobile, boolean la) {
		this.name = name;
		this.mobile = mobile;
		this.isLicenseAvailable =la;
	}

	public void rentVehicle(Vehicle veh,int days) {//bike100
		if(veh.isAvailable()) {
			if(veh.rent(this,days)) { //bike100.veh(cust100)
				rentedVehicles.add(veh);
			}
		}
		else {
			System.out.println("Vehicle not available !");
		}
	}
	
	public String getName() {
		return name;
	}

	public long getMobile() {
		return mobile;
	}

	public boolean isLicenseAvailable() {
		return isLicenseAvailable;
	}

	public ArrayList<Vehicle> getRentedVehicles() {
		return rentedVehicles;
	}

	public void returnVehicle(Vehicle veh) {
		rentedVehicles.remove(veh);
		System.out.println("Vehicle returned !");
	}
    public void returnAllVehicle() {
		
	} 
	
	public void viewRentedVehicles() {
		if(rentedVehicles.isEmpty()) {
			System.out.println("List is Empty !");
		}
		else {
		System.out.println("-----------------------------------------------------------------------------------");
		System.out.println("  | Vehicle Id \t| Rental Rate \t| Rented Days \t| Available \t| UnderMaintenance |");
		System.out.println("-----------------------------------------------------------------------------------");
		
		for(Vehicle veh:rentedVehicles) {
			System.out.println("  |\t"+veh.getId()+" \t|\t"+veh.getRentalRate()+"\t|\t"+veh.getRentedDays()+"\t|\t"+(veh.isAvailable()?"YES":"NO")+"\t|\t"+(veh.isUnderMaintenance()?"YES":"NO")+"\t|");
			System.out.println("-----------------------------------------------------------------------------------");
		}
	}
	}
}