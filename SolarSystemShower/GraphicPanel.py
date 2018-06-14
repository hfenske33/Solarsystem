'''
The graphic user interface illustrates the position of the
sun (important for solar irradiance), the collector, the
two tanks (hot water, cold water, level, temperature) and
represents the shower symbolically. With the help of the
shower-head you can see if the shower is switched on or not.
If the shower is on, the tanks-level is going lower. The color
of the tanks depends on the temperature.
'''

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPainter, QColor, QPen, QLinearGradient, QPalette, QBrush
from PyQt5.QtWidgets import QWidget

import AdditionalOperations as AO
from Parameter import Parameters as P


class UIGraphic(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 800
        self.showerIsOn = False
        self.initUI()
        self.update()

    def initUI(self):
        self.setGeometry(0, 0, self.width, self.height)

        self.setAutoFillBackground(True)
        palette = self.palette()

        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(180, 200, 200))
        palette.setBrush(QPalette.Window, QBrush(gradient))


        self.setPalette(palette)
        self.setCoordinates()
        self.show()

    def updateGraphics(self):
        self.m.update()


    def setCoordinates(self):
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(self.width, self.height)


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.black)

        self.paintHotTank(P.fluidLevelHot / 300, 300, qp)
        self.paintColdTank(P.fluidLevelCold / 300, 300, qp)
        self.paintCollector(qp)
        self.paintSun(qp)
        self.paintShower(qp, P.showerOn)
        self.drawArrows(qp)


    def paintHotTank(self, fillInt, tempint, painter):
        # Hot tank
        painter.setBrush(AO.getColorHotTank())
        painter.drawRect(400, 350 + (200 - fillInt * 200), 100, 200 * fillInt)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawText(380, 580, "Hot Water, Fluid level: " + str(round(100 * fillInt, 2)) + "%, T = " + str(
            round(P.hotTankTemp, 2)) + "K")


    def paintColdTank(self, fillInt, tempint, painter):
        # Cold tank
        painter.setBrush(AO.getColorColdTank())
        painter.drawRect(150, 350 + (200 - fillInt * 200), 100, 200 * fillInt)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawText(20, 580, "Cold Water, Fluid level: " + str(round(100 * fillInt, 2)) + "%, T = " + str(
            round(P.coldTankTemp, 2)) + "K")


    def paintCollector(self, painter):
        # Collector with time-axis
        painter.setBrush(QColor(200, 0, 0))
        painter.drawLine(0, 250, 700, 250)

        painter.setBrush(QColor(250, 240, 240))
        painter.drawRect(225, 200, 230, 50)

        painter.setBrush(QColor(0, 0, 0))
        painter.drawText(200, 100, 300, 130, 100, "Collector, T [K] = " + str(round(P.collectorTemp, 4)))

        painter.drawLine(340, 250, 340, 255)
        painter.drawText(325, 270, "12:00")
        painter.drawLine(240, 250, 240, 255)
        painter.drawText(225, 270, "10:00")
        painter.drawLine(440, 250, 440, 255)
        painter.drawText(425, 270, "14:00")
        painter.drawLine(140, 250, 140, 255)
        painter.drawText(125, 270, "08:00")
        painter.drawLine(540, 250, 540, 255)
        painter.drawText(525, 270, "16:00")
        painter.drawLine(40, 250, 40, 255)
        painter.drawText(25, 270, "06:00")
        painter.drawLine(640, 250, 640, 255)
        painter.drawText(625, 270, "18:00")

    def paintSun(self, painter):
        painter.setBrush(QColor(250, 250, 0))
        time = AO.getTimeInt()
        x = AO.getXSunCoordinate(time)
        y = AO.getYSunCoordinate(x)
        painter.drawEllipse(315 - x, 200 - y, 60, 60)

    def paintShower(self, painter, isOnBool):
        if(isOnBool):
            i = QImage("pics/showeron")
        else:
            i = QImage("pics/showeroff")
        r = QRect(290, 650, 100, 100)
        painter.drawImage(r, i)

    def drawArrows(self, painter):
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)
        painter.drawLine(200, 600, 450, 600)
        painter.drawLine(200, 600, 200, 590)
        painter.drawLine(450, 600, 450, 590)

        if(P.collectorIsOn):
            a1 = QImage("pics/arrow1")
            r = QRect(340, 280, 50, 50)
            painter.drawImage(r, a1)

            a2 = QImage("pics/arrow1a")
            r = QRect(400, 280, 50, 50)
            painter.drawImage(r, a2)

        a3 = QImage("pics/arrow2")
        r = QRect(315, 595, 50, 60)
        painter.drawImage(r, a3)

