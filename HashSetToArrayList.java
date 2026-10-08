package RealTimeEx;

import java.util.ArrayList;
import java.util.HashSet;

public class HashSetToArrayList {

    public static void main(String[] args) {

        HashSet<Integer> set = new HashSet<>();

        set.add(10);
        set.add(20);
        set.add(30);
        set.add(20); // Duplicate
        set.add(40);

        System.out.println("HashSet: " + set);

        // Convert HashSet into ArrayList
        ArrayList<Integer> list = new ArrayList<>(set);

        System.out.println("ArrayList: " + list);
    }
}