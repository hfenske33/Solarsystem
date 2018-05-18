from PyQt5.QtWidgets import QFrame, QDial, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen


class ControlField(QFrame):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.StyledPanel)

        # Label for Temperature-Text
        self.labelTemp = QLabel(self)
        self.labelTemp.setText("Temperature in Kelvin [K] : ")
        self.labelTemp.setFixedWidth(180)
        self.labelTemp.move(20, 30)

        # Label for Temperature
        self.label = QLabel(self)
        self.label.setText("290")
        self.label.move(190, 30)
        self.label.setFixedWidth(30)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Dial-to regulate Temperature
        self.dial = QDial(self)
        self.dial.setMaximum(340)
        self.dial.setMinimum(290)
        self.dial.setNotchesVisible(True)
        self.dial.setFocusPolicy(Qt.StrongFocus)
        self.dial.move(100, 60)

        self.dial.valueChanged.connect(self.label.setNum)

        # Button to start shower
        self.startButton = QPushButton(self)
        self.startButton.setText("Start Shower")
        self.startButton.move(100, 200)

        # Label for Temperature-Outside-Text
        self.labelTempOutText = QLabel(self)
        self.labelTempOutText.setText("Temperature outside [K]: ")
        self.labelTempOutText.setFixedWidth(180)
        self.labelTempOutText.move(10, 300)

        # Label for Temperature-Outside
        self.labelTempOut = QLabel(self)
        self.labelTempOut.setText("290")
        self.labelTempOut.move(190, 300)
        self.labelTempOut.setFixedWidth(30)
        self.labelTempOut.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-Outside-Text
        self.labelTempTankText = QLabel(self)
        self.labelTempTankText.setText("Temperature tank [K]: ")
        self.labelTempTankText.setFixedWidth(180)
        self.labelTempTankText.move(10, 330)

        # Label for Temperature-Outside
        self.labelTempTank = QLabel(self)
        self.labelTempTank.setText("290")
        self.labelTempTank.move(190, 330)
        self.labelTempTank.setFixedWidth(30)
        self.labelTempTank.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-Collector-Text
        self.labelTempCollectorText = QLabel(self)
        self.labelTempCollectorText.setText("Temperature collector [K]: ")
        self.labelTempCollectorText.setFixedWidth(180)
        self.labelTempCollectorText.move(10, 360)

        # Label for Temperature-Collector
        self.labelTempCollector = QLabel(self)
        self.labelTempCollector.setText("290")
        self.labelTempCollector.move(190, 360)
        self.labelTempCollector.setFixedWidth(30)
        self.labelTempCollector.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Collector-Mass-Of-Water-Text
        self.labelCollectorMassText = QLabel(self)
        self.labelCollectorMassText.setText("Collector mass [Kg]: ")
        self.labelCollectorMassText.setFixedWidth(180)
        self.labelCollectorMassText.move(10, 390)

        # Label for Collector-Mass-Of-Water
        self.labelCollectorMass = QLabel(self)
        self.labelCollectorMass.setText("10")
        self.labelCollectorMass.move(190, 390)
        self.labelCollectorMass.setFixedWidth(30)
        self.labelCollectorMass.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Tank-Mass-Of-Water-Text
        self.labelTankMassText = QLabel(self)
        self.labelTankMassText.setText("Tank mass [Kg]: ")
        self.labelTankMassText.setFixedWidth(180)
        self.labelTankMassText.move(10, 420)

        # Label for Tank-Mass-Of-Water
        self.labelTankMass = QLabel(self)
        self.labelTankMass.setText("320")
        self.labelTankMass.move(190, 420)
        self.labelTankMass.setFixedWidth(30)
        self.labelTankMass.setStyleSheet("background-color: rgb(255, 255, 255)")


        # Button to show diagrams
        self.diaButton = QPushButton(self)
        self.diaButton.setText("Show Diagrams")
        self.diaButton.move(100, 750)

        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color: rgb(230, 255, 255)")
        self.setFixedHeight(800)
        self.setFixedWidth(300)

