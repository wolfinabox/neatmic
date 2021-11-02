import os
import sys
from PySide6 import QtGui
from PySide6 import QtWidgets
import daiquiri
import subprocess
import webbrowser
import ctypes
# pyside
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox,QWidget
from neatmic.audio import mic_from_name, speaker_from_name

# local imports
from neatmic.ui.mainapp_ui import Ui_MainWindow
from neatmic.ui.logs_ui import Ui_LogsDialog
from neatmic.ui.vbaudio_install_ui import Ui_VbaudioInstaller
from neatmic.ui.about_ui import Ui_AboutWidget
from neatmic.utils import ConsoleColorToHTMLStream,local_path
from neatmic import consts

#logging
# def _make_log_file(): return daiquiri.output.RotatingFile(LOG_PATH,formatter=daiquiri.formatter.TEXT_FORMATTER,level=daiquiri.logging.DEBUG,max_size_bytes=20*1024*1024,backup_count=5)
def setup_logging(stream):
    # make_dirs(LOG_PATH)
    daiquiri.setup(level=daiquiri.logging.DEBUG,outputs=(
        daiquiri.output.Stream(),
        daiquiri.output.Stream(stream=stream,formatter=daiquiri.formatter.ColorExtrasFormatter(fmt='%(asctime)s %(color)s%(levelname)-8.8s: %(message)s%(color_stop)s %(extras)s',datefmt='%I:%M:%S %p'))
    ))
logger=daiquiri.getLogger('neatmic-main')

class AboutWindow(QWidget):
    def __init__(self):
        super(AboutWindow,self).__init__()
        self.ui:Ui_AboutWidget=Ui_AboutWidget()
        self.ui.setupUi(self)
        icon=QtGui.QIcon(local_path('resources','icon.png'))
        self.setWindowIcon(icon)
        about_file_path=local_path("resources","about.html")
        self.about_text=""
        try:
            with open(about_file_path,'r') as f:
                self.about_text=f.read()
        except:
            self.about_text=f"Couldn\'t open \"{about_file_path}\""
        self.ui.about_text.setHtml(self.about_text)


class DebugWindow(QWidget):
    def __init__(self):
        super(DebugWindow, self).__init__()
        self.ui: Ui_MainWindow = Ui_LogsDialog()
        self.ui.setupUi(self)
        icon=QtGui.QIcon(local_path('resources','icon.png'))
        self.setWindowIcon(icon)
 

class VBAudioInstallerWindow(QWidget):
    def __init__(self):
        super(VBAudioInstallerWindow, self).__init__()
        self.ui: Ui_MainWindow = Ui_VbaudioInstaller()
        self.ui.setupUi(self)
        icon=QtGui.QIcon(local_path('resources','icon.png'))
        self.setWindowIcon(icon)
        self.vbaudio_zip_path=local_path("resources","temp","vbaudio_virtualcable.zip")
        if os.path.isfile(self.vbaudio_zip_path):
            # self.ui.vbaudio_download.setDisabled(True)
            self.ui.vbaudio_install.setEnabled(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.icon=QtGui.QIcon(local_path('resources','icon.png'))
        self.setWindowIcon(self.icon)
        #thank you windows very cool
        appid=f'wolfinabox.neatmic.neatmic.{consts.version_num}'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

        #logging/debug
        self.debug_window=DebugWindow()
        self.vbaudio_install_window=None
        self.ui.logs.triggered.connect(self.debug_window.show)
        setup_logging(ConsoleColorToHTMLStream(self.debug_window.ui.debug_console.append))

        #actions
        self.about_window=AboutWindow()
        self.ui.about.triggered.connect(self.about_window.show)
        self.ui.documentation.triggered.connect(lambda: webbrowser.open(consts.docs_link,0))
        #main buttons
        self.ui.mic_settings.clicked.connect(self.open_mic_settings)
        self.ui.speaker_settings.clicked.connect(self.open_speaker_settings)
        self.show()
        #further setup
        self.check_vbaudio()

        logger.debug('Ready.')


    def open_mic_settings(self):
        #TODO Multi-OS support?
        subprocess.Popen(consts.WinCommands.open_recording_panel.split())
        logger.info('Mic settings opened')

    def open_speaker_settings(self):
        #TODO Multi-OS support?
        subprocess.Popen(consts.WinCommands.open_playback_panel.split())
        logger.info('Speaker settings opened')

    def check_vbaudio(self):
        vbaudio_mic=mic_from_name('vb-audio')
        vbaudio_speaker=speaker_from_name('vb-audio')
        if (not vbaudio_mic) or (not vbaudio_speaker):
            msgbox=QMessageBox()
            msgbox.setWindowTitle("Neatmic")
            msgbox.setText("VB-Audio Virtual Cable required, but not found.")
            msgbox.setInformativeText("Automatically download and install?")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msgbox.setDefaultButton(QMessageBox.Yes)
            msgbox.setWindowIcon(self.icon)
            ret=msgbox.exec()
            
            if ret==QMessageBox.Yes:
                self.vbaudio_install_window=VBAudioInstallerWindow()
                self.vbaudio_install_window.ui.vbaudio_install_url.setText(consts.WinPaths.vbaudio_download)
                self.vbaudio_install_window.show()
            else:
                return False
        return True

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon(local_path('resources','icon.png')))

    sys.exit(app.exec_())
