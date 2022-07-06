# This Python file uses the following encoding: utf-8
import sys

sys.path.append("./")
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from MainWindow import Ui_Widget
from ErrorDialog import Ui_Dialog
import bank_backend.app as bank
from bank_backend.BankUser import BankUser


class ErrorDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnUpdateUser.clicked.connect(
            self.updateUserInfo
        )  

    def displayWrongMessageDialogue(self):
        e = ErrorDialog(self)
        e.exec()

    def updateUserInfo(self):
        password = self.txtEditPassword.toPlainText()

        oldName = self.txtEditOldName.toPlainText()
        oldAmount = self.txtEditOldAmount.toPlainText()
        oldMembershipStatus = self.txtEditOldMembershipStatus.toPlainText()

        newName = self.txtEditNewName.toPlainText()
        newAmount = self.txtEditNewAmount.toPlainText()
        newMembershipStatus = self.txtEditNewMembershipStatus.toPlainText()

        oldUser = BankUser(
            name=oldName, amount=oldAmount, membership_status=oldMembershipStatus
        )

        newUser = BankUser(
            name=newName, amount=newAmount, membership_status=newMembershipStatus
        )

        if (
            bank.update_user_info(password=password, old_data=oldUser, new_data=newUser)
            == 0
        ):
            self.displayWrongMessageDialogue()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
