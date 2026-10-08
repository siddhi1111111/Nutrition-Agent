
package EVProject;

import java.util.Properties;
import java.util.Scanner;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class EmailService {
	static Scanner sc=new Scanner(System.in);
		private static final String sender_Mail="siddhikolage8@gmail.com";
		private static final String sender_Pass="eenw mcjd pscy ppul";
	public static void sendBookingConfirmation(Customer cust, Vehicle vehicle, int days) {
		System.out.println("enter receiver mail id:");
		String receiverMail=sc.next();
		
		String title="Vehicle Booking Confirmation";
		String body="Hello"+cust.getName()+","+"Vehicle ID :"+vehicle.getId()+","+"\nToatalAmount:"+vehicle.getRentalRate()+"/nVehicle Booked Successfully !";
		
		
		Properties properties =new Properties();
		 properties.put("mail.smtp.auth", "true");
		 properties.put("mail.smtp.starttls.enable", "true");
		 properties.put("mail.smtp.host", "smtp.gmail.com");
		 properties.put("mail.smtp.port", "587");

	  
	  
	  //mail sesssion
		 Session session=Session.getInstance(properties,new Authenticator() {
			 @Override
			protected PasswordAuthentication getPasswordAuthentication() {
				
				return new PasswordAuthentication(sender_Mail, sender_Pass);
			}
		});
		 
		 


	  
	  //message send  -
		    Message message =new MimeMessage(session); 
			try {
				message.setFrom(new InternetAddress(sender_Mail));
				 message.setRecipient(Message.RecipientType.TO, new InternetAddress(receiverMail)); //astha
				 message.setSubject(title);
				 message.setText(body);
				 Transport.send(message);
			} catch (AddressException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (MessagingException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
	  
            System.out.println("mail send to "+receiverMail);
		
	}

}