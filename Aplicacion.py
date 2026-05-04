from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from txt_ventanas import (
    txt_titulo, txt_bienvenida, win_x, win_y, pos_x, pos_y,
    txt_instrucciones, txt_boton
)
from ventana2 import ventana_2


class main_win(QWidget):
    def __init__(self):
        super().__init__()
        self.apariencia()
        self.interfaz()
        self.conexion()
        self.show()

    def apariencia(self):
        self.setWindowTitle(txt_titulo)
        self.resize(win_x, win_y)
        self.move(pos_x, pos_y)

    def interfaz(self):
        self.txt_bienvenida = QLabel(txt_bienvenida)
        self.instrucciones = QLabel(txt_instrucciones)
        self.boton = QPushButton(txt_boton)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_bienvenida)
        self.layout.addWidget(self.instrucciones)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)

    def conexion(self):
        self.boton.clicked.connect(self.proxima_ventana)
  
    def proxima_ventana(self):
        self.hide()
        self.ventana2 = ventana_2()


app = QApplication([])
mw = main_win()
app.exec_()
