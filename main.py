from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtSql import *
import requests
from PyQt6.uic.properties import QtWidgets

Form, Window = uic.loadUiType("MainForm.ui")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)



app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()