# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(304, 189)
        Dialog.setStyleSheet(u"background-color: rgb(133, 133, 133);")
        self.btnConfirmError = QPushButton(Dialog)
        self.btnConfirmError.setObjectName(u"btnConfirmError")
        self.btnConfirmError.setGeometry(QRect(100, 140, 100, 32))
        self.btnConfirmError.setStyleSheet(u"background-color: rgb(132, 255, 149);\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 281, 101))
        self.label.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 149, 154);")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnConfirmError.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Wrong password!", None))
    # retranslateUi

