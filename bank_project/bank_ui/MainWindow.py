# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 502)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.btnUpdateUser = QPushButton(Widget)
        self.btnUpdateUser.setObjectName(u"btnUpdateUser")
        self.btnUpdateUser.setGeometry(QRect(660, 440, 111, 31))
        self.btnUpdateUser.setAutoFillBackground(False)
        self.btnUpdateUser.setStyleSheet(u"\n"
"background-color: rgb(42, 97, 42);\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 371))
        self.frame.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lblOldUser = QLabel(self.frame)
        self.lblOldUser.setObjectName(u"lblOldUser")
        self.lblOldUser.setGeometry(QRect(40, 30, 101, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOldUser.sizePolicy().hasHeightForWidth())
        self.lblOldUser.setSizePolicy(sizePolicy)
        self.lblOldUser.setLayoutDirection(Qt.LeftToRight)
        self.lblOldUser.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 135, 135);\n"
"font: 18pt \".AppleSystemUIFont\";")
        self.lblOldUser.setScaledContents(False)
        self.lblOldUser.setAlignment(Qt.AlignCenter)
        self.lblNewUser = QLabel(self.frame)
        self.lblNewUser.setObjectName(u"lblNewUser")
        self.lblNewUser.setGeometry(QRect(310, 30, 101, 41))
        self.lblNewUser.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(133, 174, 255);")
        self.lblNewUser.setAlignment(Qt.AlignCenter)
        self.txtEditOldName = QTextEdit(self.frame)
        self.txtEditOldName.setObjectName(u"txtEditOldName")
        self.txtEditOldName.setGeometry(QRect(40, 90, 181, 31))
        self.txtEditOldName.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditOldAmount = QTextEdit(self.frame)
        self.txtEditOldAmount.setObjectName(u"txtEditOldAmount")
        self.txtEditOldAmount.setGeometry(QRect(40, 130, 181, 31))
        self.txtEditOldAmount.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditOldMembershipStatus = QTextEdit(self.frame)
        self.txtEditOldMembershipStatus.setObjectName(u"txtEditOldMembershipStatus")
        self.txtEditOldMembershipStatus.setGeometry(QRect(40, 180, 181, 31))
        self.txtEditOldMembershipStatus.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditNewName = QTextEdit(self.frame)
        self.txtEditNewName.setObjectName(u"txtEditNewName")
        self.txtEditNewName.setGeometry(QRect(310, 90, 181, 31))
        self.txtEditNewName.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditNewAmount = QTextEdit(self.frame)
        self.txtEditNewAmount.setObjectName(u"txtEditNewAmount")
        self.txtEditNewAmount.setGeometry(QRect(310, 130, 181, 31))
        self.txtEditNewAmount.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditNewMembershipStatus = QTextEdit(self.frame)
        self.txtEditNewMembershipStatus.setObjectName(u"txtEditNewMembershipStatus")
        self.txtEditNewMembershipStatus.setGeometry(QRect(310, 180, 181, 31))
        self.txtEditNewMembershipStatus.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtEditPassword = QTextEdit(Widget)
        self.txtEditPassword.setObjectName(u"txtEditPassword")
        self.txtEditPassword.setGeometry(QRect(410, 420, 241, 51))
        self.txtEditPassword.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"")
        self.frame.raise_()
        self.btnUpdateUser.raise_()
        self.txtEditPassword.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Bank Manager", None))
        self.btnUpdateUser.setText(QCoreApplication.translate("Widget", u"Update User", None))
        self.lblOldUser.setText(QCoreApplication.translate("Widget", u"Old User", None))
        self.lblNewUser.setText(QCoreApplication.translate("Widget", u"New User", None))
        self.txtEditOldName.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Name", None))
        self.txtEditOldAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Amount", None))
        self.txtEditOldMembershipStatus.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Membership Status", None))
        self.txtEditNewName.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Name", None))
        self.txtEditNewAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Amount", None))
        self.txtEditNewMembershipStatus.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Membership Status", None))
        self.txtEditPassword.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter password...", None))
    # retranslateUi

