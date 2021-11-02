# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vbaudio_install.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_VbaudioInstaller(object):
    def setupUi(self, VbaudioInstaller):
        if not VbaudioInstaller.objectName():
            VbaudioInstaller.setObjectName(u"VbaudioInstaller")
        VbaudioInstaller.resize(400, 300)
        self.gridLayout = QGridLayout(VbaudioInstaller)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vbaudio_console = QTextEdit(VbaudioInstaller)
        self.vbaudio_console.setObjectName(u"vbaudio_console")
        self.vbaudio_console.setReadOnly(True)

        self.gridLayout.addWidget(self.vbaudio_console, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vbaudio_download = QPushButton(VbaudioInstaller)
        self.vbaudio_download.setObjectName(u"vbaudio_download")

        self.horizontalLayout.addWidget(self.vbaudio_download)

        self.vbaudio_install = QPushButton(VbaudioInstaller)
        self.vbaudio_install.setObjectName(u"vbaudio_install")
        self.vbaudio_install.setEnabled(False)

        self.horizontalLayout.addWidget(self.vbaudio_install)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.vbaudio_progressbar = QProgressBar(VbaudioInstaller)
        self.vbaudio_progressbar.setObjectName(u"vbaudio_progressbar")
        self.vbaudio_progressbar.setEnabled(False)
        self.vbaudio_progressbar.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vbaudio_progressbar)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)

        self.vbaudio_install_url = QLineEdit(VbaudioInstaller)
        self.vbaudio_install_url.setObjectName(u"vbaudio_install_url")

        self.gridLayout.addWidget(self.vbaudio_install_url, 1, 0, 1, 1)


        self.retranslateUi(VbaudioInstaller)

        QMetaObject.connectSlotsByName(VbaudioInstaller)
    # setupUi

    def retranslateUi(self, VbaudioInstaller):
        VbaudioInstaller.setWindowTitle(QCoreApplication.translate("VbaudioInstaller", u"VB-Audio Installer", None))
#if QT_CONFIG(statustip)
        self.vbaudio_console.setStatusTip(QCoreApplication.translate("VbaudioInstaller", u"Status/information about the VB-Audio Cable download. Read me!", None))
#endif // QT_CONFIG(statustip)
        self.vbaudio_console.setPlaceholderText(QCoreApplication.translate("VbaudioInstaller", u"Install logs here...", None))
#if QT_CONFIG(statustip)
        self.vbaudio_download.setStatusTip(QCoreApplication.translate("VbaudioInstaller", u"Download from the above URL", None))
#endif // QT_CONFIG(statustip)
        self.vbaudio_download.setText(QCoreApplication.translate("VbaudioInstaller", u"Download", None))
#if QT_CONFIG(statustip)
        self.vbaudio_install.setStatusTip(QCoreApplication.translate("VbaudioInstaller", u"Run the VB audio cable installer", None))
#endif // QT_CONFIG(statustip)
        self.vbaudio_install.setText(QCoreApplication.translate("VbaudioInstaller", u"Install", None))
#if QT_CONFIG(statustip)
        self.vbaudio_progressbar.setStatusTip(QCoreApplication.translate("VbaudioInstaller", u"Download progress", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.vbaudio_install_url.setStatusTip(QCoreApplication.translate("VbaudioInstaller", u"URL to download VB-Audio Cable from", None))
#endif // QT_CONFIG(statustip)
        self.vbaudio_install_url.setPlaceholderText(QCoreApplication.translate("VbaudioInstaller", u"VB-Audio cable install URL...", None))
    # retranslateUi

