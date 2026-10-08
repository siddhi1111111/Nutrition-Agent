
package EVProject;

public class Bike extends Vehicle {

    private boolean helmetAvailable;

    public Bike(String id, double rentalRate, boolean ha) {

        super(id, rentalRate);

        this.helmetAvailable = ha;
    }
}