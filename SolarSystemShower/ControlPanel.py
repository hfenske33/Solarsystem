'''
Use the control user interface to perform the basic functions
of the program: turn on / off the shower, refill tanks, start/stop
collector and view graphs. In addition, all important parameters
are listed with their current value in labels. If the program is running,
a thread which updates labels and graphics every 5 secs is also
running.
'''

import _thread
import os
import time
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QDial, QLabel, QPushButton

import AdditionalOperations as AO
import BasicOperations as BO
import XMLSaver as XS
import Statistics as Stat
from Parameter import Parameters as P


class UIControl(QFrame):
    def __init__(self, graphicUI):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.graphicUI = graphicUI
        self.labelWidth = 130

        self.xmlControll = XS
        xmlPath = Path("temp/" + AO.getDate() + ".xml")
        if(xmlPath.exists()):
            self.xmlControll.loadLastData()

        # Label for Temperature-Text
        self.labelTempText = QLabel(self)
        self.labelTempText.setText("Temperature shower [K] : ")
        self.labelTempText.setFixedWidth(180)
        self.labelTempText.move(20, 30)

        # Label for Temperature
        self.labelTemp = QLabel(self)
        self.labelTemp.setText("290")
        self.labelTemp.move(200, 30)
        self.labelTemp.setFixedWidth(30)
        self.labelTemp.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Dial-to regulate Temperature
        self.dial = QDial(self)
        self.dial.setMaximum(P.hotTankTemp)
        self.dial.setMinimum(P.coldTankTemp)
        self.dial.setNotchesVisible(True)
        self.dial.setFocusPolicy(Qt.StrongFocus)
        self.dial.move(100, 60)
        self.dial.valueChanged.connect(self.labelTemp.setNum)

        # Button to start shower
        self.startButton = QPushButton(self)
        self.startButton.setText("Start Shower")
        self.startButton.move(10, 200)
        self.startButton.clicked.connect(self.handleShowerButton)

        # Button to refill tanks
        self.refillButton = QPushButton(self)
        self.refillButton.setText("Refill Tanks")
        self.refillButton.move(140, 200)
        self.refillButton.clicked.connect(self.refillTanks)

        # Button to start collector
        self.startCollectorButton = QPushButton(self)
        self.startCollectorButton.setText("Start Collector")
        self.startCollectorButton.move(270, 200)
        self.startCollectorButton.clicked.connect(self.handleCollector)

        # Label for Time-Text
        self.labelTimeText = QLabel(self)
        self.labelTimeText.setText("Time (hh:mm): ")
        self.labelTimeText.setFixedWidth(180)
        self.labelTimeText.move(10, 270)

        # Label for Time
        self.labelTime = QLabel(self)
        t = AO.getTime()
        self.labelTime.setText(t)
        self.labelTime.move(220, 270)
        self.labelTime.setFixedWidth(self.labelWidth)
        self.labelTime.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-Outside-Text
        self.labelTempOutText = QLabel(self)
        self.labelTempOutText.setText("Ambient temperature [K]: ")
        self.labelTempOutText.setFixedWidth(180)
        self.labelTempOutText.move(10, 300)

        # Label for Temperature-Outside
        self.labelTempOut = QLabel(self)
        t = AO.getTemperature()
        self.labelTempOut.setText(str(t))
        self.labelTempOut.move(220, 300)
        self.labelTempOut.setFixedWidth(self.labelWidth)
        self.labelTempOut.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-hot-tank-Text
        self.labelTempTankHotText = QLabel(self)
        self.labelTempTankHotText.setText("Temperature hot tank [K]: ")
        self.labelTempTankHotText.setFixedWidth(180)
        self.labelTempTankHotText.move(10, 330)

        # Label for Temperature-tank-hot
        self.labelTempTankHot = QLabel(self)
        self.labelTempTankHot.setText(str(P.hotTankTemp))
        self.labelTempTankHot.move(220, 330)
        self.labelTempTankHot.setFixedWidth(self.labelWidth)
        self.labelTempTankHot.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-cold-tank-Text
        self.labelTempTankColdText = QLabel(self)
        self.labelTempTankColdText.setText("Temperature cold tank [K]: ")
        self.labelTempTankColdText.setFixedWidth(180)
        self.labelTempTankColdText.move(10, 360)

        # Label for Temperature-tank-cold
        self.labelTempTankCold = QLabel(self)
        self.labelTempTankCold.setText(str(P.coldTankTemp))
        self.labelTempTankCold.move(220, 360)
        self.labelTempTankCold.setFixedWidth(self.labelWidth)
        self.labelTempTankCold.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Temperature-Collector-Text
        self.labelTempCollectorText = QLabel(self)
        self.labelTempCollectorText.setText("Temperature collector [K]: ")
        self.labelTempCollectorText.setFixedWidth(180)
        self.labelTempCollectorText.move(10, 390)

        # Label for Temperature-Collector
        self.labelTempCollector = QLabel(self)
        self.labelTempCollector.setText("290")
        self.labelTempCollector.move(220, 390)
        self.labelTempCollector.setFixedWidth(self.labelWidth)
        self.labelTempCollector.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Collector-Mass-Of-Water-Text
        self.labelCollectorMassText = QLabel(self)
        self.labelCollectorMassText.setText("Collector mass [Kg]: ")
        self.labelCollectorMassText.setFixedWidth(180)
        self.labelCollectorMassText.move(10, 420)

        # Label for Collector-Mass-Of-Water
        self.labelCollectorMass = QLabel(self)
        self.labelCollectorMass.setText("20")
        self.labelCollectorMass.move(220, 420)
        self.labelCollectorMass.setFixedWidth(self.labelWidth)
        self.labelCollectorMass.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Tank-Mass-Of-Water-Text
        self.labelTankHotMassText = QLabel(self)
        self.labelTankHotMassText.setText("Tank hot mass [Kg]: ")
        self.labelTankHotMassText.setFixedWidth(180)
        self.labelTankHotMassText.move(10, 450)

        # Label for Tank-Mass-Of-Water
        self.labelTankHotMass = QLabel(self)
        self.labelTankHotMass.setText("300")
        self.labelTankHotMass.move(220, 450)
        self.labelTankHotMass.setFixedWidth(self.labelWidth)
        self.labelTankHotMass.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Tank-Mass-Of-Cold-Water-Text
        self.labelTankMassColdText = QLabel(self)
        self.labelTankMassColdText.setText("Tank cold mass [Kg]: ")
        self.labelTankMassColdText.setFixedWidth(180)
        self.labelTankMassColdText.move(10, 480)

        # Label for Tank-Mass-Of-Water
        self.labelTankMassCold = QLabel(self)
        self.labelTankMassCold.setText("300")
        self.labelTankMassCold.move(220, 480)
        self.labelTankMassCold.setFixedWidth(self.labelWidth)
        self.labelTankMassCold.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Solar-Irradiance-Text
        self.labelSolarIrradianceText = QLabel(self)
        self.labelSolarIrradianceText.setText("Solar irradiance [W/m²]: ")
        self.labelSolarIrradianceText.setFixedWidth(180)
        self.labelSolarIrradianceText.move(10, 510)

        # Label for Solar-Irradiance
        self.labelSolarIrradiance = QLabel(self)
        self.labelSolarIrradiance.setText(AO.getSolarIrradianceString())
        self.labelSolarIrradiance.move(220, 510)
        self.labelSolarIrradiance.setFixedWidth(self.labelWidth)
        self.labelSolarIrradiance.setStyleSheet("background-color: rgb(255, 255, 255)")

        # Label for Solar-Irradiance-Text
        self.labelSolarIrradianceText = QLabel(self)
        self.labelSolarIrradianceText.setText("Statistics:")
        self.labelSolarIrradianceText.setFixedWidth(180)
        self.labelSolarIrradianceText.move(10, 570)

        # Button to show heatening-statistics
        self.diagrammButton = QPushButton(self)
        self.diagrammButton.setText("Heatening")
        self.diagrammButton.move(10, 600)
        self.diagrammButton.setFixedWidth(90)
        self.diagrammButton.setToolTip('Show diagram of Runge-Kutta-Calculation for collector heating the hot tank')
        self.diagrammButton.clicked.connect(self.showDiagrams)

        # Button to show temp - statistics
        self.statisticTempButton = QPushButton(self)
        self.statisticTempButton.setText("Temperature")
        self.statisticTempButton.move(10, 650)
        self.statisticTempButton.setFixedWidth(90)
        self.statisticTempButton.setToolTip('Show temperature - statistics of the day')
        self.statisticTempButton.clicked.connect(self.showTempStatistic)

        # Button to show level - statistics
        self.statisticLevelButton = QPushButton(self)
        self.statisticLevelButton.setText("Fluid-level")
        self.statisticLevelButton.move(150, 600)
        self.statisticLevelButton.setFixedWidth(90)
        self.statisticLevelButton.setToolTip('Show fluid - level - statistics of the day')
        self.statisticLevelButton.clicked.connect(self.showLevelStatistic)

        # Button to clear - statistics
        self.clearStatButton = QPushButton(self)
        self.clearStatButton.setText("Clear")
        self.clearStatButton.move(150, 650)
        self.clearStatButton.setFixedWidth(90)
        self.clearStatButton.setToolTip('Clear the daily statistics and start a new round')
        self.clearStatButton.setStyleSheet("background-color:rgb(220, 255, 255)");
        self.clearStatButton.clicked.connect(self.clearStatistic)

        # Label for Information
        self.labelInformation = QLabel(self)
        self.labelInformation.setFixedWidth(350)
        self.labelInformation.setFixedHeight(100)
        self.labelInformation.move(10, 700)

        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color: rgb(240, 255, 255)")
        self.setFixedHeight(800)
        self.setFixedWidth(400)

        try:
            _thread.start_new_thread(self.updateLabelsAndValues, ())
            _thread.start_new_thread(BO.TempChanging, ())
        except:
            print("Error: unable to start thread")


    def handleShowerButton(self):
        if(P.showerOn):
            self.stopShower()
        else:
            self.startShower()

    def startShower(self):
        self.startButton.setText("Stop Shower")
        P.showerOn = True
        self.blockButtons()
        self.graphicUI.updateGraphics()
        Tshower = int(self.labelTemp.text())
        BO.flowRate(Tshower)
        self.labelInformation.setText("Shower startet, Hot/Cold [kg/s]: " + P.flowRateHC)
        self.xmlControll.save()


    def stopShower(self):
        self.labelInformation.setText("Shower stoped")
        self.startButton.setText("Start Shower")
        P.showerOn = False
        self.freeButtons()
        self.graphicUI.updateGraphics()
        self.xmlControll.save()


    def emptyTanks(self):
        if(not AO.getLevelColdTank()):
            self.labelInformation.setText("Cold Tank is empty")
        if(not AO.getLevelHotTank()):
            self.labelInformation.setText("Hot Tank is empty")

    def updateLabelsAndValues(self):
        while(True):
            self.labelTankHotMass.setText(str(P.fluidLevelHot))
            self.labelTankMassCold.setText(str(P.fluidLevelCold))
            self.labelTime.setText(AO.getTime())
            self.labelSolarIrradiance.setText(AO.getSolarIrradianceString())
            self.labelTempTankHot.setText(str(round(P.hotTankTemp, 4)))
            self.labelTempTankCold.setText(str(round(P.coldTankTemp, 4)))
            self.labelTempCollector.setText(str(round(P.collectorTemp, 4)))
            self.dial.setMaximum(P.hotTankTemp)
            self.dial.setMinimum(P.coldTankTemp)
            if(P.collectorIsOn):
                BO.startTimeCalculator()
                self.labelInformation.setText("Collector is running.\nCalculated Time ~" + str(round(P.calcTimeForHeatUp)) + "sec")

            if(P.collectorIsOn and P.hotTankTemp >= 340):
                self.startCollectorButton.setText("Start Collector")
                self.labelInformation.setText("Collector stoped.\nHot Tank Temp = " + str(round(P.hotTankTemp, 2)) + "K")
                self.freeButtons()
                P.collectorIsOn = False
            AO.setSolarIrradiance()
            AO.getTemperature()
            self.graphicUI.updateGraphics()
            self.emptyTanks()
            self.xmlControll.save()
            time.sleep(5)


    def refillTanks(self):
        self.labelInformation.setText("Tanks where refilled")
        BO.refill()
        self.graphicUI.updateGraphics()
        self.xmlControll.save()



    def blockButtons(self):
        self.clearStatButton.setEnabled(False)
        self.statisticLevelButton.setEnabled(False)
        self.statisticTempButton.setEnabled(False)
        self.diagrammButton.setEnabled(False)


    def freeButtons(self):
        self.clearStatButton.setEnabled(True)
        self.statisticLevelButton.setEnabled(True)
        self.statisticTempButton.setEnabled(True)
        self.diagrammButton.setEnabled(True)


    def handleCollector(self):
        if(not P.collectorIsOn):
            self.startCollector()
        else:
            self.stopCollector()


    def startCollector(self):
        if(P.currentSolarIrradiance != 0):
            self.startCollectorButton.setText("Stop Collector")
            self.labelInformation.setText("Collector started")
            P.collectorIsOn = True
            P.collectorFlowRate = 0.8
            self.blockButtons()
            self.graphicUI.updateGraphics()
        else:
            self.labelInformation.setText("Collector is only working when\ncurrent solar irradiance is not zero.")





    def stopCollector(self):
        self.startCollectorButton.setText("Start Collector")
        self.labelInformation.setText("Collector stoped")
        P.collectorIsOn = False
        P.collectorFlowRate = 0
        self.freeButtons()
        self.graphicUI.updateGraphics()


    def showDiagrams(self):
        Stat.showCalculationStatistics()

    def showTempStatistic(self):
        xmlPath = str("temp/" + AO.getDate() + ".xml")
        if (os.path.exists(xmlPath)):
            Stat.showTempStatistics()

    def showLevelStatistic(self):
        xmlPath = str("temp/" + AO.getDate() + ".xml")
        if (os.path.exists(xmlPath)):
            Stat.showLevelStatistics()

    def clearStatistic(self):
        self.labelInformation.setText("New round: Temperatures and fluid-levels at\ninitial (no statistics of both available).")
        self.xmlControll.clearStatistics()
        P.fluidLevelCold = 300
        P.fluidLevelHot = 300
        P.hotTankTemp = 320
        P.coldTankTemp = 290
        P.collectorTemp = 300
        self.graphicUI.updateGraphics()

