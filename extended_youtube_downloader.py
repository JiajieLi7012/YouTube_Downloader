import sys
from functools import partial

from pytube import YouTube
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class YouTubeDownloaderUI(QMainWindow):
    """View"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('YouTube Downloader')
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createInputLine()
        self._createButtons()
    
    def _createInputLine(self):
        self.line = QLineEdit()
        self.line.setFixedHeight(35)
        self.line.setAlignment(Qt.AlignLeft)
        self.generalLayout.addWidget(self.line)
    
    def _createButtons(self):
        subLayout = QHBoxLayout()
        self.runButton = QPushButton("Download")
        self.clearButton = QPushButton("Clear")
        subLayout.addWidget(self.runButton)
        subLayout.addWidget(self.clearButton)
        self.generalLayout.addLayout(subLayout)
    

    def getURL(self):
        return self.line.text()
    
    def clearURL(self):
        self.line.setText('')

class YouTubeDownloaderCtrl():
    """Controller"""

    def __init__(self,view,model):
        self._view = view
        self._model = model
        self._connectSignals()
    
    def _connectSignals(self):
        self._view.clearButton.clicked.connect(self._view.clearURL)
        self._view.runButton.clicked.connect(partial(self._model,self._view.getURL()))


def downloadYouTube(url):
    if not url:
        alert = QMessageBox()
        alert.setText("No url provided")
        alert.exec_()
    else:
        try:
            yt = YouTube(url)
        except Exception as e:
            alert = QMessageBox()
            alert.setText("Invalid url provided")
            url.clear()
            alert.exec_()
        else:
            ys = yt.streams.get_highest_resolution()
            ys.download('./Videos')
            url.clear()

    


def main():
    u2b = QApplication(sys.argv)
    view = YouTubeDownloaderUI()
    model = downloadYouTube
    YouTubeDownloaderCtrl(view=view,model=model)
    view.show()
    sys.exit(u2b.exec_())

if __name__ == '__main__':
    main()