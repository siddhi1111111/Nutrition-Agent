package RealTimeEx;

import java.util.TreeSet;

public class StudentMarks {

    public static void main(String[] args) {

        TreeSet<Integer> marks = new TreeSet<>();

        marks.add(85);
        marks.add(72);
        marks.add(95);
        marks.add(72); // Duplicate
        marks.add(60);
        marks.add(95); // Duplicate

        System.out.println("Unique Marks:");
        System.out.println(marks);
    }
}