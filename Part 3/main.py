from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QCheckBox, QButtonGroup
from PyQt6.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400,150)

        parentLayout = QVBoxLayout()
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(False)

        self.checkBoxRed = QCheckBox("Red")
        self.checkBoxYellow = QCheckBox("Yellow")
        self.checkBoxBlue = QCheckBox("Blue")
        self.checkBoxBlue.setChecked(True)
        self.button = QPushButton("Click me")

        self.buttonGroup.addButton(self.checkBoxRed)
        self.buttonGroup.addButton(self.checkBoxYellow)
        self.buttonGroup.addButton(self.checkBoxBlue)

        self.button.clicked.connect(self.clickHandler)

        parentLayout.addWidget(self.checkBoxRed)
        parentLayout.addWidget(self.checkBoxBlue)
        parentLayout.addWidget(self.checkBoxYellow)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

    def clickHandler(self):
        print("Button Clicked!")
        for button in self.buttonGroup.buttons():
            if button.isChecked():
                print(button.text())

app = QApplication([])
window = Window()

window.show()
app.exec()

