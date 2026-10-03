import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTimeEdit, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtMultimedia import QSound  # Import QSound for playing audio

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()

        # Timer Display
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("mm:ss")
        self.time_edit.setTime(QTime(0, 0, 20))  
        self.time_edit.setReadOnly(True)
        self.layout.addWidget(self.time_edit)

        # Status Label
        self.status_label = QLabel("Timer Status: Ready", self)
        self.layout.addWidget(self.status_label)

        # Buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Timer", self)
        self.start_button.clicked.connect(self.start_timer)
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Timer", self)
        self.stop_button.clicked.connect(self.stop_timer)
        button_layout.addWidget(self.stop_button)

        self.layout.addLayout(button_layout)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Initialize timer value
        self.remaining_time = 20  # Time in seconds

        # Sound setup
        self.buzzer_sound = QSound("timer_beep.wav")  # Load your sound file here

        self.setLayout(self.layout)
        self.setWindowTitle("Timer App")

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # Trigger every 1 second
            self.status_label.setText("Timer Status: Running")

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.status_label.setText("Timer Status: Stopped")

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.time_edit.setTime(QTime(0, 0, self.remaining_time))
            self.buzzer_sound.play()  # Play sound effect every second
        else:
            self.timer.stop()
            self.status_label.setText("Timer Status: Completed")
def update_time(self):
        """Decrements the time by 1 second and updates the UI."""
        if self.time_left > 0:
            self.time_left -= 1
            self.update_label()
            self.tts_engine.say(str(self.time_left))
            self.tts_engine.runAndWait()
        else:
            self.timer.stop()
            self.timer_running = False
            self.timerLabel.setText("Time's up!")
            self.tts_engine.say("Time's up!")
            self.tts_engine.runAndWait()

        def update_label(self):
          """Updates the button label with the remaining time."""
        self.lable.setText(f"TIMER: {self.time_left} seconds")
        self.timerLabel.setText(str(self.time_left))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())
