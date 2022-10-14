from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clickHandler)

    def clickHandler(self):
        print("Clicked!")
        entered_task = self.lineEdit.text()
        if entered_task.strip() != "":
            self.listWidget.addItem(entered_task)
            self.lineEdit.setText("")

app = QApplication([])
window = Window()

window.show()
app.exec()