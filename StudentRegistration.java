package RealTimeEx;

import java.util.HashSet;

public class StudentRegistration {

    public static void main(String[] args) {

        HashSet<String> students = new HashSet<>();

        students.add("Siddhi");
        students.add("Atharv");
        students.add("Om");
        students.add("Samarth");
        students.add("Anu");
        students.add("Siddhi"); // Duplicate

        System.out.println("Registered Students:");
        System.out.println(students);
    }
}