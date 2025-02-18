import math
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

class calculadoraCientifica(QMainWindow):

    calculadoraCerrada = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.operacionActual = ''
        self.resultado = 0

        self.setUi()
        self.setStyle()
        self.setLayout()
        self.conectarSenales()

    def setUi (self):
        self.setFixedWidth(450)
        self.setFixedHeight(600)
        self.setWindowTitle('Calculadora Científica')

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.centralWidget)

        self.operacionesTextEdit = QTextEdit()
        self.operacionesTextEdit.setReadOnly(True)
        self.mainLayout.addWidget(self.operacionesTextEdit)

        self.botonesLayout = QVBoxLayout()

        self.boton1 = QPushButton('1')
        self.boton2 = QPushButton('2')
        self.boton3 = QPushButton('3')
        self.boton4 = QPushButton('4')
        self.boton5 = QPushButton('5')
        self.boton6 = QPushButton('6')
        self.boton7 = QPushButton('7')
        self.boton8 = QPushButton('8')
        self.boton9 = QPushButton('9')
        self.boton0 = QPushButton('0')

        self.botonSuma = QPushButton('+')
        self.botonResta = QPushButton('-')
        self.botonMult = QPushButton('*')
        self.botonDividir = QPushButton('/')
        self.botonIgual = QPushButton('=')
        self.botonLimpiar = QPushButton('Limpiar')
        self.botonSqrt = QPushButton('Sqrt')
        self.botonPow = QPushButton('Pow')
        self.botonLog = QPushButton('Log')
        self.botonCerrarParentesis = QPushButton(')')
        self.botonAbrirParentesis = QPushButton('(')
        self.botonComa = QPushButton(',')
        self.botonSalir = QPushButton('Salir')

        self.botones = [
            [self.botonPow, self.botonSqrt, self.botonLog, self.botonAbrirParentesis, self.botonCerrarParentesis],
            [self.boton7, self.boton8, self.boton9, self.botonLimpiar, self.botonSalir],
            [self.boton4, self.boton5, self.boton6, self.botonDividir, self.botonMult],
            [self.boton1, self.boton2, self.boton3, self.botonSuma, self.botonResta],
            [self.boton0, self.botonComa, self.botonIgual],
        ]

    def setStyle (self):
        styleSheet = '''
            QMainWindow {
                background: black;
            }

            QPushButton {
                font-size: 15pt;
            }

            QTextEdit {
                font-size: 15pt;
            }
        '''

        self.setStyleSheet(styleSheet)

    def setLayout (self):
        orientVertical = QVBoxLayout()

        for fila in self.botones:
            orientHorizontal = QHBoxLayout()
            for boton in fila:
                orientHorizontal.addWidget(boton)
            orientVertical.addLayout(orientHorizontal)

        self.mainLayout.addLayout(orientVertical)

    def conectarSenales (self):
        self.boton1.clicked.connect(lambda: self.agregarNumero('1'))
        self.boton2.clicked.connect(lambda: self.agregarNumero('2'))
        self.boton3.clicked.connect(lambda: self.agregarNumero('3'))
        self.boton4.clicked.connect(lambda: self.agregarNumero('4'))
        self.boton5.clicked.connect(lambda: self.agregarNumero('5'))
        self.boton6.clicked.connect(lambda: self.agregarNumero('6'))
        self.boton7.clicked.connect(lambda: self.agregarNumero('7'))
        self.boton8.clicked.connect(lambda: self.agregarNumero('8'))
        self.boton9.clicked.connect(lambda: self.agregarNumero('9'))
        self.boton0.clicked.connect(lambda: self.agregarNumero('0'))

        self.botonSuma.clicked.connect(lambda: self.agregarOperacion('+'))
        self.botonResta.clicked.connect(lambda: self.agregarOperacion('-'))
        self.botonMult.clicked.connect(lambda: self.agregarOperacion('*'))
        self.botonDividir.clicked.connect(lambda: self.agregarOperacion('/'))
        self.botonComa.clicked.connect(lambda: self.agregarOperacion(','))
        self.botonSqrt.clicked.connect(lambda: self.agregarOperacion('math.sqrt('))
        self.botonPow.clicked.connect(lambda: self.agregarOperacion('^'))
        self.botonLog.clicked.connect(lambda: self.agregarOperacion('math.log('))
        self.botonAbrirParentesis.clicked.connect(lambda: self.agregarOperacion('('))
        self.botonCerrarParentesis.clicked.connect(lambda: self.agregarOperacion(')'))

        self.botonIgual.clicked.connect(self.calcularResultado)
        self.botonLimpiar.clicked.connect(self.limpiar)
        self.botonSalir.clicked.connect(self.salir)

    def agregarNumero (self, numero):
        self.operacionActual +=numero
        self.operacionesTextEdit.setText(self.operacionActual)

    def agregarOperacion (self, operacion):
        self.operacionActual += operacion
        self.operacionesTextEdit.setText(self.operacionActual)

    def calcularResultado (self):
        try: 
            self.operacionActual = self.operacionActual.replace(',', '.')
            self.operacionActual = self.operacionActual.replace('^', '**')
            self.resultado = eval(self.operacionActual)
            self.operacionesTextEdit.setText(str(self.resultado))
            self.operacionActual = str(self.resultado)

        except Exception as e:
            self.operacionesTextEdit.setText('Error')
            self.operacionActual = ''

    def calcularSqrt (self):
        try:
            self.resultado = math.sqrt(float(self.operacionActual))
            self.operacionesTextEdit.setText(str(self.resultado))
            self.operacionActual = str(self.resultado)

        except Exception as e:
            self.operacionesTextEdit.setText('Error')
            self.operacionActual = ''

    def calcularPow (self):
        try:
            base, exponente = self.operacionActual.split('^')
            self.resultado = math.pow(float(base), float(exponente))
            self.operacionesTextEdit.setText(str(self.resultado))
            self.operacionActual = str(self.resultado)

        except Exception as e:
            self.operacionesTextEdit.setText('Error')
            self.operacionActual = ''

    def calcularLog (self):
        try:
            self.resultado = math.log(float(self.operacionActual))
            self.operacionesTextEdit.setText(str(self.resultado))
            self.operacionActual = str(self.resultado)

        except Exception as e:
            self.operacionesTextEdit.setText('Error')
            self.operacionActual = ''

    def limpiar (self):
        self.operacionActual = ''
        self.operacionesTextEdit.setText('')

    def salir (self):
        self.close()
        self.calculadoraCerrada.emit()

if __name__ == '__main__':

    from main import principal

    app = QApplication([])
    mainWindow = principal()
    calculadora = calculadoraCientifica()
    calculadora.show()
    app.exec()
