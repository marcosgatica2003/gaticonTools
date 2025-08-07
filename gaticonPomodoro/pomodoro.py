#!/bin/python3
# Pomodoro escrito en pyqt5 porque no encontré otro pomodoro god que me guste.
# Dedicado a mi pequeña Melani ^-^~

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.remainingSeconds = 25*60
        self.timerRunning = False

        self.setUI()
        self.setLayout()
        self.setStyle()

    def setUI(self):
        self.setWindowTitle("Gaticon Pomodoro")
        self.setGeometry(100, 100, 300, 200)

        self.timeLabel = QLabel("25:00")
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Empezar', self)

        self.timer = QTimer()
        self.timer.setInterval(1000)

    def setLayout(self):
        centralWidget = QWidget(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.button)
        
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setStyle(self):
        self.setStyleSheet("""
            QLabel {
                font-size: 32px;
                color: #333;
            }

            QPushButton {
                font-size: 18px;
                padding: 8px 16px;
                background-color: #2e8b57;
                color: white;
                border: none;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #3cb371;
            }

            QPushButton:pressed {
                background-color: #276747;
            }
        """)
    
    def startTimer(self):
        self.timer.start()
        self.timerRunning = True
        self.button.setText("Parar")

    def stopTimer(self):
        self.timer.stop()
        self.timerRunning = False
        self.button.setText("Empezar")
    
    def setConnections(self):
        self.button.clicked.connect(self.toggleTimer())
        self.timer.timeout.connect(self.updateTimer())

    def toggleTimer(self):
        if self.timerRunning:
            self.stopTimer()
        else:
            self.startTimer()

    def updateTimer(self):
        if self.remainingSeconds > 0:
            self.remainingSeconds -= 1
            self.updateTimeDisplay()
        else:
            self.stopTimer()
            self.timeLabel.setText("Termino")

    def updateTimeDisplay(self):
        minutos = self.remainingSeconds // 60
        segundos = self.remainingSeconds % 60
        self.timeLabel.setText(f"{minutos:02d}:{segundos:02d}")


if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow()
    window.show()
    app.exec()

