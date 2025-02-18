import sys
import os
import subprocess

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class confirmarCaptura(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Capturar pantasha')
        self.setFixedSize(250,250)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        layout = QVBoxLayout()

        label = QLabel('Guardar?')
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        botonSI = QPushButton('Sí')
        botonSI.clicked.connect(self.aceptar)
        layout.addWidget(botonSI)

        botonNO = QPushButton('No')
        botonNO.clicked.connect(self.noAceptar)
        layout.addWidget(botonNO)

        self.setLayout(layout)
    
    def enviarNotificacion(self, titulo, mensaje):
        try:
            subprocess.run(['notify-send', titulo, mensaje])
        except Exception as e:
            print(f"No se pudo enviar la noti: {e}")

    def aceptar(self):
        # print("Captura guardada")
        rutaArchivo = os.environ.get('nombreRutaGuardado')
        if rutaArchivo:
            directorio = os.path.dirname(rutaArchivo)
            nombreArchivo = os.path.basename(rutaArchivo)
            self.enviarNotificacion(
                "Mel ha guardado la imagen",
                f"Captura {nombreArchivo} guardado en {directorio}"
            )
        self.done(0)

    def noAceptar(self):
        rutaArchivo = os.environ.get('nombreRutaGuardado')
        if rutaArchivo and os.path.exists(rutaArchivo):
            try:
                os.remove(rutaArchivo)
                self.enviarNotificacion(
                    "Captura borrada",
                    ""
                )
                # print("Captura borrada")
            except Exception as e:
                print(f"Error al borrar: {e}")
        self.done(1)

def main():
    app = QApplication(sys.argv)
    dialogo = confirmarCaptura()
    resultado = dialogo.exec_()
    sys.exit(resultado)

if __name__ == '__main__':
    main()

