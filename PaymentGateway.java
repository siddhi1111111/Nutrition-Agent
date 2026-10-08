package EVProject;

public class PaymentGateway {
	public static boolean processPayment(double amount){
		System.out.println("Processing Payment ..............");
		try {
			Thread.sleep(5000);
			System.out.println("Amount : "+amount);
			System.out.println("Payment Done !");
			return true;
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return false;
	}

}
