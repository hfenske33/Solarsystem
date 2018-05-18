import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QStyleFactory

from ui.ControlPanel import ControlField
from ui.GraphicPanel import GraphicField

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        left = GraphicField()
        right = ControlField()

        hbox.addWidget(left)
        hbox.addWidget(right)

        self.setLayout(hbox)

        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle('QSplitter demo')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()