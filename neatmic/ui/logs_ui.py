# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logs.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_LogsDialog(object):
    def setupUi(self, LogsDialog):
        if not LogsDialog.objectName():
            LogsDialog.setObjectName(u"LogsDialog")
        LogsDialog.resize(400, 300)
        self.gridLayout = QGridLayout(LogsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 7)
        self.debug_console = QTextBrowser(LogsDialog)
        self.debug_console.setObjectName(u"debug_console")

        self.gridLayout.addWidget(self.debug_console, 0, 0, 1, 1)

        self.logs_folder = QPushButton(LogsDialog)
        self.logs_folder.setObjectName(u"logs_folder")

        self.gridLayout.addWidget(self.logs_folder, 1, 0, 1, 1)


        self.retranslateUi(LogsDialog)

        QMetaObject.connectSlotsByName(LogsDialog)
    # setupUi

    def retranslateUi(self, LogsDialog):
        LogsDialog.setWindowTitle(QCoreApplication.translate("LogsDialog", u"Debug Logs", None))
        self.debug_console.setPlaceholderText(QCoreApplication.translate("LogsDialog", u"Logs here...", None))
        self.logs_folder.setText(QCoreApplication.translate("LogsDialog", u"Open logs folder...", None))
    # retranslateUi

