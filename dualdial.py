import sys
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDial, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

# Set up the serial connection
try:
    arduino = serial.Serial('COM6', 9600)  # Replace 'COM6' with your Arduino's port
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None


class MotorControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout()

        # Motor 1 controls
        layout.addWidget(QLabel("Motor 1 Controls"))
        self.dial1 = QDial()
        self.dial1.setRange(0, 255)
        self.dial1.valueChanged.connect(self.update_motor1_speed)
        layout.addWidget(self.dial1)

        # Buttons for Motor 1
        button_layout1 = QHBoxLayout()
        self.start_button1 = QPushButton("Start Motor 1")
        self.start_button1.clicked.connect(self.start_motor1)
        button_layout1.addWidget(self.start_button1)

        self.stop_button1 = QPushButton("Stop Motor 1")
        self.stop_button1.clicked.connect(self.stop_motor1)
        button_layout1.addWidget(self.stop_button1)

        self.reverse_button1 = QPushButton("Reverse Motor 1")
        self.reverse_button1.clicked.connect(self.reverse_motor1)
        button_layout1.addWidget(self.reverse_button1)

        layout.addLayout(button_layout1)

        # Motor 2 controls
        layout.addWidget(QLabel("Motor 2 Controls"))
        self.dial2 = QDial()
        self.dial2.setRange(0, 255)
        self.dial2.valueChanged.connect(self.update_motor2_speed)
        layout.addWidget(self.dial2)

        # Buttons for Motor 2
        button_layout2 = QHBoxLayout()
        self.start_button2 = QPushButton("Start Motor 2")
        self.start_button2.clicked.connect(self.start_motor2)
        button_layout2.addWidget(self.start_button2)

        self.stop_button2 = QPushButton("Stop Motor 2")
        self.stop_button2.clicked.connect(self.stop_motor2)
        button_layout2.addWidget(self.stop_button2)

        self.reverse_button2 = QPushButton("Reverse Motor 2")
        self.reverse_button2.clicked.connect(self.reverse_motor2)
        button_layout2.addWidget(self.reverse_button2)

        layout.addLayout(button_layout2)

        self.setLayout(layout)
        self.setWindowTitle("Motor Control")

    def send_command(self, command):
        if arduino and arduino.isOpen():
            arduino.write((command + '\n').encode())
        else:
            print(f"Failed to send command: {command} (Arduino not connected)")

    def update_motor1_speed(self, value):
        self.send_command(f"M1_SPEED {value}")

    def start_motor1(self):
        speed = self.dial1.value()
        self.send_command(f"M1_START {speed}")

    def stop_motor1(self):
        self.send_command("M1_STOP")

    def reverse_motor1(self):
        speed = self.dial1.value()
        self.send_command(f"M1_REVERSE {speed}")

    def update_motor2_speed(self, value):
        self.send_command(f"M2_SPEED {value}")

    def start_motor2(self):
        speed = self.dial2.value()
        self.send_command(f"M2_START {speed}")

    def stop_motor2(self):
        self.send_command("M2_STOP")

    def reverse_motor2(self):
        speed = self.dial2.value()
        self.send_command(f"M2_REVERSE {speed}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorControlApp()
    window.show()
    sys.exit(app.exec_())
    