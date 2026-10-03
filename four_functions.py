import sys
import serial
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from four_17_11 import Ui_MainWindow

# Try to establish a connection to the Arduino
try:
    arduino_is_open = serial.Serial('COM6', 9600)
    print("Successfully connected to Arduino on COM6")
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    arduino_is_open = None  # Set to None if connection fails

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

       
        # Set slider ranges
        self.dial.setMinimum(0)
        self.dial.setMaximum(255)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(255)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider_2.setMinimum(0)
        self.verticalSlider_2.setMaximum(255)

        # Connect sliders to update methods
        self.horizontalSlider.valueChanged.connect(self.update_motor_speeds)
        self.horizontalSlider_2.valueChanged.connect(self.update_motor_speeds)
        self.verticalSlider.valueChanged.connect(self.update_motor_speeds)
        self.verticalSlider_2.valueChanged.connect(self.update_motor_speeds)

        # Timer to periodically send speeds to Arduino
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_speeds_to_arduino)
        self.timer.start(50)

    def disable_sliders(self):
        """Disable the sliders if Arduino connection is not successful."""
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_2.setEnabled(False)
        self.verticalSlider.setEnabled(False)
        self.verticalSlider_2.setEnabled(False)
        self.dial.setEnabled(False)
        print("Sliders disabled due to Arduino connection failure.")

    def update_motor_speeds(self):
        """Update labels based on slider values."""
        speed1 = self.verticalSlider.value()
        self.label.setText(f"Motor 1: {speed1}")
        print(f"Motor 1 speed updated to {speed1}")

        speed2 = self.horizontalSlider_2.value()
        self.label_2.setText(f"Motor 2: {speed2}")
        print(f"Motor 2 speed updated to {speed2}")

        speed3 = self.verticalSlider_2.value()
        self.label_3.setText(f"Motor 3: {speed3}")
        print(f"Motor 3 speed updated to {speed3}")

        speed4 = self.horizontalSlider.value()
        self.label_4.setText(f"Motor 4: {speed4}")
        print(f"Motor 4 speed updated to {speed4}")

    def send_speeds_to_arduino(self):
        """Send all motor speeds to the Arduino."""
        if arduino_is_open:
            speed1 = self.horizontalSlider.value()
            speed2 = self.verticalSlider.value()
            speed3 = self.horizontalSlider_2.value()
            speed4 = self.verticalSlider_2.value()

            data = f"{speed1},{speed2},{speed3},{speed4}\n"
            print(f"Sending: {data}")

            try:
                arduino_is_open.write(data.encode())
                print(f"Sent to Arduino: {data.strip()}")
            except serial.SerialException as e:
                print(f"Error sending to Arduino: {e}")
        else:
            print("Arduino connection is not open. Failed to send motor speeds.")
            #self.statusBar().showMessage("Error: Unable to send data to Arduino.", 5000)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())