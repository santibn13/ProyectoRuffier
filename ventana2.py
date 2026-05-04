from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, 
    QHBoxLayout, QLineEdit
)
from PyQt5.QtGui import QFont
from txt_ventanas import (
    txt_titulo, win_x, win_y, pos_x, pos_y,
    txt_instruccion1, txt_instruccion2, txt_instruccion3, txt_instruccion4,
    txt_instruccion5, txt_boton1, txt_boton2, txt_boton3, txt_boton4, timer
)
from ventana_final import ventana_final


class ventana_2(QWidget):
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
        self.layout = QHBoxLayout()
        self.layoutI = QVBoxLayout()
        self.layoutD = QVBoxLayout()
        self.instruccion1 = QLabel(txt_instruccion1)
        self.instruccion2 = QLabel(txt_instruccion2)
        self.instruccion3 = QLabel(txt_instruccion3)
        self.instruccion4 = QLabel(txt_instruccion4)
        self.instruccion5 = QLabel(txt_instruccion5)
        self.temporizador = QLabel(timer)
        self.boton1 = QPushButton(txt_boton1)
        self.boton2 = QPushButton(txt_boton2)
        self.boton3 = QPushButton(txt_boton3)
        self.boton4 = QPushButton(txt_boton4)
        self.nombre = QLineEdit()
        self.edad = QLineEdit()
        self.test1 = QLineEdit()
        self.test2 = QLineEdit()
        self.testfinal = QLineEdit()
        self.layoutI.addWidget(self.instruccion1)
        self.layoutI.addWidget(self.nombre)
        self.layoutI.addWidget(self.instruccion2)
        self.layoutI.addWidget(self.edad)
        self.layoutI.addWidget(self.instruccion3)
        self.layoutI.addWidget(self.boton1)
        self.layoutI.addWidget(self.test1)
        self.layoutI.addWidget(self.instruccion4)
        self.layoutI.addWidget(self.boton2)
        self.layoutI.addWidget(self.test2)
        self.layoutI.addWidget(self.instruccion5)
        self.layoutI.addWidget(self.boton3)
        self.layoutI.addWidget(self.testfinal)
        self.layoutI.addWidget(self.boton4, alignment = Qt.AlignCenter)
        self.layoutD.addWidget(self.temporizador)
        self.layout.addLayout(self.layoutI)
        self.layout.addLayout(self.layoutD)
        self.setLayout(self.layout)

    def timer_test(self):
        self.tiempo = QTime(0, 1, 0)
        self.contador = QTimer()
        self.contador.timeout.connect(self.temporizadorEvento1)
        self.contador.start(1000)

    def timer_sits(self):
        self.tiempo = QTime(0, 0, 30)
        self.contador = QTimer()
        self.contador.timeout.connect(self.temporizadorEvento2)
        self.contador.start(1500)

    def timer_final(self):
        self.tiempo = QTime(0, 1, 0)
        self.contador = QTimer()
        self.contador.timeout.connect(self.temporizadorEvento3)
        self.contador.start(1000)

    def temporizadorEvento1(self):
        self.tiempo = self.tiempo.addSecs(-1)
        self.temporizador.setText(self.tiempo.toString('hh:mm:ss'))
        self.temporizador.setFont(QFont('tiempos', 36, QFont.Bold))
        self.temporizador.setStyleSheet('color: rgb(0, 0, 0)')
        if self.tiempo.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def temporizadorEvento2(self):
        self.tiempo = self.tiempo.addSecs(-1)
        self.temporizador.setText(self.tiempo.toString('hh:mm:ss')[6:8])
        self.temporizador.setText(self.tiempo.toString("hh:mm:ss")[6:8])
        self.temporizador.setStyleSheet("color: rgb(0,0,0)")
        self.temporizador.setFont(QFont("tiempos", 36, QFont.Bold))
        if self.tiempo.toString("hh:mm:ss") == "00:00:00":
            self.contador.stop()

    def temporizadorEvento3(self):
        self.tiempo = self.tiempo.addSecs(-1)
        self.temporizador.setText(self.tiempo.toString("hh:mm:ss"))
        if int(self.tiempo.toString("hh:mm:ss")[6:8]) >= 45:
            self.temporizador.setStyleSheet("color: rgb(0,255,0)")
        elif int(self.tiempo.toString("hh:mm:ss")[6:8]) <= 15:
            self.temporizador.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.temporizador.setStyleSheet("color: rgb(0,0,0)")
        self.temporizador.setFont(QFont("tiempos", 36, QFont.Bold))
        if self.tiempo.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def conexion(self):
        self.boton1.clicked.connect(self.timer_test)
        self.boton2.clicked.connect(self.timer_sits)
        self.boton3.clicked.connect(self.timer_final)
        self.boton4.clicked.connect(self.siguiente_ventana)

    def siguiente_ventana(self):
        self.hide()
        self.cal = calculo(self.edad.text(), self.test1.text(),
                           self.test2.text(), self.testfinal.text())
        self.ventana3 = ventana_final(self.cal)

class calculo():
    def __init__(self, edad, test1, test2, test3):
        self.age = int(edad)
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

    