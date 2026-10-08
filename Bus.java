package EVProject;

public class Bus extends Vehicle {

    private int noOfSeats;

    public Bus(String id, double rate, int no) {
        super(id, rate);
        this.noOfSeats = no;
    }

    public void displayInfo() {
    }
}