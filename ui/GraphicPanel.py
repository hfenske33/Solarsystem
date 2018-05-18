from PyQt5.QtWidgets import QFrame, QDial, QLabel
from PyQt5.QtCore import Qt



class GraphicField(QFrame):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.StyledPanel)


        self.setStyleSheet("background-color: rgb(200, 255, 255)")
