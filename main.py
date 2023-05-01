from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtSql import *
import requests
from PyQt6.uic.properties import QtWidgets
from mainForm import Ui_MainWindow


class testApp(QMainWindow, Ui_MainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.postButton.clicked.connect(self.send_data)
        self.getButton.clicked.connect(self.get_data)

    def send_data(self):
        url = 'http://localhost:5000/post_data'

        data = {
            'text': self.lineEdit.text(),
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            QMessageBox.information(self, 'Success', 'Данные отправлены.')
        else:
            QMessageBox.warning(self, 'Error', f'Error: {response.status_code}')

    def get_data(self):
        url = 'http://localhost:5000/get_data'
        response = requests.get(url)
        data = response.json()

        self.textEdit.append(str(data))



app = QApplication([])
window = testApp('http://localhost:5000/')
# form = Form()
# form.setupUi(window)
window.show()
app.exec()

# import requests
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QListView, QPushButton, QMessageBox
# from PyQt6.QtGui import QStandardItemModel, QStandardItem

# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.model = QStandardItemModel()
#         self.listview = QListView()
#         self.listview.setModel(self.model)
#
#         self.btn_get = QPushButton('Get Data')
#         self.btn_get.clicked.connect(self.get_data)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.listview)
#         vbox.addWidget(self.btn_get)
#
#         self.setLayout(vbox)
#
#     def get_data(self):
#         url = 'http://localhost:5000/get_data'
#         response = requests.get(url)
#         data = response.json()
#
#         self.model.clear()
#         for item in data:
#             text = f'{item["id"]} - {item["text"]} - {item["date"]} - {item["time"]}'
#             qitem = QStandardItem(text)
#             self.model.appendRow(qitem)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     w = MyWidget()
#     w.show()
#     app.exec_()