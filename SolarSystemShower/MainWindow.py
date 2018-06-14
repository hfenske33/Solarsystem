'''
The main window takes the control user interface and graphics user
interface and displays them side by side in a widget.
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QStyleFactory

from ControlPanel import UIControl
from GraphicPanel import UIGraphic


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        left = UIGraphic()
        right = UIControl(left)
        hbox.addWidget(left)
        hbox.addWidget(right)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Solarsystem-Shower')
        self.setFixedWidth(1200)
        self.setFixedHeight(800)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
