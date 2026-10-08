package EVProject;
import java.util.ArrayList;


public class VehicleInventory {
	ArrayList<Vehicle> vehicles=new ArrayList<Vehicle>();
	//[]
	public void addVehicle(Vehicle veh) {
		vehicles.add(veh);
		System.out.println("Vehicle added !"); 
		//[bike100,car100,bus100]
	}
	
	public void removeVehicle(Vehicle vehicle) {
		vehicles.remove(vehicle); 
		System.out.println("Vehicle Removed !");
	}
	
	public void showAvailableVehicles(Class<?> type) {
		System.out.println("Show Available "+type.getSimpleName()+"s");
		//[bike100,bike200,car100,......]
		
		System.out.println("-----------------------------------------------------------------------------------");
		System.out.println("  | Vehicle Id \t| Rental Rate \t| Rented Days \t| Available \t| UnderMaintenance |");
		System.out.println("-----------------------------------------------------------------------------------");
		for(Vehicle veh:vehicles) { //bike100
			if(type.isInstance(veh) && veh.isAvailable()) {
				System.out.println("  |\t"+veh.getId()+" \t|\t"+veh.getRentalRate()+"\t|\t"+veh.getRentedDays()+"\t|\t"+(veh.isAvailable()?"YES":"NO")+"\t|\t"+(veh.isUnderMaintenance()?"YES":"NO")+"\t|");
				System.out.println("-----------------------------------------------------------------------------------");
			}
		}
	}
	
	public ArrayList<Vehicle> getAllVehicles() {
		return vehicles;
	}

}