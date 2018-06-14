import _thread
import time

import AdditionalOperations as AO
from Parameter import Parameters as P
import Solar
import ODESolver



def flowRate(Tshower):
    Tcold = P.coldTankTemp
    Thot = P.hotTankTemp

    if(Tshower > Tcold and Tshower < Thot):
        flowRateCold = (Tshower - Thot)/(Tcold - Thot)
        flowRateHot = 1 - flowRateCold
    elif(Tshower <= Tcold):
        flowRateCold = 1
        flowRateHot = 0
    elif(Tshower >= Thot):
        flowRateCold = 0
        flowRateHot = 1

    P.flowRateHC = str(round(flowRateHot * P.flowRate, 2)) + " / " + str(round(flowRateCold * P.flowRate, 2))

    try:
        _thread.start_new_thread(letItFlow, (flowRateCold, flowRateHot, ))
    except:
        print("Error: unable to start thread_letItFlow")


def letItFlow(flowRateCold, flowRateHot):
    while(P.showerOn):
        time.sleep(1)
        hotFlow(flowRateHot)
        coldFlow(flowRateCold)


def coldFlow(flowRateCold):
    if(AO.getLevelColdTank()):
        P.fluidLevelCold = round(
            P.fluidLevelCold - flowRateCold * P.flowRate, 2)


def hotFlow(flowRateHot):
    if(AO.getLevelHotTank()):
        P.fluidLevelHot = round(
            P.fluidLevelHot - flowRateHot * P.flowRate, 2)


def refill():
    tempPerc = P.fluidLevelHot / 300
    P.hotTankTemp = tempPerc * P.hotTankTemp + (1 - tempPerc) * P.ambientTemp

    tempPerc = P.fluidLevelCold / 300
    P.coldTankTemp = tempPerc * P.coldTankTemp + (1 - tempPerc) * P.ambientTemp
    P.fluidLevelHot = 300
    P.fluidLevelCold = 300


def TempChanging():
    solarSystem1 = Solar.SolarSystem()
    odeSolver1 = ODESolver.Euler(solarSystem1)

    i = 0
    while(True):
        solarSystem1.mt = P.fluidLevelHot
        solarSystem1.mtf = P.fluidLevelCold
        odeSolver1.integrate(i)
        i += 1
        time.sleep(1)


def startTimeCalculator():
    solarSystem2 = Solar.SolarSystem()
    odeSolver2 = ODESolver.Euler(solarSystem2)
    solarSystem2.mt = P.fluidLevelHot
    odeSolver2.getCalcTime()
    solarSystem2.mt = P.fluidLevelHot
    odeSolver2.getCalcTime()
    print("#################CalculatedTime = " + str(P.calcTimeForHeatUp))


