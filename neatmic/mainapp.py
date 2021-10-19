import sys
import daiquiri
import subprocess
# pyside
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget

# local imports
from neatmic.ui.mainapp_ui import Ui_MainWindow
from neatmic.ui.logs_ui import Ui_LogsDialog
from neatmic.utils import ConsoleColorToHTMLStream
from neatmic.consts import WinPaths,WinCommands

#logging
# def _make_log_file(): return daiquiri.output.RotatingFile(LOG_PATH,formatter=daiquiri.formatter.TEXT_FORMATTER,level=daiquiri.logging.DEBUG,max_size_bytes=20*1024*1024,backup_count=5)
def setup_logging(stream):
    # make_dirs(LOG_PATH)
    daiquiri.setup(level=daiquiri.logging.DEBUG,outputs=(
        daiquiri.output.Stream(),
        daiquiri.output.Stream(stream=stream,formatter=daiquiri.formatter.ColorExtrasFormatter(fmt='%(asctime)s %(color)s%(levelname)-8.8s: %(message)s%(color_stop)s %(extras)s',datefmt='%I:%M:%S %p'))
    ))
logger=daiquiri.getLogger('neatmic-main')

class DebugWindow(QWidget):
    def __init__(self):
        super(DebugWindow, self).__init__()
        self.ui: Ui_MainWindow = Ui_LogsDialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        #logging/debug

        self.debug_window=DebugWindow()
        self.ui.logs.triggered.connect(self.debug_window.show)
        setup_logging(ConsoleColorToHTMLStream(self.debug_window.ui.debug_console.append))


        #main buttons
        self.ui.mic_settings.clicked.connect(self.open_mic_settings)
        self.ui.speaker_settings.clicked.connect(self.open_speaker_settings)
        logger.debug('Ready.')


    def open_mic_settings(self):
        #TODO Multi-OS support?
        subprocess.Popen(WinCommands.open_recording_panel.split())
        logger.info('Mic settings opened')

    def open_speaker_settings(self):
        #TODO Multi-OS support?
        subprocess.Popen(WinCommands.open_playback_panel.split())
        logger.info('Speaker settings opened')





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
