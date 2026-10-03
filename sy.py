from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QImage, QPixmap
import cv2 
import numpy as np


class VideoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window setup
        self.setWindowTitle("Ball Tracking and Timer App")
        self.resize(1575, 843)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Timer display
        self.timer_display = QtWidgets.QLabel("00:20", self.centralwidget)
        self.timer_display.setGeometry(QtCore.QRect(10, 30, 221, 91))
        self.timer_display.setAlignment(QtCore.Qt.AlignCenter)

        # Start button
        self.start_button = QtWidgets.QPushButton("Start", self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 130, 100, 50))
        self.start_button.clicked.connect(self.start_timer)

        # Stop button
        self.stop_button = QtWidgets.QPushButton("Stop", self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(130, 130, 100, 50))
        self.stop_button.clicked.connect(self.stop_timer)

        # Dribble count
        self.dribble_count_label = QtWidgets.QLabel("Dribble Count: 0", self.centralwidget)
        self.dribble_count_label.setGeometry(QtCore.QRect(300, 160, 200, 50))
        self.dribble_count = 0

        # Score count
        self.score_count_label = QtWidgets.QLabel("Score: 0", self.centralwidget)
        self.score_count_label.setGeometry(QtCore.QRect(570, 30, 140, 150))
        self.score_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.score_count = 0

        # System time
        self.system_time_label = QtWidgets.QLabel("", self.centralwidget)
        self.system_time_label.setGeometry(QtCore.QRect(770, 10, 250, 80))
        self.system_time_label.setAlignment(QtCore.Qt.AlignCenter)

        # Ball movement capture
        self.camera_label = QtWidgets.QLabel(self.centralwidget)
        self.camera_label.setGeometry(QtCore.QRect(10, 220, 491, 321))
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)

        # Regular camera recording
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(QtCore.QRect(520, 220, 491, 321))
        self.video_label.setAlignment(QtCore.Qt.AlignCenter)

        # Timer setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = 20  # 20 seconds timer

        # System clock setup
        self.system_clock = QTimer()
        self.system_clock.timeout.connect(self.update_system_time)
        self.system_clock.start(1000)

        # Camera setup
        self.capture = cv2.VideoCapture(0)  # OpenCV camera capture
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.update_camera_feed)

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # Update every second
            self.camera_timer.start(30)  # Start updating the camera feed
        self.dribble_count += 1
        self.dribble_count_label.setText(f"Dribble Count: {self.dribble_count}")

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.camera_timer.isActive():
            self.camera_timer.stop()
        self.score_count += 1
        self.score_count_label.setText(f"Score: {self.score_count}")

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_display.setText(f"00:{self.remaining_time:02d}")
        else:
            self.timer.stop()
            self.camera_timer.stop()
            self.timer_display.setText("Time's Up!")

    def update_system_time(self):
        current_time = QDateTime.currentDateTime()
        self.system_time_label.setText(current_time.toString("hh:mm:ss AP"))

    def update_camera_feed(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB for PyQt
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Ball trajectory tracking (only for the camera feed showing ball movements)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_orange = np.array([5, 50, 50])     # Lower bound for orange
            upper_orange = np.array([15, 255, 255])  # Upper bound for orange
            mask = cv2.inRange(hsv, lower_orange, upper_orange)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            ball_positions = []  # List to store previous ball positions
            for contour in contours:
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                
                # Store current position
                ball_positions.append(center)
                
                # Draw a circle around detected ball
                cv2.circle(frame_rgb, center, radius, (0, 255, 0), 2)

            # Draw trajectory (only if there are previous positions to connect)
            if len(ball_positions) > 1:
                for i in range(1, len(ball_positions)):
                    cv2.line(frame_rgb, ball_positions[i-1], ball_positions[i], (255, 0, 0), 2)

            # Ball movement feed (only apply processing to camera_label)
            ball_image = QImage(frame_rgb, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.camera_label.setPixmap(QPixmap.fromImage(ball_image))

            # Regular camera feed (no trajectory drawing, just display the frame)
            regular_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(regular_image))

    def closeEvent(self, event):
        self.capture.release()  # Release the camera when the app is closed
        super().closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = VideoApp()
    main_window.show()
    sys.exit(app.exec_())
