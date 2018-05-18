from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Showerhead(QLabel):
    def __init__(self, Qwidget):
        super().__init__(Qwidget)
        self.showerOn = QPixmap('pics/showeron.png')
        self.showerOff = QPixmap('pics/showeroff.png')
        #self.setPixmap(self.showerOff)

    def setShower(self, statusOn):
        if(statusOn):
            self.setPixmap(self.showerOn)
        else:
            self.setPixmap(self.showerOff)


