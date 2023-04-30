import requests
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QListView, QPushButton, \
    QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()
        self.listview = QListView()
        self.listview.setModel(self.model)

        self.btn_get = QPushButton('Get Data')
        self.btn_get.clicked.connect(self.get_data)

        vbox = QVBoxLayout()
        vbox.addWidget(self.listview)
        vbox.addWidget(self.btn_get)

        self.setLayout(vbox)

    def get_data(self):
        url = 'http://localhost:5000/get_data'
        response = requests.get(url)
        data = response.json()

        self.model.clear()
        for item in data:
            text = f'{item["id"]} - {item["text"]} - {item["date"]} - {item["time"]}'
            qitem = QStandardItem(text)
            self.model.appendRow(qitem)


app = QApplication([])
window = MyWidget()
window.show()
app.exec()