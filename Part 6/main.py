from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon, QPixmap
import os
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        icon_file_path = os.path.join(sys._MEIPASS, "images/application_icon.ico")
        image_file_path = os.path.join(sys._MEIPASS, "images/monitor.png")

        parentLayout = QVBoxLayout()

        self.setWindowTitle("PyInstaller Showcase")
        self.setWindowIcon(QIcon(icon_file_path))
        self.setMinimumSize(300,300)

        button = QPushButton("Click me")
        label = QLabel()
        label.setPixmap(QPixmap(image_file_path))
        
        parentLayout.addWidget(button)
        parentLayout.addWidget(label)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)

        self.setCentralWidget(centerWidget)

app = QApplication([])
window = Window()

window.show()
app.exec()