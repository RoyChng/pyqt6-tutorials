from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QColorDialog, QFileDialog
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QAction, QBrush
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400,400)
        self.setWindowTitle("Drawing App")
       

app = QApplication([])
window = MainWindow()
window.show()
app.exec()