# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTextEdit,
    QWidget)

class Ui_AboutWidget(object):
    def setupUi(self, AboutWidget):
        if not AboutWidget.objectName():
            AboutWidget.setObjectName(u"AboutWidget")
        AboutWidget.setProperty("modal", False)
        AboutWidget.resize(424, 350)
        self.gridLayout = QGridLayout(AboutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.about_text = QTextEdit(AboutWidget)
        self.about_text.setObjectName(u"about_text")
        self.about_text.setMinimumSize(QSize(0, 0))
        self.about_text.setReadOnly(True)

        self.gridLayout.addWidget(self.about_text, 0, 0, 1, 1)


        self.retranslateUi(AboutWidget)

        QMetaObject.connectSlotsByName(AboutWidget)
    # setupUi

    def retranslateUi(self, AboutWidget):
        AboutWidget.setWindowTitle(QCoreApplication.translate("AboutWidget", u"About NeatMic", None))
        self.about_text.setPlaceholderText(QCoreApplication.translate("AboutWidget", u"About page here...", None))
    # retranslateUi

