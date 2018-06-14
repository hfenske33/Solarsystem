'''
The Parameter class is a supporting class that provides all the
required parameters. Because of the static character of the
parameters, different objects can access and change the values
of the current parameters.
'''

class Parameters:
    showerOn = False
    collectorIsOn = False

    fluidLevelCold = 300
    fluidLevelHot = 300

    hotTankTemp = 300
    coldTankTemp = 290
    collectorTemp = 320
    ambientTemp = 300

    flowRateHC = ""
    flowRate = 5

    #usually in germany ~1400
    solarIrradiance = 1400
    currentSolarIrradiance = 0

    calcTimeForHeatUp = 0
    collectorFlowRate = 0
