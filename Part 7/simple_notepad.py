from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QGridLayout, QWidget
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500,300)
        self.setWindowTitle("Notedly")

        parentLayout = QGridLayout()

        self.textEdit = QTextEdit()
        saveBtn = QPushButton("Save File")
        openBtn = QPushButton("Open File")

        parentLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        parentLayout.addWidget(saveBtn, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        parentLayout.addWidget(openBtn, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        centralWidget = QWidget()
        centralWidget.setLayout(parentLayout)

        self.setCentralWidget(centralWidget)

app = QApplication([])
window = Window()

window.show()
app.exec()