package EVProject;

public class ReceiptGenerator {
	public static void generateReceipt(Customer cust, Vehicle vehicle, int days) {
		System.out.println("--------Receipt--------");
        System.out.println("Name : " + cust.getName());
        System.out.println("Vehicle Id : " + vehicle.getId());
        System.out.println("No of Days : " + days);
        System.out.println("Rental Rate : " + vehicle.getRentalRate());
        System.out.println("Total Amount : " + (vehicle.getRentalRate() * days));
        System.out.println("-----------------------");
    }
}
