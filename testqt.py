import requests
import datetime

from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListView
from PyQt6.QtWidgets import QMessageBox

import requests
import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.num_clicks = 0

        self.line_edit = QListView()
        self.btn_send = QPushButton('Send Data')
        self.btn_send.clicked.connect(self.send_data)

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.btn_send)

        self.setLayout(vbox)

    def send_data(self):
        url = 'http://localhost:5000/get_data'

        # data = {
        #     'text': self.line_edit.text(),
        #     # 'num_clicks': self.num_clicks + 1
        # }

        response = requests.get(url)

        if response.status_code == 200:
            # self.num_clicks += 1
            QMessageBox.information(self, 'Success', 'Data sent successfully.')
        else:
            QMessageBox.warning(self, 'Error', f'Error: {response.status_code}')


app = QApplication([])
window = MyWidget()
window.show()
app.exec()