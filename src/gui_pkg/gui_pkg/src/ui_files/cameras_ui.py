# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameras.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(570, 465)
        self.left_camera = QLabel(Form)
        self.left_camera.setObjectName(u"left_camera")
        self.left_camera.setGeometry(QRect(0, 10, 301, 271))
        self.left_camera.setScaledContents(True)
        self.sensors_label = QLabel(Form)
        self.sensors_label.setObjectName(u"sensors_label")
        self.sensors_label.setGeometry(QRect(426, 80, 101, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.left_camera.setText("")
        self.sensors_label.setText("")
    # retranslateUi

