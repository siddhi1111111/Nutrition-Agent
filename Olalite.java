package CabBooking;

import java.util.Scanner;

public class Olalite {
	static Scanner sc=new Scanner(System.in);
	static String name;
	static String email;
	static long mobile;
	static int km;
	static double totalBill;
	
	public static void main(String[] args) {
		System.out.println("----------Ola Lite-----------");
		System.out.println("1.signup");
		System.out.println("2.login");
		System.out.println("Enter your choice : ");
		int ch=sc.nextInt();
		switch(ch) {
		case 1->signUp();
		case 2->login();
		}
	}
	
	public static void signUp() {
		System.out.println("-------Sign Up Form----------");
		System.out.println("Enter your name : ");
		name=sc.next();
		System.out.println("Enter your email : ");
		email=sc.next();
		System.out.println("Enter your mobile no : ");
		mobile=sc.nextLong();
		System.out.println("Accout created");
		login();
		}
	
public static void login() {
	System.out.println("----------Login Form-----------");
	System.out.println("Enter mobile number : ");
	long newmob=sc.nextLong();
	if(newmob==mobile) {
		long otp=Math.round(Math.random()*10000);
		System.out.println("Generating OTP : "+otp);
		System.out.println("OTP sent on your mobile");
		System.out.println("Enter otp : ");
		long OTP=sc.nextLong();
		if(OTP==otp) {
			System.out.println("Login Successfully");
			showCabTypes();
		}
		else {
			System.out.println("Invalid OTP");
		}
		}
	else {
		System.out.println("user not found");
	}
		
	}

public static void showCabTypes() {
	System.out.println("-----------Select a Ride-------------");
	System.out.println("1.Auto");
	System.out.println("2.Prime Sedan");
	System.out.println("3.Prime SUV");
	System.out.println("4.Parcel");
	System.out.println("------------------------------------");
	System.out.println("Enter your choice : ");
	int ch=sc.nextInt();
	System.out.println("Enter distance in KM : ");
	km=sc.nextInt();
	switch(ch) {
	case 1->totalBill=km*10;
	case 2->totalBill=km*15;
	case 3->totalBill=km*20;
	case 4->totalBill=km*7;
	}
	System.out.println("Amount to Pay : "+totalBill);
	System.out.println("Proceeding Payment........");
	System.out.println("Payment Done");
	generateBill();
	
}

public static void generateBill() {
	System.out.println("-----------Total Bill-----------");
	System.out.println("Customer name : "+name);
	System.out.println("Email ::"+email);
	System.out.println("Mobile number : "+mobile);
	System.out.println("Total Amount : "+totalBill);
	System.out.println("--------------------------------");
	
}

}