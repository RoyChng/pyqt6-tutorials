from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QLabel, QPushButton, QWidget
from PyQt6.QtCore import Qt

app = QApplication([])
window = QMainWindow()

window.setMinimumSize(400,400)

parentLayout = QGridLayout()

loginLabel = QLabel("Login", alignment=Qt.AlignmentFlag.AlignCenter)
loginLabel.setMaximumHeight(100)
# font = window.font()
# font.setPointSize(20)
# font.setBold(True)
# loginLabel.setFont(font)
emailLabel = QLabel("Email: ")
passwordLabel = QLabel("Password: ")
emailInput = QLineEdit()
passwordInput = QLineEdit()
passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
submitButton = QPushButton("Submit")

parentLayout.addWidget(loginLabel, 0, 0, 1, 2)
parentLayout.addWidget(emailLabel, 1, 0)
parentLayout.addWidget(emailInput, 1, 1)
parentLayout.addWidget(passwordLabel, 2, 0)
parentLayout.addWidget(passwordInput, 2, 1)
parentLayout.addWidget(submitButton, 3, 0, 1, 2)

centerWidget = QWidget()
centerWidget.setLayout(parentLayout)
window.setCentralWidget(centerWidget)

window.show()
app.exec()