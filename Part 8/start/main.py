from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.setMinimumSize(300,300)
        parentLayout = QGridLayout()

        login_label = QLabel("Login")
        login_label.setObjectName("login_label")
        email_label = QLabel("Email:")
        password_label = QLabel("Password:")

        email_input = QLineEdit()
        password_input = QLineEdit()

        submit_button = QPushButton("Submit")

        parentLayout.addWidget(login_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        parentLayout.addWidget(email_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        parentLayout.addWidget(password_label, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        parentLayout.addWidget(email_input, 1, 1)
        parentLayout.addWidget(password_input, 2, 1)
        parentLayout.addWidget(submit_button, 3, 0, 1, 2)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

app = QApplication([])
window = Window()

window.show()
app.exec()

