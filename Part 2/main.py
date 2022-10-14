from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel
from PyQt6.QtCore import Qt

app = QApplication([])
window = QMainWindow()

window.setMinimumSize(400,400)

parentLayout = QGridLayout()

label = QLabel("This is a label", alignment=Qt.AlignmentFlag.AlignCenter)
parentLayout.addWidget(label,0, 0, 1, 2)

button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
parentLayout.addWidget(button1, 1, 0)
parentLayout.addWidget(button2, 1, 1)

parentLayout.setHorizontalSpacing(50)

centerWidget = QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.show()
app.exec()