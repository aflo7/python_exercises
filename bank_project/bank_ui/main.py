# This Python file uses the following encoding: utf-8
import sys
sys.path.append('./')
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from MainWindow import Ui_Widget
# from bank_backend.BankUser import BankUser
# from bank_backend.app import read_user_data, get_number_of_users


class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushMe.clicked.connect(hello) # when the button is clicked, run the function hello

def hello():
        print("HEllo world")
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
