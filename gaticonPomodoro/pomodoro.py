#!/bin/python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gaticon Pomodoro")

    def initUI(self):
        self.setWindowTitle("Gaticon Pomodoro")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Empezar', self)


if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow()
    window.show()
    app.exec()

