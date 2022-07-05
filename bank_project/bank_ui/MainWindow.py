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
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"background-color: rgb(98, 181, 111);")
        self.pushMe = QPushButton(Widget)
        self.pushMe.setObjectName(u"pushMe")
        self.pushMe.setGeometry(QRect(360, 480, 100, 32))
        self.pushMe.setStyleSheet(u"color: rgb(255, 11, 7)")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 771, 391))
        self.frame.setStyleSheet(u"background-color: rgb(198, 198, 198)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 101, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 135, 135);\n"
"font: 18pt \".AppleSystemUIFont\";")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 40, 101, 41))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 18pt \".AppleSystemUIFont\";\n"
"background-color: rgb(133, 174, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame.raise_()
        self.pushMe.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Bank Manager", None))
        self.pushMe.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Old User", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"New User", None))
    # retranslateUi

