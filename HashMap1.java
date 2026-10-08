package RealTimeEx;

import java.util.HashMap;
import java.util.Map.Entry;

public class HashMap1 {
    public static void main(String[] args) {

        HashMap<Long, String> contacts = new HashMap<>();
        contacts.put(9876543210L, "Siddhi");
        contacts.put(8765432109L, "Atharv");
        contacts.put(7654321098L, "Anu");
        contacts.put(9876543210L, "Samarth");
        contacts.put(9123456780L, "Om");

        contacts.put(null, null);

        System.out.println(contacts);
        System.out.println(contacts.get(9876543210L));
        System.out.println(contacts.containsKey(9876543210L));
        System.out.println(contacts.isEmpty());
        System.out.println(contacts.remove(9123456780L));
        System.out.println(contacts);
        System.out.println(contacts.keySet());
        System.out.println(contacts.values());
        System.out.println(contacts.entrySet());

        // Iterate HashMap
        for (Long a : contacts.keySet()) {
            System.out.println(a + " = " + contacts.get(a));
        }

        // forEach loop
        contacts.forEach((a, b) -> System.out.println(a + " = " + b));

        // Entry
        for (Entry<Long, String> a : contacts.entrySet()) {
            System.out.println(a);
        }
    }
}