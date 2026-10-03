from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1585, 948)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1500, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(750, 0, 20, 801))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 340, 50, 50))
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(6, 400, 45, 45))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1455, 400, 45, 45))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 880, 101, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 830, 41, 31))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.input_x = QtWidgets.QLineEdit(self.centralwidget)
        self.input_x.setGeometry(QtCore.QRect(640, 830, 111, 31))
        self.input_x.setObjectName("input_x")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 830, 41, 31))
        self.label_2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.input_y = QtWidgets.QLineEdit(self.centralwidget)
        self.input_y.setGeometry(QtCore.QRect(850, 830, 111, 31))
        self.input_y.setObjectName("input_y")

        self.path_points = []  # Store path dots
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.move_bot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "BOT"))
        self.label_3.setText(_translate("MainWindow", "Basket"))
        self.label_4.setText(_translate("MainWindow", "Basket"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "X :"))
        self.label_2.setText(_translate("MainWindow", "Y :"))

    # def move_bot(self):
    #     x = int(self.input_x.text())
    #     y = int(self.input_y.text())

    #     max_x = self.frame.width() - self.pushButton_6.width()
    #     max_y = self.frame.height() - self.pushButton_6.height()

    #     x = max(0, min(x, max_x))
    #     y = max(0, min(y, max_y))

    #     # Animation
    #     self.animation = QPropertyAnimation(self.pushButton_6, b"geometry")
    #     self.animation.setDuration(1000)  # 1 second
    #     self.animation.setStartValue(self.pushButton_6.geometry())
    #     self.animation.setEndValue(QtCore.QRect(x, y, 50, 50))
    #     self.animation.start()

    #      # Draw path dots
    #     dot = QtWidgets.QLabel(self.frame)
    #     dot.setGeometry(x + 20, y + 20, 5, 5)  # Small dot in the center
    #     dot.setStyleSheet("background-color: red; border-radius: 2px;")
    #     dot.show()
    #     self.path_points.append(dot)

    # def move_bot(self):
    #     x = int(self.input_x.text())
    #     y = int(self.input_y.text())

    #     max_x = self.frame.width() - self.pushButton_6.width()
    #     max_y = self.frame.height() - self.pushButton_6.height()
    #     x = max(0, min(x, max_x))
    #     y = max(0, min(y, max_y))

    #      # Clear previous path dots
    #     list(map(lambda label: label.deleteLater(), self.path_points))
    #     self.path_points.clear()

    #     # Animation
    #     self.animation = QPropertyAnimation(self.pushButton_6, b"geometry")
    #     self.animation.setDuration(1000)
    #     self.animation.setStartValue(self.pushButton_6.geometry())
    #     self.animation.setEndValue(QtCore.QRect(x, y, 50, 50))
    #     self.animation.start()

    #     # Calculate intermediate points (e.g., every 100 pixels)
    #     start_x, start_y = self.pushButton_6.x(), self.pushButton_6.y()
    #     steps = max(abs(x - start_x), abs(y - start_y)) // 100  # Adjust step size as needed
    #     if steps > 0:
    #         def calc_point(i):
    #             px = int(start_x + (x - start_x) * i / steps)
    #             py = int(start_y + (y - start_y) * i / steps)
    #             dot = QtWidgets.QLabel(self.frame)
    #             dot.setGeometry(px + 20, py + 20, 5, 5)
    #             dot.setStyleSheet("background-color: red; border-radius: 2px;")
    #             dot.show()
    #             return dot

    #         self.path_points.extend(list(map(calc_point, range(1, steps + 1))))

    def move_bot(self):
        x = int(self.input_x.text())
        y = int(self.input_y.text())

        max_x = self.frame.width() - self.pushButton_6.width()
        max_y = self.frame.height() - self.pushButton_6.height()
        x = max(0, min(x, max_x))
        y = max(0, min(y, max_y))

        # Clear previous path dots
        list(map(lambda label: label.deleteLater(), self.path_points))
        self.path_points.clear()

        # Animation
        self.animation = QPropertyAnimation(self.pushButton_6, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.pushButton_6.geometry())
        self.animation.setEndValue(QtCore.QRect(x, y, 50, 50))
        self.animation.start()

        # Draw new path dot
        dot = QtWidgets.QLabel(self.frame)
        dot.setGeometry(x + 20, y + 20, 5, 5)
        dot.setStyleSheet("background-color: red; border-radius: 2px;")
        dot.show()
        self.path_points.append(dot)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
