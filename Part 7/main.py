from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(100,100)

        btn = QPushButton("Open file dialog")
        self.setCentralWidget(btn)

app = QApplication([])
window = Window()

window.show()
app.exec()