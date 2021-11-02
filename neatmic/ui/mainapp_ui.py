# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainapp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 199)
        MainWindow.setMinimumSize(QSize(504, 0))
        self.load_config = QAction(MainWindow)
        self.load_config.setObjectName(u"load_config")
        self.save_config = QAction(MainWindow)
        self.save_config.setObjectName(u"save_config")
        self.install_vbaudio = QAction(MainWindow)
        self.install_vbaudio.setObjectName(u"install_vbaudio")
        self.documentation = QAction(MainWindow)
        self.documentation.setObjectName(u"documentation")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.logs = QAction(MainWindow)
        self.logs.setObjectName(u"logs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(250, 0))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 480, 85))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mic_section = QFormLayout()
        self.mic_section.setObjectName(u"mic_section")
        self.mic_1_layout = QHBoxLayout()
        self.mic_1_layout.setObjectName(u"mic_1_layout")
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label)

        self.mic_selector = QComboBox(self.scrollAreaWidgetContents_2)
        self.mic_selector.setObjectName(u"mic_selector")
        self.mic_selector.setEditable(False)

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.mic_selector)


        self.mic_1_layout.addLayout(self.formLayout_10)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.mic_volume = QProgressBar(self.scrollAreaWidgetContents_2)
        self.mic_volume.setObjectName(u"mic_volume")
        self.mic_volume.setStyleSheet(u" QProgressBar::chunk {\n"
"     background-color: #3add36;\n"
"\n"
" }")
        self.mic_volume.setMaximum(100)
        self.mic_volume.setValue(0)
        self.mic_volume.setTextVisible(False)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.mic_volume)


        self.mic_1_layout.addLayout(self.formLayout_7)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.mic_delay = QSpinBox(self.scrollAreaWidgetContents_2)
        self.mic_delay.setObjectName(u"mic_delay")
        self.mic_delay.setMinimum(0)
        self.mic_delay.setMaximum(999999999)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.mic_delay)


        self.mic_1_layout.addLayout(self.formLayout_6)


        self.mic_section.setLayout(0, QFormLayout.FieldRole, self.mic_1_layout)

        self.add_mic = QPushButton(self.scrollAreaWidgetContents_2)
        self.add_mic.setObjectName(u"add_mic")

        self.mic_section.setWidget(1, QFormLayout.FieldRole, self.add_mic)


        self.verticalLayout_5.addLayout(self.mic_section)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.output_selector = QComboBox(self.centralwidget)
        self.output_selector.setObjectName(u"output_selector")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.output_selector)


        self.horizontalLayout_4.addLayout(self.formLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mic_settings = QPushButton(self.centralwidget)
        self.mic_settings.setObjectName(u"mic_settings")

        self.horizontalLayout_5.addWidget(self.mic_settings)

        self.speaker_settings = QPushButton(self.centralwidget)
        self.speaker_settings.setObjectName(u"speaker_settings")

        self.horizontalLayout_5.addWidget(self.speaker_settings)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.load_config)
        self.menuFile.addAction(self.save_config)
        self.menuFile.addAction(self.install_vbaudio)
        self.menuHelp.addAction(self.documentation)
        self.menuHelp.addAction(self.about)
        self.menuHelp.addAction(self.logs)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeatMic", None))
        self.load_config.setText(QCoreApplication.translate("MainWindow", u"Load Config...", None))
        self.save_config.setText(QCoreApplication.translate("MainWindow", u"Save Config...", None))
        self.install_vbaudio.setText(QCoreApplication.translate("MainWindow", u"Install VB Audio Cable", None))
        self.documentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
#if QT_CONFIG(statustip)
        self.documentation.setStatusTip(QCoreApplication.translate("MainWindow", u"NeatMic documentation (opens in web browser)", None))
#endif // QT_CONFIG(statustip)
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(statustip)
        self.about.setStatusTip(QCoreApplication.translate("MainWindow", u"About NeatMic", None))
#endif // QT_CONFIG(statustip)
        self.logs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(statustip)
        self.logs.setStatusTip(QCoreApplication.translate("MainWindow", u"Debugging logs", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mic 1:", None))
#if QT_CONFIG(statustip)
        self.mic_selector.setStatusTip(QCoreApplication.translate("MainWindow", u"Selected microphone", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.mic_selector.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.mic_selector.setCurrentText("")
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Current microphone volume", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
#if QT_CONFIG(statustip)
        self.mic_volume.setStatusTip(QCoreApplication.translate("MainWindow", u"Current microphone volume", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Microphone delay in milliseconds (1s = 1000ms)", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delay:", None))
#if QT_CONFIG(statustip)
        self.mic_delay.setStatusTip(QCoreApplication.translate("MainWindow", u"Microphone delay in milliseconds (1s = 1000ms)", None))
#endif // QT_CONFIG(statustip)
        self.mic_delay.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.add_mic.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
#if QT_CONFIG(statustip)
        self.output_selector.setStatusTip(QCoreApplication.translate("MainWindow", u"Output device. Set this to your virtual microphone's \"Input\"", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.mic_settings.setStatusTip(QCoreApplication.translate("MainWindow", u"Open Windows microphone settings", None))
#endif // QT_CONFIG(statustip)
        self.mic_settings.setText(QCoreApplication.translate("MainWindow", u"Mic settings...", None))
#if QT_CONFIG(statustip)
        self.speaker_settings.setStatusTip(QCoreApplication.translate("MainWindow", u"Open Windows speaker settings", None))
#endif // QT_CONFIG(statustip)
        self.speaker_settings.setText(QCoreApplication.translate("MainWindow", u"Speaker settings...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

