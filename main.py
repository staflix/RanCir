import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.resize(400, 300)
        self.pushButton = QPushButton('Рисовать', self)
        self.pushButton.clicked.connect(self.paint)
        layout = QVBoxLayout(self)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            self.draw_flag(qp)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        r = random.randint(1, 100)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(
            random.randint(1, 100),
            random.randint(1, 100),
            r,
            r,
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
