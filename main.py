from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect
import sys
from random import randint


class OpenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.resize(800, 800)
        self.setWindowTitle('Randcircle')
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(300, 650, 300, 120))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Нарисовать круг")
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(a, b, c))
        radius = randint(50, 500)
        qp.drawEllipse(200, 200, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWindow()
    ex.show()
    sys.exit(app.exec_())