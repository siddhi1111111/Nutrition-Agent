import sys
import cv2
import pyttsx3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer


class VideoCaptureApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tts_engine = pyttsx3.init()  # Initialize the text-to-speech engine

    def initUI(self):
        # Window setup
        self.setWindowTitle("Video Capture with 30-Second Timer and Voice")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Video display
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(50, 50, 640, 480)
        self.video_label.setStyleSheet("background-color: black;")
        self.video_label.setObjectName("video_label")

        # Buttons
        self.start_button = QtWidgets.QPushButton("Start Video", self.centralwidget)
        self.start_button.setGeometry(150, 550, 120, 40)
        self.start_button.clicked.connect(self.start_video)

        self.stop_button = QtWidgets.QPushButton("Stop Video", self.centralwidget)
        self.stop_button.setGeometry(400, 550, 120, 40)
        self.stop_button.clicked.connect(self.stop_video)

        # Timer display
        self.timer_label = QtWidgets.QLabel("Timer: 0s", self.centralwidget)
        self.timer_label.setGeometry(300, 10, 200, 40)
        self.timer_label.setStyleSheet("font: 16pt; color: blue;")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)

        # Initialize timer and video capture
        self.capture = None
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.update_frame)

        self.seconds_elapsed = 0
        self.max_time = 30  # Set timer to 30 seconds
        self.timer_display = QTimer()
        self.timer_display.timeout.connect(self.update_timer)

    def speak(self, text):
        """Speak a given text using pyttsx3."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def start_video(self):
        """Start video capture and 30-second timer."""
        self.capture = cv2.VideoCapture(0)  # Open the default camera
        if not self.capture.isOpened():
            print("Error: Unable to access the camera.")
            self.speak("Unable to access the camera.")
            return

        self.video_timer.start(30)  # Update the video frame every 30ms
        self.timer_display.start(1000)  # Update the timer every 1 second
        self.seconds_elapsed = 0
        self.timer_label.setText("Timer: 0s")
        self.speak("Video started")

    def stop_video(self):
        """Stop video capture."""
        if self.capture:
            self.video_timer.stop()
            self.timer_display.stop()
            self.capture.release()
            self.video_label.clear()
            self.timer_label.setText("Timer: Stopped")
            self.speak("Video stopped")

    def update_frame(self):
        """Update the video frame."""
        if self.capture:
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.video_label.setPixmap(QPixmap.fromImage(qt_image))

    def update_timer(self):
        """Update the timer display."""
        self.seconds_elapsed += 1
        self.timer_label.setText(f"Timer: {self.seconds_elapsed}s")

        if self.seconds_elapsed >= self.max_time:
            self.stop_video()
            self.timer_label.setText("Timer: Completed (30s)")
            self.speak("Timer completed. Video stopped.")

    def closeEvent(self, event):
        """Ensure video capture is released on close."""
        if self.capture:
            self.capture.release()
        event.accept()


if __name__ == "__main__":
    # Install the required library
    # pip install pyttsx3 opencv-python PyQt5
    app = QtWidgets.QApplication(sys.argv)
    main_window = VideoCaptureApp()
    main_window.show()
    sys.exit(app.exec_())
