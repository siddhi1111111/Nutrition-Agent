package EVProject;

public class admin {
	private static final String username="siddhi";
	private static final String password="siddhi2503";
	public static boolean authenticate(String uname,String pass) {
		if(username.equals(uname)&&password.equals(pass)) {
			return true;
		}
		
		return false;
		
	}
	
}