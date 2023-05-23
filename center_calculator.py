#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Search for the coordinates of the centers of circles by two intersection points and a radius
"""

import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_input = QGridLayout()
        self.grid_result = QGridLayout()
        self.grid_or = QGridLayout()
        self.v_layout = QVBoxLayout()
        self.lbl = QLabel()
        self.pb_result = QPushButton()
        self.pb_result.setText('Calculate')
        self.lbl_template = QLabel()
        self.img = QPixmap('./template.jpg')
        self.img_resize = self.img.scaled(500, 500)
        self.lbl_template.setPixmap(self.img_resize)

        self.lbl_ax = QLabel()
        self.lbl_ax.setText('ax:')
        self.lbl_ay = QLabel()
        self.lbl_ay.setText('ay:')
        self.lbl_bx = QLabel()
        self.lbl_bx.setText('bx:')
        self.lbl_by = QLabel()
        self.lbl_by.setText('by:')
        self.raduis = QLabel()
        self.raduis.setText('R:')

        self.ln_ax = QLineEdit()
        self.ln_ax.setText('4')
        self.ln_ay = QLineEdit()
        self.ln_ay.setText('3')
        self.ln_bx = QLineEdit()
        self.ln_bx.setText('6')
        self.ln_by = QLineEdit()
        self.ln_by.setText('8')
        self.ln_r = QLineEdit()
        self.ln_r.setText('10')

        self.lbl_result = QLabel()
        self.lbl_result.setText('Result:')

        self.o1x = QLabel()
        self.o1x.setText('o1x:')
        self.o1x_out = QLabel()
        self.o1x_out.setText('---')

        self.o1y = QLabel()
        self.o1y.setText('o1y:')
        self.o1y_out = QLabel()
        self.o1y_out.setText('---')

        self.o2x = QLabel()
        self.o2x.setText('o2x:')
        self.o2x_out = QLabel()
        self.o2x_out.setText('---')

        self.o2y = QLabel()
        self.o2y.setText('o2y:')
        self.o2y_out = QLabel()
        self.o2y_out.setText('---')



        self.init_ui()

    def init_ui(self):
        self.grid_input.addWidget(self.lbl_ax, 1, 1, )
        self.grid_input.addWidget(self.ln_ax, 1, 2, )
        self.grid_input.addWidget(self.lbl_ay, 1, 3, )
        self.grid_input.addWidget(self.ln_ay, 1, 4, )
        self.grid_input.addWidget(self.lbl_bx, 2, 1, )
        self.grid_input.addWidget(self.ln_bx, 2, 2, )
        self.grid_input.addWidget(self.lbl_by, 2, 3, )
        self.grid_input.addWidget(self.ln_by, 2, 4, )
        self.grid_input.addWidget(self.raduis, 3, 1, )
        self.grid_input.addWidget(self.ln_r, 3, 2, )

        self.grid_result.addWidget(self.o1x, 1, 1, )
        self.grid_result.addWidget(self.o1x_out, 1, 2, )
        self.grid_result.addWidget(self.o1y, 1, 3, )
        self.grid_result.addWidget(self.o1y_out, 1, 4, )

        self.grid_result.addWidget(self.o2x, 2, 1, )
        self.grid_result.addWidget(self.o2x_out, 2, 2, )
        self.grid_result.addWidget(self.o2y, 2, 3, )
        self.grid_result.addWidget(self.o2y_out, 2, 4, )


        self.pb_result.clicked.connect(self.calculate)

        self.v_layout.addWidget(self.lbl_template)
        self.v_layout.addLayout(self.grid_input)
        self.v_layout.addWidget(self.lbl_result)
        self.v_layout.addLayout(self.grid_result)
        self.v_layout.addWidget(self.pb_result)
        self.setLayout(self.v_layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Center')
        self.show()

    def calculate(self):
        ax = float(self.ln_ax.text())
        ay = float(self.ln_ay.text())
        bx = float(self.ln_bx.text())
        by = float(self.ln_by.text())
        rad = float(self.ln_r.text())

        ab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
        ho = math.sqrt(rad ** 2 - (ab / 2) ** 2)

        o1x = ax + (bx - ax) / 2 + (by - ay) * ho / ab
        o1y = ay + (by - ay) / 2 - (bx - ax) * ho / ab
        o2x = ax + (bx - ax) / 2 - (by - ay) * ho / ab
        o2y = ay + (by - ay) / 2 + (bx - ax) * ho / ab

        self.o1x_out.setText('%s' % round(o1x, 3))
        self.o1y_out.setText('%s' % round(o1y, 3))
        self.o2x_out.setText('%s' % round(o2x, 3))
        self.o2y_out.setText('%s' % round(o2y, 3))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())



"""
ax = 5
ay = 6
bx = 10
by = 7
R = 8

ab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
ho = math.sqrt(R ** 2 - (ab / 2) ** 2)

o1x = ax + (bx - ax) / 2 + (by - ay) * ho / ab
o1y = ay + (by - ay) / 2 - (bx - ax) * ho / ab
# O2x = Ax + (Bx - Ax)/2 - (By - Ay) *HO/AB
# O2y = Ay + (By - Ay)/2 + (Bx - Ax) *HO/AB

print(o1x, o1y)
"""