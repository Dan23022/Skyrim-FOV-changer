import os
import subprocess
from os.path import expanduser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPalette
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

class App(QWidget):

    def execute(self):
        fov = self.fov_input.text()

        if fov == "":
            popup = QMessageBox()
            popup.setWindowTitle('Error')
            popup.setText('<font color="orange">Please enter a valid FOV')
            popup.setIcon(QMessageBox.Critical)
            popup.exec_()

        else:
            path = expanduser('~\Documents\My Games\Skyrim Special Edition\Skyrim.ini')

            with open(path, 'r', encoding='utf-8') as file:
                os.chmod(path, S_IWUSR | S_IREAD)
                data = file.readlines()

            data[20] = f'fDefaultWorldFOV={fov}\n'

            with open(path, 'w', encoding='utf-8') as file:
                file.writelines(data)
                os.chmod(path, S_IREAD | S_IRGRP | S_IROTH)

            popup = QMessageBox()
            popup.setWindowTitle('Success')
            popup.setText('<font color="orange">FOV successfully changed')
            popup.exec_()

    def __init__(self):
        super().__init__()
        self.title = 'Skyrim FOV changer'
        app.setStyle('Fusion')
        self.initUI()

    def initUI(self):
        width = 400
        height = 200
        self.setWindowTitle(self.title)
        self.setFixedSize(width, height)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)

        qp = QPalette()
        qp.setColor(QPalette.ButtonText, Qt.black)
        qp.setColor(QPalette.Window, Qt.black)
        app.setPalette(qp)

        self.window_title_text = QLabel('<font color="orange">Skyrim FOV Changer', self)
        self.window_title_text.move(width//2-103, height//2-80)
        self.window_title_text.setFont(QFont('Arial', 16))

        self.fov_input = QLineEdit(self)
        self.fov_input.setPlaceholderText('Enter FOV')
        self.fov_input.setGeometry(width//2-57, height//2-30, 115, 25)
        self.fov_input.setFont(font)
        self.fov_input.setAlignment(Qt.AlignCenter)

        self.set_btn = QPushButton('Set', self)
        self.set_btn.setGeometry(width//2-25, height//2 + 14, 50, 20)
        self.set_btn.setFont(font)
        self.set_btn.clicked.connect(self.execute)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())