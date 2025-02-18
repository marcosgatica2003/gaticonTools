import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

from calculadoraCientifica import calculadoraCientifica

class principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setUi()
        self.setStyle()
        self.setLayout()

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

        cientificaAction.triggered.connect(self.abrirCalculadoraCientifica)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.centralWidget)

    def setStyle(self):
        styleSheet = '''
            QMainWindow {
                background: black;
            }

            QMenuBar {
                background: gray;
                color: black;
                font-size: 15pt;
            }
            
            QMenuBar::item {
                background: lightgray;
                color: black;
            }
            
            QMenuBar::item:selected {
                background: lightgray;
            }

            QMenu {
                background: gray;
                color: white;
            }

            QMenu::item:selected {
                background: lightgray;
            }
        '''

        self.setStyleSheet(styleSheet)
    
    def setLayout(self):
        pass

    def abrirCalculadoraCientifica(self):
        self.calculadora = calculadoraCientifica()
        self.calculadora.calculadoraCerrada.connect(self.mostrarPrincipal)
        self.calculadora.show()
        self.hide()
    
    def mostrarPrincipal(self):
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    mainWindowInstance = principal()
    mainWindowInstance.show()
    app.exec()
