package EVProject;
import java.util.ArrayList;
import java.util.Scanner;

public class MainService {
	
	static Scanner sc=new Scanner(System.in);
	static VehicleInventory inventory = new VehicleInventory();
	
	public static void main(String[] args) {
		boolean flag=true;
		initializeInventory();
		while(flag) {
		System.out.println("-------------- Vehicle Rental System -------------");
		System.out.println("1.Admin");
		System.out.println("2.Customer");
		System.out.println("Enter your choice : ");
		int ch=sc.nextInt();
		switch(ch) {
		case 1->showAdminMenu();
		case 2->showCustomerMenu();
		}
		}
	}
	
	private static void initializeInventory() {
		inventory.addVehicle(new Bike("b001",700,true));
		inventory.addVehicle(new Bike("b002",500,false));
		inventory.addVehicle(new Car("c001",5000,7));
		inventory.addVehicle(new Car("c002",7000,9));
		inventory.addVehicle(new Bus("BS001",10000,20));
		inventory.addVehicle(new Bus("BS002",15000,25));
		
		
	}
	
    private static void showCustomerMenu() {
    	System.out.println("-------------------Customer Form---------------------");
    	System.out.println("Enter Customer Name : ");
    	String name=sc.next();
    	System.out.println("Enter Mobile Number : ");
    	long mobile=sc.nextLong();
    	System.out.println("License Available (yes/no) : ");
    	String la=sc.next();
    	if(la.equalsIgnoreCase("yes")) {
    		Customer cust1= new Customer(name,mobile,true);
    		boolean flag=true;
    		while(flag) {
    	System.out.println("--------------Customer Menu--------------");
    	System.out.println("1.Show Available Bikes");
    	System.out.println("2.Show Available Buses");
    	System.out.println("3.Show Available Cars");
    	System.out.println("4.Rent Vehicle"); //email receipt payment connected to this
    	System.out.println("5.Return Vehicle");
    	System.out.println("6.View rented Vehicles ");
    	System.out.println("7.Exit");
    	System.out.println("Enter your choice : ");
    	int ch=sc.nextInt();
    	switch(ch) {
    	case 1->{
    		//Bike.java ---> source code   ---> Bike.class(byte code)
    		inventory.showAvailableVehicles(Bike.class);
    	}
    	case 2->{
    		inventory.showAvailableVehicles(Bus.class);
    	}
    	case 3->{
    		inventory.showAvailableVehicles(Car.class);
    	
    	}
    	case 4->{
    		System.out.println("Enter Vehicle Id : ");
    		String id=sc.next();//b001
    		System.out.println("Enter Number of Days : ");
    		int days=sc.nextInt();
    		Vehicle vehicle=findVehicleById(id);//bike100
    		if(vehicle!=null) {
    			cust1.rentVehicle(vehicle,days);
    		}
    		else {
    			System.out.println("Vehicle not found !");
    		}
    	}
    	case 5->{
    		System.out.println("Enter Vehicle Id : ");
    		String id=sc.next();//b001
    		Vehicle veh=findVehicleById(id);//bike100
    		if(veh!=null) {
    			veh.returnVehicle();
    			cust1.returnVehicle(veh);
    		}
    		else {
    			System.out.println("Vehicle not found !");
    		}
    		
    	}
    	case 6->{
    		cust1.viewRentedVehicles();
    		
    	}
    	case 7 -> flag=false;
    	}
    	}
    	}
    	else {
    		System.out.println("MSG : License is required !");
    	}
		
	}
	
	private static void showAdminMenu() {
		System.out.println("----------Login----------");
		System.out.println("Enter username : ");
		String uname=sc.next();
		System.out.println("Enter password : ");
		String pass=sc.next();
		
		if(admin.authenticate(uname,pass)) {
		System.out.println("Admin verified ");
		boolean flag=true;
		while(flag) {
		System.out.println("---------------Admin Menu---------------");
		System.out.println("1.Add Vehicle");
		System.out.println("2.Remove Vehicle");
		System.out.println("3.Send Vehicle for maintenance");
		System.out.println("4.Complete  Vehicle Maintenance");
		System.out.println("5.Show All Vehicle Info");
		System.out.println("6.Exit");
		System.out.println("Enter your choice : ");
		int ch=sc.nextInt();//1
		switch(ch) {
		case 1->{
			//id and rentalRate
			System.out.println("--------Vehicle-------");
			System.out.println("1.Car");
			System.out.println("2.Bike");
			System.out.println("3.Bus");
			System.out.println("Enter your choice :");
			int n=sc.nextInt();//1
			
			System.out.println("Enter Vehicle ID :");
			String id=sc.next();//c001
			System.out.println("Enter Rental Rate : ");
			double rate=sc.nextDouble();//5000
			
			switch(n) {
			case 1->{
				System.out.println("Enter no of Sests : ");
				int no=sc.nextInt();
				inventory.addVehicle( new Car(id,rate,no));//car100
			}
			case 2->{
				System.out.println("Helmet Available(Yes/No) : ");
				String ha=sc.next();
				boolean hela=ha.equalsIgnoreCase("yes"); //true
				inventory.addVehicle( new Bike(id,rate,hela));//bike100
			}
			case 3->{
				System.out.println("Enter no of Sests : ");
				int no=sc.nextInt();
				inventory.addVehicle( new Bus(id,rate,no));//bus100
			}
			}
			}
		case 2->{
			System.out.println("Enter vehicle Id :");
			String id=sc.next(); //b001
			Vehicle vehicle=findVehicleById(id); //bike100
			if(vehicle!=null) {
				inventory.removeVehicle(vehicle);
			}
			else {
				System.out.println("Vehicle not found !");
			}
		}
		case 3->{
			System.out.println("Enter Vehicle Id :");
			String id=sc.next();
			Vehicle veh=findVehicleById(id);//b001 --->bike100
			if(veh!=null) {
				veh.sendForMaintenance();//bike100
			}
			else {
				System.out.println("Vehicle Not Found !");
			}
			
		}
		case 4->{
			System.out.println("Enter Vehicle Id : ");
			String id=sc.next();
			Vehicle veh=findVehicleById(id);
			if(veh!=null) {
				veh.completeMaintenance();
			}
			else {
				System.out.println("Vehicle Not Found !");
			}
			
		}
		case 5->{
			//[bike100,Car100,Bus100]
			System.out.println("-----------------------------------Vehicle Data-----------------------------------");
			System.out.println("-----------------------------------------------------------------------------------");
			System.out.println("  | Vehicle Id \t| Rental Rate \t| Rented Days \t| Available \t| UnderMaintenance |");
			System.out.println("-----------------------------------------------------------------------------------");
			ArrayList<Vehicle> vehicles= inventory.getAllVehicles();
			for(Vehicle veh:vehicles) {
				System.out.println("  |\t"+veh.getId()+" \t|\t"+veh.getRentalRate()+"\t|\t"+veh.getRentedDays()+"\t|\t"+(veh.isAvailable()?"YES":"NO")+"\t|\t"+(veh.isUnderMaintenance()?"YES":"NO")+"\t|");
				System.out.println("-----------------------------------------------------------------------------------");
			}
		}
		case 6->{
			flag=false;
		}
		default->System.out.println("Invalid Choice !");
		}
		}
		}
		else {
			System.out.println("Wrong credentials ");
		}
	}

	private static Vehicle findVehicleById(String id) {//b005
		ArrayList<Vehicle> vehicles=inventory.getAllVehicles();
		//[bike100,bike200,bus100,....]
		for(Vehicle veh:vehicles) {//bus100
			if(veh.getId().equalsIgnoreCase(id)) {
				return veh;
			}
		}
		return null;
		
	}
	

	
	

}