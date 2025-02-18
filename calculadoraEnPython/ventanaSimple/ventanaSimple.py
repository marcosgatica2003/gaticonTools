from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QMenuBar, QAction
from PyQt5.QtWidgets import QTextEdit

from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtCore import Qt


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setUi()
        self.setStyle()
        self.setLayout()

        self.operacionActual = ''
        self.resultado = 0

    def setUi(self):
        self.setFixedWidth(450)
        self.setFixedHeight(600)
        
        self.setWindowTitle('Calculadora')

        menuBar = self.menuBar()

        calculadorasMenu = menuBar.addMenu('Calculadoras')
        conversionesMenu = menuBar.addMenu('Conversiones')
        funcionesMenu = menuBar.addMenu('Funciones')
        preferenciasMenu = menuBar.addMenu('Preferencias')
        acercaDe = menuBar.addMenu('Acerca de')

        cientificaAction = QAction('Científica', self)
        conversionesAction = QAction('Conversiones', self)
        funcionesAction = QAction('Funciones', self)
        preferenciasAction = QAction('Preferencias', self)
        autor = QAction('Autor', self)

        calculadorasMenu.addAction(cientificaAction)
        conversionesMenu.addAction(conversionesAction)
        funcionesMenu.addAction(funcionesAction)
        preferenciasMenu.addAction(preferenciasAction)
        acercaDe.addAction(autor)

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


        self.botones = [
            [self.botonPow, self.botonSqrt, self.botonLog],
            [self.boton7, self.boton8, self.boton9, self.botonDividir],
            [self.boton4, self.boton5, self.boton6, self.botonMult],
            [self.boton0, self.botonLimpiar, self.botonIgual, self.botonSuma],
        ]

    def setStyle(self):

        self.setStyleSheet('''
            QMainWindow {
                background: black;
            }

            QMenuBar {
                background: gray;
                color: black;
            }

            QManuBar::item {
                background: gray;
                color: black;
            }

            QMenuBar::item:select {
                background: lightgray;
            }

            QManu {
                background: gray;
                color: black;
            }

            QMenu::item:select {
                background: lightgray;
            }

        ''')


    def setLayout(self):
        orientVertical = QVBoxLayout()
        
        for fila in self.botones:
            orientHorizontal = QHBoxLayout()
            for boton in fila:
                orientHorizontal.addWidget(boton)
            orientVertical.addLayout(orientHorizontal)

        self.mainLayout.addLayout(orientVertical)
    
    def conectarSenales(self):
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
        
        self.botonIgual.clicked.connect(lambda: self.agregarOperacion(self.calcularResultado))
        self.botonLimpiar.clicked.connect(lambda: self.agregarOperacion(self.limpiar))

    def agregarNumero (self, numero):
        self.operacionActual += numero
        self.operacionesTextEdit.setText(self.operacionActual)

    def agregarOperacion (self, operacion):
        self.operacionActual += operacion
        self.operacionesTextEdit.setText(self.operacionActual)

    def calcularResultado (self):
        try:
            self.resultad = eval(self.operacionActual)
            self.operacionesTextEdit.setText(str(self.resultado))
            self.operacionActual = str(self.resultado)

        except Exception as e:
            self.operacionesTextEdit.setText('Error')
            self.operacionActual = ''

if __name__ == '__main__':
    app = QApplication([])
    win = principal()
    win.show()
    app.exit(app.exec_())









