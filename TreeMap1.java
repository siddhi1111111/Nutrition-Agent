package RealTimeEx;

import java.util.TreeMap;

public class TreeMap1 {
    public static void main(String[] args) {

        TreeMap<Integer, String> accounts = new TreeMap<>();
        accounts.put(5003, "Siddhi");
        accounts.put(5001, "Atharv");
        accounts.put(5002, "Anu");
        accounts.put(5005, "Samarth");
        accounts.put(5004, "Om");

        // duplicate key
        accounts.put(5004, "Sakshi");
        System.out.println(accounts.get(5002));
        System.out.println(accounts);
        System.out.println(accounts.keySet());
        System.out.println(accounts.values());
        System.out.println(accounts.entrySet());
    }
}
