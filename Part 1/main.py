from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

app = QApplication([])
window = QMainWindow()

# -- Setting up window --
window.setMinimumSize(400,500)
window.setWindowTitle("A new application")
window.setWindowIcon(QIcon("application_icon.png"))

# -- Adding widgets --
# label = QLabel("A new label", alignment=Qt.AlignmentFlag.AlignCenter)
font = window.font()
font.setPointSize(17)
font.setBold(True)
# label.setFont(font)

button = QPushButton("A Button")
button.setFixedSize(100,100)
button.setFont(font)
window.setCentralWidget(button)

window.show()
app.exec()