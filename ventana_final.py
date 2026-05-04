from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from txt_ventanas import (
    txt_titulo, win_x, win_y, pos_x, pos_y, txt_1, txt_2,
    txt_workheart, txt_index, txt_res1, txt_res2, txt_res3,
    txt_res4, txt_res5
)


class ventana_final(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.apariencia()
        self.interfaz()
        self.show()
        
    def apariencia(self):
        self.setWindowTitle(txt_titulo)
        self.resize(win_x, win_y)
        self.move(pos_x, pos_y)

    def interfaz(self):
        print('Los resultados son:', self.results())
        self.texto1 = QLabel(txt_workheart + self.results())
        self.texto2 = QLabel(txt_index + str(self.index))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.texto1)
        self.layout.addWidget(self.texto2)
        self.setLayout(self.layout)

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return 'No hay datos para esta edad'
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5