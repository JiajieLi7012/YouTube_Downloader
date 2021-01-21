import sys
from pytube import YouTube
from PyQt5.QtWidgets import *

def start_downloading():
    if not url.text():
        alert = QMessageBox()
        alert.setText("No url provided")
        alert.exec_()
    else:
        try:
            yt = YouTube(url.text())
        except Exception as e:
            alert = QMessageBox()
            alert.setText("Invalid url provided")
            url.clear()
            alert.exec_()
        else:
            ys = yt.streams.get_highest_resolution()
            ys.download('./Videos')
            url.clear()


app = QApplication([])
window = QWidget()
window.setWindowTitle("YouTube Downloader")
window.setGeometry(100, 100, 280, 80)

layout = QVBoxLayout()
prompt = QLabel("Enter the link of YouTube video you want to download below:")
layout.addWidget(prompt)

url = QLineEdit()
layout.addWidget(url)

download_button = QPushButton('Download')
download_button.clicked.connect(start_downloading)
layout.addWidget(download_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())



